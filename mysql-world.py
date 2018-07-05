import mysql
import mysql.connector

mydb = mysql.connector.connect(user='root', password='',
                               host='127.0.0.1',
                               database='world')

cur = mydb.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM city ")

# print all the first cell of all the rows
for row in cur.fetchall():
    print(row[0],"-->",row[1],"@",row[2],"@",row[3],"@",row[4])

print("---------------------------------------")
print(" WHERE population > 150000")
print("---------------------------------------")
cur.execute("SELECT * FROM city WHERE population > 150000")

# print all the first cell of all the rows
for row in cur.fetchall():
    print(row[0],"-->",row[1],"@",row[2],"@",row[3],"@",row[4])

print("---------------------------------------")
print(" WHERE value = 150000")
print("---------------------------------------")    
value = "150000"
cur.execute("SELECT * FROM city WHERE population = %s" %(value))
# print all the first cell of all the rows
for row in cur.fetchall():
    print(row[0],"-->",row[1],"@",row[2],"@",row[4])

table = 'City'
column = 'Name'
term = 's%'
statement = """select * from %s where %s like '%s'""" %(table, column,term)

command = cur.execute(statement)
results = cur.fetchall()

print(results)

record_list = []
for record in results:
    record_list.append(record[0])
for i in range(0, len(record_list)):
    
    print ("%s. %s" %(i+1, record_list[i]))


