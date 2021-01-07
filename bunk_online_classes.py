import time 
from datetime import datetime 
import pyautogui
from pynput.keyboard import Controller
from pynput.keyboard import Key
import webbrowser as wb

print("WELCOME_TO_BIT_MESRA_BUNK_CLASSES_TEAMS")
print("Created by SHIVAM KUMAR ECE K19 batch")

n = str(input("Enter the meeting link : "))  
a = str(input("Enter the meeting joining time (Use 24 hour format i.e HH:MM) : "))  
b = str(input("Enter the meeting leaving time (Use 24 hour format i.e HH:MM) : ")) 
lst=[
    [n,a,b]
#input lecture stats in form of list ......
# ["Link","start_time","end_time"]
# give time in 24 hrs format...
]
keyboard= Controller()

is_class_started =False
for lecture  in lst:
    while True :
        if is_class_started==False:
            if (datetime.now().hour == int(lecture[1].split(':')[0])and 
                datetime.now().minute == int(lecture[1].split(':')[1])):
                wb.open(lecture[0])
                is_class_started=True
                time.sleep(20)
                pyautogui.press('right')
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(5)
                pyautogui.hotkey('ctrl','shift','m')
                time.sleep(10)
        elif   (datetime.now().hour == int(lecture[2].split(':')[0]) and
                datetime.now().minute == int(lecture[2].split(':')[1])):
                is_class_started=False
                pyautogui.hotkey('ctrl','shift','b')
                time.sleep(3)
                pyautogui.hotkey('alt','f4')
                time.sleep(3)
                pyautogui.hotkey('alt','f4')
                #time.sleep(3)
                #pyautogui.hotkey('alt','f4')
                break
