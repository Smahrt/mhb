#!/usr/bin/python
# Author: Justice Amoh
# Description: Script to build sqlite3 database out of hymn files (.mhb)


import sqlite3, glob, codecs, os, sys

database =sqlite3.connect("mhb.db")
cursor = database.cursor()


#creating a table
cursor.execute('drop table if exists a')
cursor.execute("""CREATE TABLE a 
	(mhb integer primary key, title text, author text, url text, hymn text)""")


os.chdir("data")
for ifile in glob.glob("*.mhb"):
	with codecs.open(ifile,"r","utf-8") as f:
		ifile=ifile.rstrip('.mhb')
		url=f.readline().rstrip('\n')
		title=f.readline().rstrip('\n')
		author=f.readline().rstrip('\n')
		dump=f.readline()		

		#TODO temporary hack to read all of code
		lyrics=''
		temp=f.read()
		while(temp!=''):
			hymn+=temp
			temp=f.read()

		# sql = "INSERT INTO a VALUES (?, ?, ?, ?)" 
		# values = [ifile.rstrip('.mhb'),title,author,url]

		sql = "INSERT INTO hymns VALUES (?, ?, ?, ?, ?)" 
		values = [ifile, title, author, url, hymn]
 		cursor.execute(sql,values)


# query: display all of table a
# cursor.execute("select * from a")
# for row in cursor:
#     print row 		

#save updates and close database
database.commit()
database.close()
