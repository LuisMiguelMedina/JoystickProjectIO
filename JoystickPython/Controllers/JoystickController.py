import serial, warnings, serial.tools.list_ports
import pyautogui as pg  
from pynput.keyboard import Controller

keyboard = Controller()
pg.FAILSAFE=False

ports = serial.tools.list_ports.comports(include_links=False)
for port in ports :
    print(port.device)
portVar = port.device
serialInst = serial.Serial()
serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()
# FirstJoystick (Mouse)
while True:
    read = serialInst.readline().decode('ascii')
    readArray = read.split()
    c = readArray[0]
    x = readArray[1]
    y = readArray[2]
    x2 = readArray[3]
    y2 = readArray[4]
    h = readArray[5]
    i = readArray[6]
    j = readArray[7]
    k = readArray[8]
    m = readArray[9]
    print(c, ' ', x,' ',y,' ',m,' ', h,' ',i,' ',j,' ',k)
    if c=='c':
        pg.click(button='left')
    if  h == '1':
        keyboard.press('a')
        keyboard.release('a')
    if  i == '2':
        keyboard.press('w')
        keyboard.release('w')
    if  j == '3':
        keyboard.press('d')
        keyboard.release('d')
    if  k == '4':
        keyboard.press('s')
        keyboard.release('s')

    pg.moveTo(int(x), int(y))