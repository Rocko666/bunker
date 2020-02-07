#----------Pico y Placa System----------
#Code by Cristian Ortiz
#Made in Visual Studio Code
#Python programming languaje
#Necesary libraries
from datetime import datetime
import calendar
import time
from sys import exit
#Informattion that must to be shown for the user
print("Welcome to Quito's Pico y Placa system")
print("This program will allow you to know if you can drive along in Quito in an specific hour")
print("We need some information to continue:")
#Information given by the user
#Input date in an specific format
date_input= input('Please type the date in YMD format(i.e. 2017,7,1): ')
#To separate year, ,month and day form the variable date_input
year, month, day = map(int, date_input.split(','))
#Input time in an specific format
time_input= input('"Please type the time in 24hr format (i.e. 18:05:12): ')
#To separate hour, minute and second form the variable time_input
hour, minute, second = map(int, time_input.split(':'))
date = datetime(year, month, day,hour, minute, second)
#To show the information entered
print("YYYY/MM/DD HH:MM:SS")
print (date)
#Is important to show the weekday because Pico y Placa uses it to restrict the traffic
print("Today is",date.strftime("%A"))
#To assign the weekday to an int: 0 to monday, 1 to tuesday...etc
nameday=calendar.weekday(year, month, day)
#To stablish a comparison between the day and the licence plate number and remember to the user pico y placa's schedule
#On Saturday and Sunday(5 and 6) pico y placa doesn't works
if (nameday!=5) and (nameday!=6):
    #For Monday
    if nameday== 0:
     print("Remember that only cars with licence plate last digit ending in 1 & 2 can't drive")
     print("from 7:00am - 9:30am and 16:00pm - 19:30")
    #For Tuesday
    if nameday== 1:
     print("Remember that only cars with licence plate last digit ending in 3 & 4 can't drive")
     print("from 7:00am - 9:30am and 16:00pm - 19:30")
    #For Wednesday
    if nameday== 2:
     print("Remember that only cars with licence plate last digit ending in 5 & 6 can't drive")
     print("from 7:00am - 9:30am and 16:00pm - 19:30")
   #For Thursday
    if nameday== 3:
     print("Remember that only cars with licence plate last digit ending in 7 & 8 can't drive")
     print("from 7:00am - 9:30am and 16:00pm - 19:30")
    #For Friday
    if nameday== 4:
     print("Remember that only cars with licence plate last digit ending in 9 & 0 can't drive")
     print("from 7:00am - 9:30am and 16:00pm - 19:30")
#For Saturday and Sunday the program finishes because hour and licence plate number don't matter
else:
    print("All cars can drive all day long, It isn't necessary to enter you licence plate, thanks for use this program")
    exit(0)
#lp is a variable for licence plate number
lp = input("Please type full Licence plate (i.e. PBT1234) ")
#To show to the user the licence plate number entered
print (lp)
#To determine lenght of variable lp
lenght=len(lp)
#To get last digit from lp variable as an int value
last=int (lp[lenght-1])
print("Your licence plate last digit is:",last)
#To determine a comparison between the day and the last digit from licence plate number
#For Monday and licences plate number 1 and 2
if (last==1 or last==2) and nameday==0:
    if 7<=hour<=8 or 16<=hour<=18:
        print("Sorry, You can't drive along Quito, thanks for use this program")
    elif hour==9 or hour==19:
        if minute<=29:
         print("Sorry, You can't drive along Quito, thanks for use this program")
        else:
         print("It's ok, You can drive along Quito, thanks for use this program")
    else: 
        print("It's ok, You can drive along Quito, thanks for use this program")

#For Tuesday and licences plate number 3 and 4
elif (last==3 or last==4) and nameday==1:
    if 7<=hour<=8 or 16<=hour<=18:
        print("Sorry, You can't drive along Quito, thanks for use this program")
    elif hour==9 or hour==19:
        if minute<=29:
         print("Sorry, You can't drive along Quito, thanks for use this program")
        else:
         print("It's ok, You can drive along Quito, thanks for use this program")
    else: 
        print("It's ok, You can drive along Quito, thanks for use this program")
#For Wednesday and licences plate number 5 and 6
elif (last==5 or last==6) and nameday==2:
    if 7<=hour<=8 or 16<=hour<=18:
        print("Sorry, You can't drive along Quito, thanks for use this program")
    elif hour==9 or hour==19:
        if minute<=29:
         print("Sorry, You can't drive along Quito, thanks for use this program")
        else:
         print("It's ok, You can drive along Quito, thanks for use this program")
    else: 
        print("It's ok, You can drive along Quito, thanks for use this program")

#For Thursday and licences plate number 7 and 8
elif (last==7 or last==8) and nameday==3:
    if 7<=hour<=8 or 16<=hour<=18:
        print("Sorry, You can't drive along Quito, thanks for use this program")
    elif hour==9 or hour==19:
        if minute<=29:
         print("Sorry, You can't drive along Quito, thanks for use this program")
        else:
         print("It's ok, You can drive along Quito, thanks for use this program")
    else: 
        print("It's ok, You can drive along Quito, thanks for use this program")

#For Friday and licences plate number 9 and 0
elif (last==9 or last==0) and nameday==4:
    if 7<=hour<=8 or 16<=hour<=18:
        print("Sorry, You can't drive along Quito, thanks for use this program")
    elif hour==9 or hour==19:
        if minute<=29:
         print("Sorry, You can't drive along Quito, thanks for use this program")
        else:
         print("It's ok, You can drive along Quito, thanks for use this program")
    else: 
        print("It's ok, You can drive along Quito, thanks for use this program")
#For all other cases
else:
 print("It's ok, You can drive along Quito, thanks for use this program")
