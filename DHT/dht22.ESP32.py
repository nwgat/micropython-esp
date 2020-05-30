# nwgat.ninja
# DHT22 / AOSONG AM2302
# pin 1 > 21(SDA)
# pin 2 > 3.3v
# pin 4 > GND

import dht, machine

d = dht.DHT22(machine.Pin(21))
dm = d.measure()
dt = d.temperature()
dh = d.humidity()

print ((dm))
print ((dt))
print ((dh))