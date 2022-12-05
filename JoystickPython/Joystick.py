import serial            #Install Modules
import pyautogui as pg   #Install Modules


pg.FAILSAFE=False

ser = serial.Serial("COM3",'9600')  #Enter Arduino Port Number
while True:
    read = ser.readline().decode('ascii')
    readArray = read.split()
    c = readArray[0]
    x = readArray[1]
    y = readArray[2]
    m = readArray[3]
    print(c, ' ', x,' ',y,' ',m)
    if c=='c':
        pg.click(button='left')

    pg.moveTo(int(x), int(y))