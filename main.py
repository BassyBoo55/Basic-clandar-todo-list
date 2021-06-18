


import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import version


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"C:\users\public\qlitedata")

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
    4.Exit/Quit
    5.Version and authers info
    """)
    ans=input("What would you like to do? ") 
    if ans=="1":
      entry = input ('entry= ') 
      print("\n Entry Added") 
    elif ans=="2":
      print("\n Entry Deleted") 
    elif ans=="3":
      entryinfo=input ('entry number?: ')
      print("\n Entry Record Found") 


    elif ans=="4":
      print("\n Goodbye") 
      quit
    elif ans=="5":
      print("\n Version: 0.2") 
      print ("Made possible by Spectrum Gaming community")
      print ("Head coder: Harry Hayward-Evans")
      print ("Coding team: Insert names here")
      print ("Bug checker: Harry and Insert name here")
    elif ans !="":
      print("\n Not Valid Choice Try again")