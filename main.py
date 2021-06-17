from typing import Optional


user1 = input ('Enter your name: ')
print ('welcome',user1)
ans=True
while ans:
    print ("""
    1.Add a Entry
    2.Delete an Entry
    3.Find Entry
    4.Exit/Quit
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
      z=entryinfo
      print (z)

    elif ans=="4":
      print("\n Goodbye") 
      quit
    elif ans !="":
      print("\n Not Valid Choice Try again")