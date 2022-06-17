from time import sleep

def bolme_islemi():
    sayi1 = int(input('Birinci sayiyi giriniz:'))
    while True:
        sayi2 = int(input('İkinci sayiyi giriniz:'))
        print('Hesaplanıyor...')
        sleep(2)

        try:
            sonuc = sayi1 / sayi2
        except:
            print("0'a bölünme hatası!")
            continue
        break

    print(f'Sonuç: {sonuc}')

bolme_islemi()