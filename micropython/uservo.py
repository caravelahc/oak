from machine import Pin, PWM


class Servo:
    def __init__(self, pin):
        self.servo = PWM(Pin(pin), freq=50, duty=40)
        self._angle = 0

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, angle):
        if not 0 <= angle <= 180:
            raise ValueError('Angle must be a value between 0 and 180')
        self._angle = angle
        value = self._convert_to_value(angle)
        self.servo.duty(value)

    def _convert_to_value(self, angle):
        # servo can be controlled with duty from 40 to 115
        # but while testing, 115 made him noisy
        value = int(angle*73/180 + 40)
        return value
