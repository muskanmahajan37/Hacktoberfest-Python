import mysql.connector
con = mysql.connector.connect(user='root',password ='tigermanudon!1234',host ='localhost')
mycursor = con.cursor()
mycursor.execute("Create database DAV University")
mycursor.execute("Use DAV University")

