# import psycopg2
# con=psycopg2.connect(host="localhost",user="postgres",password="root",database="db1")
# cur=con.cursor()
import sqlite3
class Dboperation:
	con=sqlite3.connect("db2.db")
	cur=con.cursor()

	def insert_table(self,table_name,st_id,name):
		try:

			 q= "insert into %s(id, name) values(%s,'%s')"%(table_name,st_id,name)
			 self.cur.execute(q)
			 self.con.commit()
		except Exception as err:
			print "Error:",err
			print "some error is there"


	def create_table(self,table_name):
		try:
			q="create table %s (id int,name varchar(250))"%(table_name)
			self.cur.execute(q)
			print "see database"
		except Exception as err:
			print "Error:",err
			print "some error"

	def update_table(self,table_name,st_id,name):
		try:

			 q="update %s set name='%s' where id=%s"%(table_name,name,st_id)
			 self.cur.execute(q)
			 self.con.commit()
		except Exception as err:
			print "Error:",err
			print "some error is there"