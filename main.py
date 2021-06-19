


import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import version

import sqlite3

con = sqlite3.connect('games.db')
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE Users
               (name text, rank int)''')


from typing import Optional


print ('gui?')
def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False

if True:

  user1 = input ('Enter your name: ')
  print ('welcome',user1)
  ans=True
  while ans:
    print ("""
    1.Add a Entry
    2.Delete an Entry
    3.Find Entry
    4.Save changes and exit
    5.Save changes and continue
    6.Version and authers info
    """)
    ans=input("What would you like to do? ") 
    if ans=="1":
      entry = input ('Entry Number? ') 
      addtosql = input ('Entry?')
      print("\n Entry Added") 
    elif ans=="2":
      print("\n Entry Deleted") 
    elif ans=="3":
      entryinfo=input ('entry number?: ')
      print("\n Entry Record Found") 


    elif ans=="4":
      print("\n Saving Changes") 
      print ("Goodbye")
      exit()
    elif ans=="5":
      print("\n Saving changes") 
      
    elif ans=="6":
      print("\n Version: 0.2") 
      print ("Made possible by Spectrum Gaming community")
      print ("Head coder: Harry Hayward-Evans")
      print ("Coding team: Insert names here")
      print ("Bug checker: Harry and Insert name here")
    elif ans=="2009":
      print ('admin mode selected please choose option')
      ans=True
      while ans:
        print ("""
        1. Danger Zone
        2. Delete a user
        3. add a user
        4. open sqlite file
        5. debug mode
        6. go back
        
        """)
        ans=input("What would you like to do? ") 
        if ans=="1":
            print ("!Danger zone!")
        elif ans=="2":
            print ('delete user selected')

        elif ans=="3":
            print ('add user selected')


        elif ans=="4":
            print ('opening SQLite files')


            


    elif ans !="":
      print("\n Not Valid Choice Try again")
