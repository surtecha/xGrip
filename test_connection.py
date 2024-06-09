from pyfirmata import Arduino, util
import time

board = Arduino('/dev/cu.usbmodem21301')    # Change the port to the one you are using

print(board.get_firmata_version())

blinkCount = input("Blink count: ")

for i in range(int(blinkCount)):
    print("Blink counter: " + str(i+1))
    board.digital[13].write(1)
    time.sleep(0.5)
    board.digital[13].write(0)
    time.sleep(0.5)
