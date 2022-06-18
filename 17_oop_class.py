
class Araba():

    Uretim = 0

    def __init__(self, marka, model, yakit, motor, vites):
        self.marka = marka
        self.model = model
        self.yakit = yakit
        self.motor = motor
        self.vites = vites


araba1 = Araba('Doğan SLX', 1989, 'LPG', '1.5 cc', 'Manuel')
print('araba1 markası: ', araba1.marka)

araba2 = Araba('Togg', 2022, 'Elektrik', '240 kW', 'Otomatik')
print('araba2 yakıt türü: ', araba2.yakit)
