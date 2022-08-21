import sys

LET = 26
UTL = 32

class Rot:

    def __init__(self, string: str):
        self.string = string

    def rot(self, value: int):

        if (value < 1 or value > 25):
            print("select [1-25]")
            return

        rotated = str()
        for char in self.string:
            
            cache = ord(char.upper())
            if cache >=65 and cache <=90:
                flag = UTL if char.islower() else 0;
                buffer = cache + value + flag
                buffer -= (LET if buffer > 122 else 0)
                rotated += chr(buffer)

            else: 
                rotated += char
         
        return rotated

    def rot47(self):

        ROT = 47
        RESET = ROT * 2
        rotated = str()

        for char in self.string:

            cache = ord(char)
            if cache >=33 and cache <=126:
                res = cache + ROT;   
                rotated += chr(res - RESET if res > 126 else res);

            else:
                 rotated += char
        return rotated

