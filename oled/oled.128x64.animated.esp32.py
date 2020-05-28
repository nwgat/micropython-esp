# nwgat.ninja

from machine import I2C, Pin
import ssd1306, framebuf, time

i2c = I2C(-1, Pin(22), Pin(21))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

images = []
for n in range(1,7):
    with open('seq/seq0000%s.pbm' % n, 'rb') as f:
        f.readline() # Magic number
        f.readline() # Dimensions
        data = bytearray(f.read())
    fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)
    images.append(fbuf)

display.invert(1)
while True:
    for i in images:
        display.blit(i, 0, 0)
        display.show()
        time.sleep(0.1)
