import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="lizard",
  password="adidas88"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

