from time import sleep

def tam_sayiya_yuvarla():
    girdi = input('Ondalık sayı giriniz: ')
    
    state = None   # Node ekosisteminden geldiğimiz belli olsun  :)

    try:  # içindeki işlemleri dene, bir problem yoksa finally'ye zıpla.
        girdi = float(girdi)
        print(f'Yuvarlama işleminin sonucu: {round(girdi)}') # round metodu yuvarlama işlemi yapar.
        state = True
    except:  # try içinde rastladığın ilk hatada hemen buraya atla, sonrasında finally'ye uğra.
        print(f'Girilen {girdi} değeri ondalık değil!')
        state = False
    finally:  # try da çalışsa except de çalışsa her zaman çalışacak kısım.
        print(f'Tam sayiya çevirme işleminin sonucu: {state}')

tam_sayiya_yuvarla()

print('------------------- İkinci Örnek --------------------')

# def bolme_islemi():
#     sayi1 = int(input('Birinci sayiyi giriniz:'))
#     while True:
#         sayi2 = int(input('İkinci sayiyi giriniz:'))
#         print('Hesaplanıyor...')
#         sleep(1)

#         try:
#             sonuc = sayi1 / sayi2
#         except:
#             print("0'a bölünme hatası!")
#             continue
#         break

#     print(f'Sonuç: {sonuc}')

# bolme_islemi()

