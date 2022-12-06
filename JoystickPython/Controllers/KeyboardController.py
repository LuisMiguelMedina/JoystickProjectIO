import serial, pydirectinput 
from pynput.keyboard import Key, Controller

from JoystickPython import interfaz

letras = interfaz.manda_arreglo

keyboard = Controller()

ser = serial.Serial("COM4",'9600')  #Enter Arduino Port Number
# 0 to 10,024. 512 is neutral
while True:
    if(ser.inWaiting()>0):
        data = ser.read()
        if data == b"1":
            keyboard.press(letras[0])
            keyboard.release(letras[0])
        if data == b"2":
            keyboard.press(letras[1])
            keyboard.release(letras[1])
        if data == b"3":
            keyboard.press(letras[2])
            keyboard.release(letras[2])
        if data == b"4":
            keyboard.press(letras[3])
            keyboard.release(letras[3])
        if data == b"5":
            pydirectinput.click(button='right')