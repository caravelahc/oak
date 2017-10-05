from ucollections import namedtuple
from machine import I2C, Pin
import oak


ColorRGB = namedtuple('Color', ('red', 'green', 'blue'))


class Display:
    def __init__(self):
        self._i2c = I2C(scl=Pin(oak.PINS[2]),
                        sda=Pin(oak.PINS[0]))

        self._set_register(0x00, 0)
        self._set_register(0x01, 0)
        self._set_register(0x08, 255)

        self._backlight_color = ColorRGB(0, 0, 0)

    def _set_register(self, addr, value):
        self._i2c.writeto_mem(0x62, addr, bytearray([]))
        self._i2c.writeto_mem(0x62, addr, bytearray([value]))

    @property
    def backlight_color(self):
        return self._backlight_color

    @backlight_color.setter
    def backlight_color(self, color):
        self._set_register(0x04, color[0])
        self._set_register(0x03, color[1])
        self._set_register(0x02, color[2])
        self._backlight_color = color
