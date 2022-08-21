import sys

UTL = 32
DIFF = 65
MOD = 26

class Affine:

    def __init__(self, text: str, coefficient: int, shift: int):
        self.text = text
        self.coefficient = coefficient
        self.shift = shift

    def encrypt(self) -> str:

        ciphertext = str()
        for i in self.text:

            cache = ord(i.upper()); 
            if cache >= 65 and  cache <= 90:
                probe = UTL if i.islower() else 0;
                ciphertext += chr(((((cache - DIFF) * self.coefficient) 
                            + self.shift) % MOD) + DIFF + probe);
            else: 
                ciphertext += i;
        

        return ciphertext; 
    
    def decrypt(self) -> str:

        plaintext = str()
        inverse = int()

        for i in range(MOD):
            if ((self.coefficient * i)%26) == 1 :
                inverse = i;

        for i in self.text:

            cache = ord(i.upper()); 
            if cache >= 65 and  cache <= 90:
                probe = UTL if i.islower() else 0;
                plaintext += chr((((cache + DIFF - self.shift) 
                          * inverse) % MOD) + DIFF + probe);
            else: 
                plaintext+= i
        

        return plaintext;



# aff = Affine(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
# print(aff.decrypt())