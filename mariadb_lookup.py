#!/usr/bin/python 

# taken from https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/ 

import mariadb 

conn = mariadb.connect( 
  user="root", 
  password="ENTER_PASSWORD", 
  host="localhost", 
  database="ENTER_DB_NAME") 
cur = conn.cursor() 

#retrieving information from command input: 

some_name = input ("""Options are: 
        GROUP1_NAME, GROUP2_NAME, GROUP3_NAME, GROUP4_NAME, GROUP5_NAME and GROUP5_NAME 
        Type group name here: """) 
cur.execute("SELECT Characteristic2, Characteristic3, Characteristic4 FROM Teams WHERE Charecteristic1=?", (some_name,))

for Characteristic2, Charecteristics3, Charecteristics4 in cur: 
  print(f"""Charecteristics2: {Characteristics2}, 
  
  Charecteristic3: {Charecteristics3}, 
  
  Charecteristic4: {Charecteristics4}""")
