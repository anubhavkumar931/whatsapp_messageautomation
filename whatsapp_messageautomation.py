import pyautogui as py
import webbrowser as wb
import time
from datetime import datetime
import pywhatkit

#this will print the current time so the the user can have a good idea of time

now = datetime.now()
current_time = now.strftime("%H:%M:%S")


#asking user for the required inputs

print("Hello i am WHAT BOT , i can send custom whatsapp messages to any number \n .....................................................................\n ")
a = int(input("If you want to proceed input 1 and if you dont want to move forward input 2  :  "))

if a == 1 :
    Message = input("Please Enter the message that you want to send ")
    Number = input("Please enter the number to which the message has to be sent : \n ")
    # repeat_mssg=input("enter the message that u want to be sent repeatedly ")
    repeat_times = int(input("enter the number of times you want the message to be sent"))
    print("Current Time =", current_time)
    mssg_time = input("Enter the time of sending message in  HH:MM format :\n")
    mssg_hour = int(mssg_time[0:2])
    mssg_min = int(mssg_time[3:5])

    # calling the sendwhatmssg function which opens whatsapp and sends mssg..to reach our destination
    pywhatkit.sendwhatmsg(Number, Message, mssg_hour, mssg_min, 15)

    # now press function from pyautogui library will get the right atmosphere and will do its job of typing and sending

    time.sleep(4)

    x = 0
    mssg_char = None
    i = 0
    y = 0
    while i < repeat_times - 1:
        i += 1
        x = 0
        if y != 0:
            py.press("enter")
        py.typewrite(Message)

        y += 1
    py.press("enter")

elif a == 2 :
    print("\nSAY NO MORE ......BYE ")
    exit()
else :
    print("\nThe number you just entered does not match to the requested input .....SO BYE ")
    exit()




