import time

from ina260.controller import Controller

c = Controller(address=0x45)

while True:
    now = time.localtime()
    volt = "Voltage : %02.2f V , Current : %02.3fA, Power : %2.3fW" %(c.voltage(),c.current(),c.power())
    #print("Time : %02d:%02d:%02d" %(now.tm_hour,now.tm_min,now.tm_sec))
    print(volt)
    time.sleep(.2)



