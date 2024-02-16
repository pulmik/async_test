import time
import serial

def createSerial(dev_port):
    try:
        ser = serial.Serial(dev_port, 57600, write_timeout=3, timeout=3)
        time.sleep(3)
        print(f'Serial port opened: {dev_port}')
        return ser
    except serial.SerialException as exc:
        print(f'Error on open serial port "{dev_port}": {exc}')
        return None

def readFromSerial(ser):
    line = ser.readline()
    print(f'readed: {line}')

if __name__ == '__main__':
    ser = createSerial('\\\\.\\COM11')
    if ser != None:
        try:
            readFromSerial(ser)
        finally:
            ser.close()
    print('Done')