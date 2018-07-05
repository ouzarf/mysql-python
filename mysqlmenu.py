import mysql
import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='menu')

cur = cnx.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM fish")

# print all the first cell of all the rows
for row in cur.fetchall():
    print(row[0],row[1],row[2])


cnx.close()
