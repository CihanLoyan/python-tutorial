# from time import sleep

def tam_sayiya_yuvarla():
    girdi = input('Ondalık sayı giriniz: ')
    
    status = False

    try:
        girdi = float(girdi)
        print(f'Yuvarlama işleminin sonucu: {round(girdi)}')
        status = True
    except:
        print(f'Girilen {girdi} sayısı ondalık değil!')
        status = False
    finally:
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
