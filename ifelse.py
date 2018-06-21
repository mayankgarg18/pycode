#!usr/bin/python

import commands,time

option='''
press 1 to check the internet cable on your machine 
press 2 to check internet access
press 3 to check for google access 
press 4 to check  WIFI is connected or NOT
'''

print option

choice=raw_input()


if choice == '1':
   
         print "plz wait internet cable is being checked by current os..."
         time.sleep(3)
         cable_check=commands.getoutput('mii-tool eno1')
         if 'link ok' in cable_check:
                  print "Lan cable is Connected"
         else :
              print "LAN cable is not Connected"
                

elif choice == '2':
        
        print "Checking internet connectivity in a while...."
        time.sleep(3)
	check_internet=commands.getoutput('ifconfig') 
        if 'global' in check_internet:
        
           print"internet is accessible "
        
        else :
       
           print"intenet in not accessible"

       
elif choice == '3':
  
       print "google web page is loading... "
       check_google=commands.getoutput('host www.google.com')
      
       if 'connection timed out' in check_google :
         print"Google is not accessible"

       else :
         print"Google is acessible "

elif choice == '4' :
     
      print "Checking wifi is connected or not..... "
      time.sleep(2)
      check_wifi=commands.getoutput('ifconfig')
      if 'wlp19s0' in check_wifi:
         
           print"Wifi is Connected"
       
      else :
     
         print"Wifi is not Connected"
 
else :
     print"I think you click wrong option"

