#!/usr/bin/python3
from concurrent.futures import ThreadPoolExecutor
import serial 
import time

execute = ThreadPoolExecutor()
serialport=serial.Serial("COM7",115200,timeout=0.1)
def mouthLoop(serialPort):
    while True:
        try:
            serialport.write("#5P1100T999D600".encode("utf-8"))
            while True:
                print("Entered mouth close")
                str=serialport.readall().decode("utf-8")
                
                break
            print("instruction execution successful for:")
            # print(instruction)
        except Exception as e:
            print(e)
        time.sleep(2)
        try:
            serialport.write("#5P1345T999D600".encode("utf-8"))
            while True:
                print("Entered mouth open")
                str=serialport.readall().decode("utf-8")
                
                break
            print("instruction execution successful for:")
            # print(instruction)
        except Exception as e:
            print(e)
        time.sleep(4)

def write_instruction(serialport,instruction):
    print("try")
    try:
        serialport.write(instruction.encode("utf-8"))
        print("2")
        while True:
            print("loop")
            str=serialport.readall().decode("utf-8")
            
            break
        print("instruction execution successful for:")
        print(instruction)
    except Exception as e:
        print(e)

def start_task():
    try:

        
        print('start')
        #Execution of preset instructions
        write_instruction(serialport,"#1P1570#2P1500#3P1500#4P1500#20P1500#21P1500#22P1500#23P1500#24P1500#25P1500T1000D800\r\n")
        
        time.sleep(2)
        print("Moh")
        write_instruction(serialport,"#1P1768#2P1345#3P2049#4P1768#21P1570#22P1711#23P1627#24P1824#25P2021T1000D800\r\n")
        time.sleep(4)
        write_instruction(serialport,"#1P1570#2P1500#3P1500#4P1500#20P1500#21P1500#22P1500#23P1500#24P1500#25P1500T1000D800\r\n")
        time.sleep(4)
        # #Test for action groups,Group 1 run 3 times
        # write_instruction(serialport,"G1F3\r\n")

        # serialport.close()

    except Exception as e:
        print("error",e)

def run():
    future3 = execute.submit(start_task)
    future = execute.submit(mouthLoop(serialport))
    
    return future, future3

run()
