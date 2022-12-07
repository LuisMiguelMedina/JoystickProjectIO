import serial, warnings, serial.tools.list_ports
import pyautogui as pg  
from pynput.keyboard import Controller

def keyboard_controller(keys):
    keyboard = Controller()
    pg.FAILSAFE=False
    # COM port Detector
    try:
        ports = serial.tools.list_ports.comports(include_links=False)
        for port in ports :
            print(port.device)
        portVar = port.device
        serialInst = serial.Serial()
        serialInst.baudrate = 9600
        serialInst.port = portVar
        serialInst.open()
    except:
        ports = serial.tools.list_ports.comports()
        serialInst = serial.Serial()

        portsList = []

        for onePort in ports:
            portsList.append(str(onePort))
            print(str(onePort))

        val = input("Select Port: COM")

        for x in range(0,len(portsList)):
            if portsList[x].startswith("COM" + str(val)):
                portVar = "COM" + str(val)
                print(portVar)
        serialInst.baudrate = 9600
        serialInst.port = portVar
        serialInst.open()

    # JoystickReading
    while True:
        # Serial input arrangement
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
        
        # Visual data
        print(c, ' ', x,' ',y,' ',m,' ', h,' ',i,' ',j,' ',k)
        
        # Keyboard & Mouse reading
        if c=='c':
            pg.click(button='left')
        if  h == '1':
            keyboard.press(key[0])
            keyboard.release(key[0])
        if  i == '2':
            keyboard.press(key[1])
            keyboard.release(key[1])
        if  j == '3':
            keyboard.press(key[2])
            keyboard.release(key[2])
        if  k == '4':
            keyboard.press(key[3])
            keyboard.release(key[3])
        pg.moveTo(int(x), int(y))