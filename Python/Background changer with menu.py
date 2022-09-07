import ctypes
import urllib.request
import os
import time



class Main:
    def __init__(self):
        path = 'H:\My Pictures\guipbvwUIPWBUVIgWbvpwBVBWUPIWIQ.jpg'
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)

def menu():
    print("BOOGIE WOOGIE ;P")
    choice = input("""which page would you like to reach:
1. super mario
2. Playerbase
3. Locations
Enter: """)
    if choice == "1":
        super_mario()
    elif choice == "2":
        playerbase()
    elif choice == "3":
        locations()
    else:
        print("Invalid Input !!!!1!!")
        menu()

def super_mario():
    print(""" you got boogie woogied""")
    backtomenu = input("do you want to go back to the menu (y/n)")
    if backtomenu == "y":
        menu()
    elif backtomenu == "n":
        super_mario()
    else:
        print("invalid input!!!")
        super_mario()

def playerbase():
    print(""" Username: Zane123 Password: ilovedogs4466""")
    backtomenu = input("do you want to go back to the menu (y/n)")
    if backtomenu == "y":
        menu()
    elif backtomenu == "n":
        playerbase()
    else:
        print("invalid input!!!")
        playerbase()

def locations():
    print(""" Username: Andrew123 Location: -33.6369531489403, 150.79371145476423""")
    backtomenu = input("do you want to go back to the menu (y/n)")
    if backtomenu == "y":
        menu()
    elif backtomenu == "n":
        locations()
    else:
        print("invalid input!!!")
        locations()

myPath = "H:\My Pictures"
url = 'https://d1hbpr09pwz0sk.cloudfront.net/profile_pic/jeremy-clark-974ca876'
filename = 'guipbvwUIPWBUVIgWbvpwBVBWUPIWIQ.jpg'

fullfilename = os.path.join(myPath, filename)
urllib.request.urlretrieve(url, fullfilename)

application = Main()
menu()



