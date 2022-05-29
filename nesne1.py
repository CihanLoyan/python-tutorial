import math

class Daire:

    Sayi = 0

    def __init__(self, r):
        self.yaricap = r
        Daire.Sayi += 1
    
    def cevre(self):
        return 2 * math.pi * self.yaricap

    def alan(self):
        return math.pi * self.yaricap ** 2
    
    def __del__(self):
        print("Bay Bay")



nesne01 = Daire(3)
print(nesne01)


class Kure(Daire):
    def alan(self):
        return 4 * math.pi * self.yaricap ** 2
    
    def hacim(self):
        return 4 / 3 * math.pi * self.yaricap ** 3

nesne01 = Kure(2)


