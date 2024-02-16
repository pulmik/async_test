import serial
import asyncio

async def createSerial(dev_port):
    try:
        ser = serial.Serial(dev_port, 57600, write_timeout=3, timeout=3)
        print(f'Serial port opened: {dev_port}')
        # time.sleep(3)
        await asyncio.sleep(3)
        print(f'continue')
        return ser
    except serial.SerialException as exc:
        print(f'Error on open serial port "{dev_port}": {exc}')
        return None

async def readFromSerial(ser):
    line = ser.readline()
    print(f'readed: {line}')

async def main():
    print('Entering main')
    ser = await createSerial('\\\\.\\COM11')
    if ser != None:
        try:
            await readFromSerial(ser)
        finally:
            ser.close()
    print('Leaving main')

async def print_loop():
    print('Entering print_loop')
    i = 1
    while True:
        try:
            print(i)
            i += 1
            await asyncio.sleep(1)
        except KeyboardInterrupt:
            break
    print('Leaving print_loop')

if __name__ == '__main__':
    ioloop = asyncio.get_event_loop()
    tasks = [ioloop.create_task(main()), ioloop.create_task(print_loop())]
    tasks_for_wait = asyncio.wait(tasks)
    ioloop.run_until_complete(tasks_for_wait)
    ioloop.close()    
    print('Done')