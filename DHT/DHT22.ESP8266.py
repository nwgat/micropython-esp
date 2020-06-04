# nwgat.ninja
# DHT22 / AOSONG AM2302
# pin 1 > 3.3v
# pin 2 > (4) D2 (SDA)
# pin 4 > GND

import dht, machine, time

while True:

 d = dht.DHT22(machine.Pin(4))
 dm = d.measure()
 dt = d.temperature()
 dh = d.humidity()
 print (dt, dh)
 time.sleep(120)
