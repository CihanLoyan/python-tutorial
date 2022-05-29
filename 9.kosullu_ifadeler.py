
# notun = int(input("Notu giriniz:"))
# if notun > 89:
#     print("AA")
# elif notun > 79:
#     print("BB")
# elif notun > 69:
#     print("CC")
# elif notun > 59:
#     print("DD")
# else:
#     print("Kaldın")

# # Tek satırda if-else kullanımı
# sumeyye = 10
# print("doğru") if sumeyye == 16 else print("yanlış")

#################################################################

harfler = ['a', 'b', 'c']
while True:
    arananHarf = input('Bir harf giriniz: ')
    if len(arananHarf) != 1: 
        continue
    elif arananHarf in harfler:
        print('Aranan harf bulundu')
    else:
        print('Aranan harf listede bulunamadı! Listeye eklensin mi?')
        while True:
            cevap = input('Cevabınızı buraya yazabilirsiniz:(evet/hayır)')
            if cevap == 'evet' or cevap == 'EVET': 
                harfler.append(arananHarf)
                print(f'Listeye ekleme işlemi başarılı. Güncel Liste: {harfler}')
                break
            elif cevap == 'hayır' or cevap == 'HAYIR': 
                print(f'Güncel Liste: {harfler}')
                break
            else: continue
        break
            

