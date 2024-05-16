# For authenticity I got this wiring data from the wikipedia page of tehe original Enigma machine
WIRINGS= [[2, 11, 21, 0, 22, 8, 24, 4, 6, 12, 19, 14, 9, 20, 3, 18, 17, 25, 10, 1, 16, 13, 23, 15, 5, 7],
    [11, 5, 23, 17, 10, 18, 19, 20, 4, 22, 13, 0, 7, 8, 15, 9, 12, 3, 16, 21, 6, 24, 25, 14, 1, 2],
    [12, 19, 7, 14, 25, 4, 11, 8, 5, 18, 21, 16, 17, 22, 0, 13, 1, 20, 24, 3, 6, 2, 10, 9, 15, 23]
    ]

REFLECTOR = [12, 17, 19, 7, 5, 4, 6, 3, 22, 14, 10, 25, 0, 21, 9, 18, 24, 1, 15, 2, 23, 13, 8, 20, 16, 11]

class Rotor:
    def __init__(self, notch_pos, wiring_num, start_pos) -> None:
        self.notch_pos = notch_pos
        self.wiring = WIRINGS[wiring_num]
        self.position = start_pos
    
    def rotate(self):
        self.position = (self.position + 1) % 26
    
class RotorHandler:
    def __init__(self, rotors, reflector=REFLECTOR) -> None:
        self._rotors = rotors   
        self._reflector = reflector
    
    def encode(self, index):
        self.rotate_rotors()
        for i in range(3):
            index = (index + self._rotors[i].position) % 26

        index = self._reflector[index]

        for j in range(2, -1, -1):
            index = (index - self._rotors[j].position) % 26

        return index

    def rotate_rotors(self):
        self._rotors[0].rotate()
        if self._rotors[0].position == self._rotors[0].notch_pos:
            self._rotors[1].rotate()
            if self._rotors[1].position == self._rotors[1].notch_pos:
                self._rotors[2].rotate()

