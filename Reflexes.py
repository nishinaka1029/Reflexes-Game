import serial
import time
import random

_ser0 = serial.Serial('/dev/ttyUSB0', 115200, timeout=10)
_ser1 = serial.Serial('/dev/ttyUSB1', 115200, timeout=10)
_ser2 = serial.Serial('/dev/ttyUSB2', 115200, timeout=10)

USB0 = 'Hideyoshi'
USB1 = 'Konosuke'
USB2 = 'Ryu'

nyokkiedNum = 0
nyokkiedList = {USB0: False, USB1: False, USB2: False}

time.sleep(3)
start_signal = input('Push "ENTER" to Start')
start_time = time.time()

random_num = random.randrange(0, 10, 1)

time.sleep(1)

print("Takenoko Nyokki")

time.sleep(random_num)
    
print('Nyokkikki !!')

def judge_nyokki(data_str, USB):
    acc_x,acc_y,acc_z=map(float,data_str.split(','))
    if abs(acc_x) > 1.00 or abs(acc_y) > 1.00:
        nyokki_time = time.time()
        result = nyokki_time - start_time - random_num - 1
        if(result <= 0.20):
            print(f'{USB} is Cheater!')
        else :
            global nyokkiedNum
            nyokkiedNum += 1
            print(f"{nyokkiedNum} Nyokki: {USB} time:{result}")
        global nyokkiedList
        nyokkiedList[USB] = True

while not nyokkiedList[USB0] or not nyokkiedList[USB1] or not nyokkiedList[USB2]:
    
    if nyokkiedList[USB0] == False:
        data0 = _ser0.readline()
        data_str0=data0.decode().strip()
        try:
            judge_nyokki(data_str0, USB0)
        except ValueError:
            continue
            
    if nyokkiedList[USB1] == False:
        data1 = _ser1.readline()
        data_str1=data1.decode().strip()
        try: 
            judge_nyokki(data_str1, USB1)
        except ValueError:
            continue
            
    if nyokkiedList[USB2] == False:
        data2 = _ser2.readline()
        data_str2=data2.decode().strip()
        try: 
            judge_nyokki(data_str2, USB2)
        except ValueError:
            continue
