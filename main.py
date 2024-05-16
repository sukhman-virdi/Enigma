import enigma
from settings import Settings

print("Hello! This is Enigma. A replicant of an encoding machine used by Germans. It is calculated that the total no. of possible settings in this machine is 159 Quintillion!!!")
print("Type in the settings and remember those if you want to decrypt the message.")

# The constructor automatically takes input from user
setting = Settings()

# Feed the settings to teh enigma machine
engine = enigma.Enigma(setting)

# Getting the input string
string = input("Enter the string: ")
encrypt = ""

for word in string.upper():
    if word == " ":
        encrypt += word
    else:    
        index = ord(word) - ord("A")
        int = engine.encrypt_word(index)
        encrypt += chr(int + ord('A'))

print(encrypt)    

