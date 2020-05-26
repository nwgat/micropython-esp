# nwgat.ninja

import machine, ssd1306
i2c = machine.I2C(-1, machine.Pin(5), machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0); oled.text('Go', 6, 2); oled.text('Ninja', 6, 24); oled.text('Go', 6, 30); oled.show()
