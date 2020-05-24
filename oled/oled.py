import machine
import ssd1306
i2c = machine.I2C(-1, machine.Pin(5), machine.Pin(4))
oled = ssd1306.SSD1306_I2C(64, 48, i2c)

#oled.fill(0); oled.text('Hei XD', 6, 2); oled.text('Ninja', 6, 24); oled.show()