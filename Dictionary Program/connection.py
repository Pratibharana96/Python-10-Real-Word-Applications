import mysql.connector
con= mysql.connector.connect(
user = "root",
password="",
host="localhost",
database="dictionarypy"
)
cursor = con.cursor()
query = cursor.execute("SELECT * FROM dicsearch")
result = cursor.fetchall()
print (result)
