import mysql.connector

#Connect to the server
mydb = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "Soccer1624?")

#Create a cursor
mycur = mydb.cursor(buffered = True)

#execute the query
mycur.execute("USE museum")
mycur.execute("SELECT * FROM art_object")

#Insert a new row
insert_art_object = "INSERT INTO art_object (id_no, origin, title, epoch, description, year) VALUES (%s,%s,%s,%s,%s,%s) "
data_art_object = (10005, 'origin2', 'title2', 'epoch2', 'desc2', 2023)
mycur.execute(insert_art_object, data_art_object)
mydb.commit()

rows = mycur.fetchall()
print("Current Art Object Table Content:")
size = len(rows)
for i in range(size):
    print(rows[i])

mydb.close()