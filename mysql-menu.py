import mysql
import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='menu')

cur = cnx.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM fish ")

# print all the first cell of all the rows
for row in cur.fetchall():
    print(row[0],"-->",row[1],"@",row[2],"each")

print("---------------------------------------")
print(" WHERE price > 7")
print("---------------------------------------")
cur.execute("SELECT * FROM fish WHERE price > 7")

# print all the first cell of all the rows
for row in cur.fetchall():
    print(row[0],"-->",row[1],"@",row[2],"each")

# Modifying the results

operation = input("entrez l'operation = : ")
value = input("value: ")
cur.execute("SELECT * FROM fish WHERE price %s %s" %(operation, value))
# print all the first cell of all the rows
for row in cur.fetchall():
    print(row[0],"-->",row[1],"@",row[2],"each")



statement = """SHOW TABLES"""
cur.execute(statement)
table_list = []
for record in cur.fetchall():
    table_list.append(record[0])