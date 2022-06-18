from time import sleep

def tam_sayiya_yuvarla():
    girdi = input('Ondalık sayı giriniz: ')
    
    status = False

    try:  # içindeki işlemleri dene, bir problem yoksa finally'ye zıpla.
        girdi = float(girdi)
        print(f'Yuvarlama işleminin sonucu: {round(girdi)}')
        status = True
    except:  # try içinde rastladığın ilk hatada hemen buraya atla, sonrasında finally'ye uğra.
        print(f'Girilen {girdi} sayısı ondalık değil!')
        status = False
    finally:  # try'da çalışsa except'te çalışsa her zaman çalışacak kısım.
        print(f'Tam sayiya çevirme işleminin sonucu: {status}')

tam_sayiya_yuvarla()

print('------------------- İkinci Örnek --------------------')

# def bolme_islemi():
#     sayi1 = int(input('Birinci sayiyi giriniz:'))
#     while True:
#         sayi2 = int(input('İkinci sayiyi giriniz:'))
#         print('Hesaplanıyor...')
#         sleep(2)

#         try:
#             sonuc = sayi1 / sayi2
#         except:
#             print("0'a bölünme hatası!")
#             continue
#         break

#     print(f'Sonuç: {sonuc}')

# bolme_islemi()
