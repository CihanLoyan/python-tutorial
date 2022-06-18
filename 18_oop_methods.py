
class Siha():

    Uretim = 0  # Şuana kadar üretilen siha miktarı. Stok miktarıyla alakası yok. 
    Satis = 0   # Şuana kadar satılan siha miktarı. Stok miktarıyla alakası yok.
    Stok = 0    # Her üretim ve satış metotları çalıştığında adete göre güncellenecek kısım.

    def __init__(self, marka, max_irtifa, havada_kalis, max_hiz, yakit):
        self.marka = marka
        self.max_irtifa = max_irtifa
        self.havada_kalis = havada_kalis
        self.max_hiz = max_hiz
        self.yakit = yakit

    def arac_bilgi(self):
        print(f'Marka: {self.marka}, Max İrtifa(feet): {self.max_irtifa}, Havada Kalış(saat): {self.havada_kalis}, Max Hız(knot): {self.max_hiz}, Yakıt: {self.yakit}')

    def uretim(self, adet = 1): # Varsayılan olarak metot her çalıştığında 1 adet üretim yapılacak.
        self.Uretim += adet
        self.Stok += adet

    def satis(self, adet = 1):
        if self.Stok >= adet:
            self.Satis += adet
            self.Stok -= adet
        else:
            print('Stok miktarını aştınız!')

tb2 = Siha('TB2', 25000, 27, 120, 'Benzin')
tb2.arac_bilgi()
print('-------------------------------------------')

tb2.uretim(10) # Varsayılan değeri ezdim. 
print('Stok: ', tb2.Stok)

tb2.satis(8)
print('Stok: ', tb2.Stok)

tb2.satis(2)
print('Stok: ', tb2.Stok)
tb2.satis()

tb2.uretim(5)
print('Stok: ', tb2.Stok)

print('Toplam tb2 Üretim Sayısı: ', tb2.Uretim)
print('Toplam tb2 Satış Sayısı: ', tb2.Satis)

print('----------------------- SERİ ÜRETİME GEÇELİM :) ---------------------------')

for i in range(10):
    tb2.uretim(10)
    print('10 adet tb2 üretildi!!!')    
print(f'Stok: {tb2.Stok}')

