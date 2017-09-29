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
NoteEvent = namedtuple('NoteEvent', ('frequency', 'duty', 'time', 'buzzer_id'))


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
            self.frequency = note.frequency or 0
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


class BuzzerBand:
    def __init__(self, *buzzers):
        self._buzzers = buzzers

    def play_event(self, event: NoteEvent):
        print(event)
        buzzer = self._buzzers[event.buzzer_id]
        buzzer.frequency = event.frequency or 0
        buzzer.duty = event.duty

    def play_tunes(self, *tunes, speed=1):
        ensemble = []
        staccato_duration = 0.1 / speed
        for i, tune in enumerate(tunes):
            queue, t = [], 0
            for n in tune:
                queue.append(NoteEvent(n.frequency, n.duty, t, i))

                duration = n.duration / speed
                t += staccato_duration if n.staccato else duration
                queue.append(NoteEvent(None, 0, t, i))

                if n.staccato:
                    t += duration - staccato_duration

            ensemble += queue

        ensemble = sorted(ensemble, key=lambda n: n.time)

        try:
            for i, event in enumerate(ensemble):
                print(i, event)
                self.play_event(event)
                if i + 1 < len(ensemble):
                    sleep(ensemble[i+1].time - event.time)
        except:
            pass
        finally:
            for b in self._buzzers:
                b.duty = 0
