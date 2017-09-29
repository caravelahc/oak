from music import Buzzer
from grieg import IN_THE_HALL_OF_THE_MOUNTAIN_KING_2
import oak

b = Buzzer(oak.PINS[5])
b.play_tune(IN_THE_HALL_OF_THE_MOUNTAIN_KING_2)
