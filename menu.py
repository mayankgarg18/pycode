#!/usr/bin/python2

import time #to get time
import uuid # to scan all Mac address in current Network
import os # to access operating system commands
import webbrowser #to access web browser

menu='''
Press 1 to check current time and date :
Press 2 to scan all your Mac address in your currnet connected Network :
Press 3 to Shutdown your machine after 15 minutes :
Press 4 to search something on google :
Press 5 to Logout your current Machine :
Press 6 to Shutdown all connected system in your current network :
Press 7 to update status on Facebook :
Press 8 to list ip address of given website :
'''


print menu 
choice=raw_input()


if choice == '1' :
       print "Current time and date is : ",time.ctime()

elif choice == '2' :
       print "Get Mac address...."
       time.sleep(2)
       print (hex(uuid.getnode()))

elif choice == '4':
       find=raw_input("What do you want to search :")
       webbrowser.open_new_tab("https://www.google.com/search?q="+find) # to search on google anything you want

      


else :
    print "Invalid Option"
