
from . import main as dbc
import os
import yaml
import pymysql as MySQLdb
from pathlib import Path
globalconenction=None

# DB connection
class Model:

    def connect(**constr):
        global globalconenction
        # Db connection
        db = dbc.DBconnect()
        if 'printQuery' in constr :db.printQuery=op
        # connection
        
        if type(constr)==dict:
            db.connect(**constr)
        globalconenction=db
        return db

class table:
      def __new__(self,name):
          global globalconenction
          return  globalconenction.table(name)
class query:
      def __new__(self,q):
          global globalconenction
          return  globalconenction.query(q)

class UnbufferedCursor:     
      
    def connect(self,set_cursor="dict"):

        if set_cursor=="dict":
            set_cursor = MySQLdb.cursors.SSDictCursor
        else:
            set_cursor = MySQLdb.cursors.SSCursor

        self.connection = MySQLdb.connect(host=CONFIG['database']['host'], user=CONFIG['database']['user'], passwd=CONFIG['database']['password'], db=CONFIG['database']['db'], cursorclass=set_cursor)
        return self

    def query(self,sql):
        
        self.cursor = self.connection.cursor()
        self.cursor.execute(sql)
        return self.cursor,self.connection

    def insert_query(self,sql):
        
        self.cursor = self.connection.cursor()
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print("Sql : " + sql)
            print("Error : {}".format(e))
            self.connection.rollback()
        lastrowid = self.cursor.lastrowid
        self.cursor.close()
        self.connection.close()

        return lastrowid