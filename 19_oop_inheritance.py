# class Personel():

#     def __init__(self, ad, sicil_no, maas, departman):
#         self.ad = ad
#         self.sicil_no = sicil_no
#         self.maas = maas
#         self.departman = departman
    
#     def personel_bilgi(self):
#         print(f'Adı: {self.ad}, Sicil No: {self.sicil_no}, Maaş: {self.maas}, Dept: {self.departman}')


# class Muhendis(Personel):
#     def __init__(self, ad, sicil_no, maas, departman, dil):
#         Personel.__init__(self, ad, sicil_no, maas, departman)
#         self.dil = dil


# obj1 = Muhendis('Sümeyye Mutlu', 12345, 10000, 'Yazılım', 'İngilizce')
# print(obj1.ad)  # Nesne üzerinden tek bir niteliğe eriştim.
# obj1.personel_bilgi()

from pprint import pprint


class Seyahat():
    def __init__(self, kalkis, varis):
        self.kalkis = kalkis
        self.varis = varis

    def anons(self):
        print(f'Kalkış: {self.kalkis}, Varış: {self.varis}')


class Otobus(Seyahat):
    def __init__(self, mola_duraklari, *args):
        super().__init__(*args)
        self.mola_duraklari = mola_duraklari
    
    def anons(self):
        super().anons()
        print(f'{self.mola_duraklari}')

otobus = Otobus(['Silivri', 'Esenler', 'Alibeyköy', 'Dudullu', 'Gebze', 'Bursa', 'Mustafakemalpaşa'], 'Çorlu', 'Mustafakemalpaşa')
otobus.anons()