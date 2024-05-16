def get_boards():
    plugs = []
    while True:
        string = input("\nEnter the plugs with space between letters example: AG DS\n").strip()
        if string == "":
            break

        if check_valid(string) and are_pairs(string):
            plugs = string.upper().split(" ")
            break

    board_reflector = [x for x in range(26)]
    for item in plugs:
        i1 = ord(item[0]) - ord('A')
        i2 = ord(item[1]) - ord('A')
        board_reflector[i1] = i2
        board_reflector[i2] = i1

    return board_reflector

def are_pairs(string: str):
    for pair in string.split(" "):
        if len(pair) != 2:
            return False
    return True    

def check_valid(string: str):
    for c in string:
        if not c.isalpha() and not c.isspace():
            return False

    return True    