import uasyncio as asyncio
import machine
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

    async def _play_note_coro(self, note: Note, speed=1):
        try:
            duration = note.duration / speed
            if note.frequency is not None:
                self.frequency = note.frequency
            # self.duty = note.duty
            self.duty = 200

            if note.staccato:
                await asyncio.sleep(0.1)
            else:
                await asyncio.sleep(duration)
        finally:
            self.duty = 0
            if note.staccato:
                await asyncio.sleep(duration - 0.1)

    async def _play_tune_coro(self, notes, speed=1):
        try:
            for note in notes:
                await self._play_note_coro(note, speed=speed)
        finally:
            self.duty = 0

    def play_tune(self, notes, speed=1):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._play_tune_coro(notes, speed=speed))


class BuzzerBand:
    def __init__(self, *buzzers):
        self._buzzers = buzzers

    def play_tunes(self, *tunes, speed=1):
        loop = asyncio.get_event_loop()
        for buzzer, tune in zip(self._buzzers, tunes):
            loop.call_soon(buzzer._play_tune_coro(tune, speed=speed))

        loop.run_forever()
