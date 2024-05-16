from plug_board import get_boards

class Settings:
    def __init__(self) -> None:
        self.board = get_boards()
        self.rotors_data = self.get_rotor_data()
    
    def get_rotor_data(self):
        rotor_data = {"Selection": [-1, -1, -1], 
                      "Notch_Position": [-1, -1, -1],
                        "Start_Position": [-1, -1, -1]}
        
        for i in range(3):
            rotor_data["Selection"][i] = valid_input(f"Select the {tell_pos(i)} rotor (0-2): ", 3)
            rotor_data["Notch_Position"][i] = valid_input(f"Enter the notch of {tell_pos(i)} rotor (0-25): ", 26)
            rotor_data["Start_Position"][i] = valid_input(f"Enter the starting location of {tell_pos(i)} rotor (0-25): ", 26)
            print() 

        return rotor_data    

def tell_pos(index):
    match index:
        case 0: return "left"
        case 1: return "centre"
        case 2: return "right"

def valid_input(prompt, r):
    while True:
        try:
            i = int(input(prompt))
        except ValueError:
            print("Not a Valid input. Try again")
            continue

        if i not in range(r):
            print("Not a Valid input. Try again")
            continue

        return i