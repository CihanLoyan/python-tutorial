
class Araba():

    Uretim = 0

    def __init__(self, marka, model, yakit, motor, vites):
        self.marka = marka
        self.model = model
        self.yakit = yakit
        self.motor = motor
        self.vites = vites

    def arac_bilgi(self):
        print(f'Marka: {self.marka}, Model: {self.model}, Yakıt: {self.yakit}, Motor: {self.motor}, Vites: {self.vites}')

    def uretim(self):
        self.Uretim += 1

araba1 = Araba('Doğan SLX', 1989, 'LPG', '1.5 cc', 'Manuel')
print('araba1 markası: ', araba1.marka)
araba1.arac_bilgi()

araba2 = Araba('Togg', 2022, 'Elektrik', '240 kW', 'Otomatik')
print('araba2 yakıt türü: ', araba2.yakit)
araba1.arac_bilgi()

print('-------------------------------------------')

araba2.uretim()
print(araba2.Uretim)
araba2.uretim()
print(araba2.Uretim)

print('----------------------- SERİ ÜRETİME GEÇELİM :) ---------------------------')

for i in range(5):
    araba1.uretim()
    print('araba1 üretilidi.')
    print(f'Mevcut araba1 adeti {araba1.Uretim}')
print(f'Fabrikadaki araba1 sayısı: {araba1.Uretim}')
