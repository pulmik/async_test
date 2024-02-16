import time
import serial
import asyncio
from async_wrap import async_wrap, async_sleep

async def print_loop():
    print('Entering print_loop')
    i = 1
    while True:
        try:
            print(i)
            i += 1
            # await asyncio.sleep(1)
            await async_sleep(1)
        except KeyboardInterrupt:
            break
    print('Leaving print_loop')

@async_wrap
def _create_Serial(dev_port):
    return serial.Serial(dev_port, 57600, write_timeout=3, timeout=3)

async def createSerial(dev_port):
    try:
        ser = await _create_Serial(dev_port) #serial.Serial(dev_port, 57600, write_timeout=3, timeout=3)
        print(f'Serial port opened: {dev_port}')
        # time.sleep(3)
        await asyncio.sleep(0.3)
        print(f'continue')
        return ser
    except serial.SerialException as exc:
        print(f'Error on open serial port "{dev_port}": {exc}')
        return None

@async_wrap
def readFromSerial(ser):
    print(f'readline...')
    line = ser.readline()
    print(f'readed: {line}')

async def main():
    print('Entering main')
    ser = await createSerial('\\\\.\\COM3')
    print(f'ser: {type(ser)}')
    if ser != None:
        try:
            await readFromSerial(ser)
        finally:
            ser.close()
    print('Leaving main')

if __name__ == '__main__':
    ioloop = asyncio.get_event_loop()
    tasks = [ioloop.create_task(main()), ioloop.create_task(print_loop())]
    tasks_for_wait = asyncio.wait(tasks)
    ioloop.run_until_complete(tasks_for_wait)
    ioloop.close()    
    print('Done')