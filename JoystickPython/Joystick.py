import serial, time
serialInst = serial.Serial('COM3', 9600)
time.sleep(2)
String = serialInst.readline()
print(String)

serialInst.close()