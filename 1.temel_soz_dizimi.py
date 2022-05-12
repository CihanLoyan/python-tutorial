oge_1 = 1
oge_2 = 2
oge_3 = 3
toplam = oge_1 + \
        oge_2 + \
        oge_3
print(toplam)

# [], {} Veya () parantezlerinde bulunan ifadelerin satır devam karakterini kullanmasına gerek yoktur.
# Basit bir dizi üzerinden örnek verelim:

gunler = ['pazartesi', 'salı',
          'perşembe',
          'cuma']
print(gunler)

##########################################################################################

kelime = 'cihan'
cumle = "cihan bilgisayarı aç"
paragraf = """Bu bir paragraftır. Birden
              fazla satır veya cümleden oluşmuştur."""
##########################################################################################

sayi = 14
if sayi<10:
    print('sayi ondan küçüktür')
elif sayi==10:
    print('sayi ona eşittir')
else:
    print('sayi ondan büyüktür')
