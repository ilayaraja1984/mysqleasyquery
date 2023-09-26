from  mysql_fastconnector import  Model ,table,query


conn = Model.connect(database="sports", user = "root", password = "Admin@123", host = "127.0.0.1")

# id=table("users").insertMany([{'first_name':'r33333333333332XXXXXXXXXXx','last_name':'r33333333','id':'555','email':'aa@gmail.com','mobile':'987654321'},{'first_name':'r3333333333XXXXXXXXXXx','last_name':'r33333333','id':'555','email':'aa@gmail.com','mobile':'987654321'}]).getId()
# print(id)

# id=table("images").insert({'image':'r222222222XXXXXXXXXXx','user_id':id},'pk').getId()
# print(id)

# id=table("users").update({'first_name':'r33333333333332XXXXXXXXXXx','last_name':'r33333333','id':'555','email':'aa@gmail.com','mobile':'987654321'},"pk=1")
# print(id)

# id=table("users").delete("pk=2")
# print(id)
# res=table("users").fromTable('pk').where('pk=1').all()

res=table("players").one()

for v in res:   
    print(res)

print("Opened database successfully")