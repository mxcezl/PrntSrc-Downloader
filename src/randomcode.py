from random import randint
import random
import string

class RandomsiedCode:
    def __init__(self):
        self.code = self.getRandomCode()

    def __str__(self):
        return self.code

    def anotherCode(self):
        self.code = self.getRandomCode()
        return self.code
        
    def getRandomCode(self):
        return self.getRandomChars() + str(self.getRandomDigits())

    def getRandomDigits(self):
        rand = str(randint(0,9999))
        if len(rand) != 4:
            rand = (4-len(rand)) * "0" + rand
        return rand
    
    def getCode(self):
        return self.code
    
    def getRandomChars(self):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(2))
