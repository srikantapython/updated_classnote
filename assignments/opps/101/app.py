
#101. 101 Write a class(DB) program to create a table, insert values, update values, delete values of the table. 
#All database operations code write in a file(db_operations.py) and call these operations in another file( app.py).
#In app.py create instance of the DB class and call all the methods by passing some data.

from db_operation import Dboperation
print """
      Enter
      1.for create table
      2.delete value
      3.insert value
      4.update value
      5.quit
      """
opt=int(raw_input())
print "Enter Table Name"
table_name=raw_input()
db_instance=Dboperation()

if opt==1:
	db_instance.create_table(table_name)

# elif opt==2:
# 	db_instance.create_table(table_name)

elif opt==3:
	print "Enter id and name"
	try:
		st_id=int(raw_input())
	except Exception as err:
		print err
	name=raw_input()
	db_instance.insert_table(table_name,st_id,name)

elif opt==4:
	print "Enter id and updated name"
	try:
		st_id=int(raw_input())
		name=raw_input()
	except Exception as err:
		print err
	db_instance.update_table(table_name,st_id,name)

else:
	import sys
	sys.exit()