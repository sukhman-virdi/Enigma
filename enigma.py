from rotor import *
from settings import Settings

class Enigma:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def encrypt_word(self, letter):
        # Generating rotor data from settings
        rotors = []
        for i in range(3):
            w = self.settings.rotors_data["Selection"][i]
            n = self.settings.rotors_data["Notch_Position"][i]
            s = self.settings.rotors_data["Start_Position"][i]
            r = Rotor(n, w, s)

            rotors.append(r)

        rotor_handler = RotorHandler(rotors)
        
        # Change Signal once
        ans = self.change_signal(boards=self.settings.board, signal=letter)

        # change 7 times at rotors
        ans = rotor_handler.encode(ans)

        # Change signal again on plug board
        ans = self.change_signal(boards=self.settings.board, signal=ans)

        # returning the encrypted signal
        return ans

    # As boards are set up in the map
    def change_signal(self, boards, signal):
        return boards[signal]