import mysql
import mysql.connector

mydb = mysql.connector.connect(user='root', password='',
                               host='127.0.0.1',
                               database='world')

cur = mydb.cursor()

# Use all the SQL you like
cur.execute("""SHOW TABLES""")

results = cur.fetchall()
print("number of  tables is = ",len(results))
print ("--------------------------")
print ("Which table would you like to use?")
for i in range(0, len(results)): print (i+1, results[i][0])
choice = input("Input number:")

choice.isdigit()

choice_string = str(choice)
confirm = input("Did you mean %s?" %(choice_string[0]))

real_choice = int(choice_string[0])
print("real_choice =",real_choice)


table_statement = """DESCRIBE %s""" %(results[real_choice-1][0])
cur.execute(table_statement)
table_desc = cur.fetchall()
for i in range(0, len(table_desc)):
    print( table_desc[i])


print( table_desc[0][0])
print( table_desc[0][1])
print("----------------")
print( table_desc[1][2])
print( table_desc[1][3])
print("----------------")
print( table_desc[2][1])
print( table_desc[3][0])
print("----------------")
print( table_desc[3][4])


print ("The records of table %s follow this format:" %(results[real_choice-1][0]))
for i in range(0, len(table_desc)):
    print( table_desc[i][0])

