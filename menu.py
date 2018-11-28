#!usr/bin/python3

#This is the menu for bash-script 
import time 
import subprocess
Text="Welcome to KOMOS-SCRIPT-MENU\n"
# Print Into 
Intro = """
   _  ______   _____ __  __  ____   _____                                  
 | |/ / __ \ / ____|  \/  |/ __ \ / ____|                                 
 | ' / |  | | (___ | \  / | |  | | (___                                   
 |  <| |  | |\___ \| |\/| | |  | |\___ \                                  
 | . \ |__| |____) | |  | | |__| |____) |                                 
 |_|\_\____/|_____/|_| _|_|\____/|_____/__     __  __ ______ _   _ _    _ 
  / ____|/ ____|  __ \|_   _|  __ \__   __|   |  \/  |  ____| \ | | |  | |
 | (___ | |    | |__) | | | | |__) | | |______| \  / | |__  |  \| | |  | |
  \___ \| |    |  _  /  | | |  ___/  | |______| |\/| |  __| | . ` | |  | |
  ____) | |____| | \ \ _| |_| |      | |      | |  | | |____| |\  | |__| |
 |_____/ \_____|_|  \_\_____|_|      |_|      |_|  |_|______|_| \_|\____/ 
 By LyhourChhen
                                                                          
                                                                          
"""
print(Intro)
for i in Text:
    print(i,end="")
    time.sleep(0.1)
#MENU
menuList=["ClearUP","Kosmos-Softcut","Autoupdate"]
index = 1
for i in menuList:
    print(index,"=>", i)
    index +=1
    time.sleep(0.1)
option = int(input("Enter any option you want as number in row :"))
if option == 2 : 
    subprocess.call(['./kosmos-softcut.sh'])
if option == 1:
    print("This program are not unavailable at the moment :(")
if option == 3:
    print("This program are not unavailable at the moment :(")

