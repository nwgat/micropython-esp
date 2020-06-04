# file: ir_receiver_demo-1.py
# https://medium.com/@rawat.s/micropython-programming-for-esp32-14-3474eeccdddd
from machine import Pin
import utime as time
from ir_receiver import IR_RECV
ir = IR_RECV( Pin(12), timeout=80 )
try:
    while True:
        codes = ir.read()
        for code in codes:
            print("Code: '{}'".format(code) )
        time.sleep_ms(300) 
except KeyboardInterrupt:
    pass
finally:
    ir.deinit()
    print('Done')