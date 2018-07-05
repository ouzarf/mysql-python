import mysql, sys

import mysql.connector

mydb = mysql.connector.connect(user='root', password='',
                               host='127.0.0.1',
                               database='menu')

cur = mydb.cursor()

fish = sys.argv[1]
price = sys.argv[2]

# statement = "INSERT INTO fish(name, price) VALUES(%s, %s)" %(fish,price)
cur.execute("INSERT INTO fish(name, price) VALUES(%s, %s)" ,(fish,price))

print("---------------------------------------")
print(" WHERE value = 7,50")
print("---------------------------------------")    
value = "7.50"
cur.execute("SELECT * FROM fish WHERE price = %s" %(value))
# print all the first cell of all the rows
for row in cur.fetchall():
    print(row[0],"-->",row[1],"@",row[2],"each")

