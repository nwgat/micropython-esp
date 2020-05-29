# nwgat.ninja
import machine, ssd1306, urequests, network, time

wlan = network.WLAN(network.STA_IF)
i2c = machine.I2C(-1, machine.Pin(5), machine.Pin(4))
oled = ssd1306.SSD1306_I2C(64, 48, i2c)
    
while True:
    status = urequests.get("https://raw.githubusercontent.com/nwgat/mailboxninja/master/status")
    rssi = wlan.status("rssi")
    time.sleep(1)
    oled.fill(0)
    oled.text((status.content).rstrip(), 1, 10)
    oled.text(str(rssi), 1, 20,) 
    oled.show()
