import mysql.connector

connection_params = {
    'host': "localhost",
    'user': "",
    'password': "",
    'port': 3306,
}

host = input("renseignez le host (si différent de localhost) : ")
if host != "":
    connection_params["host"] = host

user = input("renseignez le user : ")
if user != "":
    connection_params["user"] = user

password = input("renseignez le password : ")
if password != "":
    connection_params["password"] = password

port = input("renseignez le port (si différent de 3306) : ")
if port != "":
    connection_params["port"] = port

print("Quelle base de données souhaitez vous installer ?")
print("1 - Employées")
print("2 - World")
print("3 - Chinook")
print("4 - Sakila")
choice = input()

mydb = mysql.connector.connect(**connection_params)

mycursor = mydb.cursor()

if (choice == "1"):
    db_name = "employees"
if (choice == "2"):
    db_name = "world"
if (choice == "3"):
    db_name = "chinook"
if (choice == "4"):
    db_name = "sakila"

with open('./databases/' + db_name + '.sql', encoding="utf-8") as f:
    query = ""
    for line in f:
        if((line[0:2] != "--") and line[0] != "\n"):
            query += line.strip()
            if(query[-1] == ";"):
                mycursor.execute(query)
                mydb.commit()
                query = ""