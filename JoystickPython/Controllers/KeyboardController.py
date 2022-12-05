import serial, pydirectinput 
from pynput.keyboard import Key, Controller

keyboard = Controller()

ser = serial.Serial("COM4",'9600')  #Enter Arduino Port Number
# 0 to 10,024. 512 is neutral
while True:
    if(ser.inWaiting()>0):
        data = ser.read()
        if data == b"1":
            keyboard.press('w')
            keyboard.release('w')
        if data == b"2":
            keyboard.press('s')
            keyboard.release('s')
        if data == b"3":
            keyboard.press('d')
            keyboard.release('d')
        if data == b"4":
            keyboard.press('a')
            keyboard.release('a')
        if data == b"5":
            pydirectinput.click(button='right')