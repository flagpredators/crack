
import sys

LET = 26
UTL = 32

class Vignere():

    def __init__(self, cred: str, key: str) -> None:
        self.cred = cred
        self.key = key

    def keygen(self) -> str:

        j = 0

        key = str()
        gen_key = str()

        for char in self.key:

            if char.isdigit():
                raise f"CharError: character {char} not in list, expected: [a-zA-Z]"

            if(char.isalpha()):
                key += char

        for char in self.cred:

            if(j >= len(key)):
                j = 0;

            if char.isalpha() == False:
                gen_key += char
            else: 
                gen_key += list(key)[j]
                j += 1
            
        return gen_key;
    
    def encrypt(self, genkey: str) -> str:

        ciphertext = str()
        for idx, char in enumerate(self.cred):

            cache = ord(char.upper())
            if cache >=65 and cache <=90:
                flag = UTL if char.islower() else 0;
                buffer = cache - (65 - ord(list(genkey)[idx].upper())) + flag;
                buffer -= (LET if buffer > 122 else 0)
                ciphertext += chr(buffer)
            else:
                ciphertext += char
        
        return ciphertext

    def decrypt(self, genkey: str) -> str:

        ciphertext = str()
        for idx, char in enumerate(self.cred):

            cache = ord(char.upper())
            if cache >=65 and cache <=90:
                flag = UTL if char.islower() else 0;
                buffer = cache - (ord(list(genkey)[idx].upper()) - 65) ;
                buffer += (LET if buffer < 65 else 0)
                ciphertext += chr(buffer+ flag)
            else:
                ciphertext += char
        
        return ciphertext

# instance = Vignere(sys.argv[1], sys.argv[2])
# key = instance.keygen()
# print(key)
# print(instance.decrypt(key))