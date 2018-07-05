# mysql-python
install

http://apprendre-python.com/page-database-data-base-donnees-query-sql-mysql-postgre-sqlite

https://pythonspot.com/mysql-with-python/
https://www.tutorialspoint.com/python/python_database_access.htm
https://www.youtube.com/watch?v=ryLsp6m1PnY

http://www.mysqltutorial.org/python-mysql/

sudo pip install mysql-connector-python
Or download it from: http://dev.mysql.com/downloads/connector/python/
Documentation: http://dev.mysql.com/doc/refman/5.5/en/connector-python.htm

import mysql
import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='menu')


### Use all the SQL you like
cur = cnx.cursor()
### execute  the SQL 
cur.execute("SELECT * FROM fish")
### fetch the first table fish
for row in cur.fetchall():
### print all the first cell of all the rows
    print(row[0],row[1],row[2])

cnx.close()
