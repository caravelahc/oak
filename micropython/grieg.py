from music import Note, Pitch
from music import Buzzer, BuzzerBand
import oak


def main():
    b1 = Buzzer(oak.PINS[5])
    b2 = Buzzer(oak.PINS[6])

    band = BuzzerBand(b1, b2)
    band.play_tunes(IN_THE_HALL_OF_THE_MOUNTAIN_KING_1,
                    IN_THE_HALL_OF_THE_MOUNTAIN_KING_2, speed=2)


IN_THE_HALL_OF_THE_MOUNTAIN_KING_1 = (
    Note(Pitch.E[3], 10, 4, 0),

    Note(Pitch.A[2], 10, 0.5, 1), Note(Pitch.B[2], 10, 0.5, 1),
    Note(Pitch.C[3], 10, 0.5, 1), Note(Pitch.D[3], 10, 0.5, 1),
    Note(Pitch.E[3], 20, 0.5, 1), Note(Pitch.C[3], 10, 0.5, 1),
    Note(Pitch.E[3], 10, 1, 1),

    Note(Pitch.Eb[3], 20, 0.5, 1), Note(Pitch.B[2], 10, 0.5, 1),
    Note(Pitch.Eb[3], 10, 1, 1),
    Note(Pitch.D[3], 20, 0.5, 1), Note(Pitch.Bb[3], 10, 0.5, 1),
    Note(Pitch.D[3], 10, 1, 1),

    Note(Pitch.A[2], 10, 0.5, 1), Note(Pitch.B[2], 10, 0.5, 1),
    Note(Pitch.C[3], 10, 0.5, 1), Note(Pitch.D[3], 10, 0.5, 1),
    Note(Pitch.E[3], 20, 0.5, 1), Note(Pitch.C[3], 10, 0.5, 1),
    Note(Pitch.E[3], 10, 0.5, 1), Note(Pitch.A[3], 10, 0.5, 1),

    Note(Pitch.G[3], 20, 0.5, 1), Note(Pitch.E[3], 10, 0.5, 1),
    Note(Pitch.C[3], 10, 0.5, 1), Note(Pitch.E[3], 10, 0.5, 1),
    Note(Pitch.G[3], 20, 2, 0),

    Note(Pitch.A[2], 10, 0.5, 1), Note(Pitch.B[2], 10, 0.5, 1),
    Note(Pitch.C[3], 10, 0.5, 1), Note(Pitch.D[3], 10, 0.5, 1),
    Note(Pitch.E[3], 20, 0.5, 1), Note(Pitch.C[3], 10, 0.5, 1),
    Note(Pitch.E[3], 10, 1, 1),

    Note(Pitch.Eb[3], 20, 0.5, 1), Note(Pitch.B[2], 10, 0.5, 1),
    Note(Pitch.Eb[3], 10, 1, 1),
    Note(Pitch.D[3], 20, 0.5, 1), Note(Pitch.Bb[3], 10, 0.5, 1),
    Note(Pitch.D[3], 10, 1, 1),

    Note(Pitch.A[2], 10, 0.5, 1), Note(Pitch.B[2], 10, 0.5, 1),
    Note(Pitch.C[3], 10, 0.5, 1), Note(Pitch.D[3], 10, 0.5, 1),
    Note(Pitch.E[3], 20, 0.5, 1), Note(Pitch.C[3], 10, 0.5, 1),
    Note(Pitch.E[3], 10, 0.5, 1), Note(Pitch.A[3], 10, 0.5, 1),

    Note(Pitch.G[3], 20, 0.5, 1), Note(Pitch.E[3], 10, 0.5, 1),
    Note(Pitch.C[3], 20, 0.5, 1), Note(Pitch.E[3], 10, 0.5, 1),
    Note(Pitch.G[3], 20, 2, 0),

)

IN_THE_HALL_OF_THE_MOUNTAIN_KING_2 = (
    Note(Pitch.E[2], 5, 4, 0),

    Note(Pitch.A[0], 10, 1, 1), Note(Pitch.E[1], 10, 1, 1),
    Note(Pitch.A[0], 10, 1, 1), Note(Pitch.E[1], 10, 1, 1),

    Note(Pitch.A[0], 10, 1, 1), Note(Pitch.E[1], 10, 1, 1),
    Note(Pitch.A[0], 10, 1, 1), Note(Pitch.E[1], 10, 1, 1),

    Note(Pitch.A[0], 10, 1, 1), Note(Pitch.E[1], 10, 1, 1),
    Note(Pitch.A[0], 10, 1, 1), Note(Pitch.E[1], 10, 1, 1),

    Note(Pitch.C[1], 10, 1, 1), Note(Pitch.G[1], 10, 1, 1),
    Note(Pitch.C[1], 10, 1, 1), Note(Pitch.G[1], 10, 1, 1),

    Note(Pitch.A[0], 10, 1, 1), Note(Pitch.E[1], 10, 1, 1),
    Note(Pitch.A[0], 10, 1, 1), Note(Pitch.E[1], 10, 1, 1),

    Note(Pitch.A[0], 10, 1, 1), Note(Pitch.E[1], 10, 1, 1),
    Note(Pitch.A[0], 10, 1, 1), Note(Pitch.E[1], 10, 1, 1),

    Note(Pitch.A[0], 10, 1, 1), Note(Pitch.E[1], 10, 1, 1),
    Note(Pitch.A[0], 10, 1, 1), Note(Pitch.E[1], 10, 1, 1),

    Note(Pitch.C[1], 10, 1, 1), Note(Pitch.G[1], 10, 1, 1),
    Note(Pitch.C[1], 10, 1, 1), Note(Pitch.G[1], 10, 1, 1),

    Note(Pitch.E[1], 10, 1, 1), Note(Pitch.B[1], 10, 1, 1),
    Note(Pitch.E[1], 10, 1, 1), Note(Pitch.B[1], 10, 1, 1),

    Note(Pitch.C[1], 10, 1, 1), Note(Pitch.Ab[1], 10, 1, 1),
    Note(Pitch.E[1], 10, 1, 1), Note(Pitch.B[1], 10, 1, 1),

    Note(Pitch.E[1], 10, 1, 1), Note(Pitch.B[1], 10, 1, 1),
    Note(Pitch.E[1], 10, 1, 1), Note(Pitch.B[1], 10, 1, 1),

    Note(Pitch.C[1], 10, 1, 1), Note(Pitch.Ab[1], 10, 1, 1),
    Note(Pitch.E[1], 10, 1, 1), Note(Pitch.B[1], 10, 1, 1),

    Note(Pitch.E[1], 10, 1, 1), Note(Pitch.B[1], 10, 1, 1),
    Note(Pitch.E[1], 10, 1, 1), Note(Pitch.B[1], 10, 1, 1),

    Note(Pitch.C[1], 10, 1, 1), Note(Pitch.Ab[1], 10, 1, 1),
    Note(Pitch.E[1], 10, 1, 1), Note(Pitch.B[1], 10, 1, 1),

    Note(Pitch.E[1], 10, 1, 1), Note(Pitch.B[1], 10, 1, 1),
    Note(Pitch.E[1], 10, 1, 1), Note(Pitch.B[1], 10, 1, 1),

)
