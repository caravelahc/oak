import machine
from time import sleep
from ucollections import namedtuple


class Pitch:
    C = [65, 131, 262, 523]
    Db = [69, 139, 277, 554]
    D = [73, 147, 294, 587]
    Eb = [78, 156, 311, 622]
    E = [82, 165, 330, 659]
    F = [87, 175, 349, 698]
    Gb = [92, 185, 370, 740]
    G = [98, 196, 392, 784]
    Ab = [104, 208, 415, 831]
    A = [110, 220, 440, 880]
    Bb = [117, 233, 466, 932]
    B = [123, 247, 494, 988]


Note = namedtuple('Note', ('frequency', 'duty', 'duration', 'staccato'))


class Buzzer:
    def __init__(self, pin_number: int):
        pin = machine.Pin(pin_number, machine.Pin.OUT)
        self._pwm = machine.PWM(pin)

    @property
    def duty(self) -> int:
        return self._pwm.duty()

    @duty.setter
    def duty(self, value: int):
        self._pwm.duty(value)

    @property
    def frequency(self) -> int:
        return self._pwm.frequency()

    @frequency.setter
    def frequency(self, value: int):
        self._pwm.freq(value)

    def play_note(self, note: Note, speed=1):
        try:
            duration = note.duration / speed
            if note.frequency is not None:
                self.frequency = note.frequency
            self.duty = note.duty

            if note.staccato:
                sleep(0.1)
            else:
                sleep(duration)
        except:
            pass
        finally:
            self.duty = 0
            if note.staccato:
                sleep(duration - 0.1)

    def play_tune(self, notes, speed=1):
        try:
            for note in notes:
                self.play_note(note, speed=speed)
        except:
            pass
        finally:
            self.duty = 0
