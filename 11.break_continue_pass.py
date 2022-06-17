# break, continue, pass

# break, Geçerli döngüyü sonlandırır, iç içe döngüde kullanıyorsak mevcut döngüyü sonlandırır, 
# diğer bloklar ise çalışmaya devam eder.

for harf in "Python":
    if(harf == 'h'):
        break
    else: print(harf)

print()

sayi = 10
while sayi > 0:
    print(sayi)
    sayi-=1
    if sayi == 5:
        break
        print("Burası çalışmaz. break ifadesinden sonra döngüden çıkılır.")
print(f"Döngü {sayi} sayısına gelince sonlandırıldı.")

print("----------------------------------------------------------------------------------")

# continue
# Continue şartı gerçekleşince altta kalan tüm ifadeler atlanıp döngünün başına gidilir.

for h in "Salih":
    if h == 'l':
        continue
        print("Burası çalışmaz. Continue ifadesinden sonra döngünün bu adımı atlanır ve devam eder.")
    print(h)

print()

deger = 0
while deger < 10:
    deger+=1
    if deger == 4 or deger == 8:
        continue
        print("Burası çalışmaz.")
    print(deger)
    # deger+=1
print("Döngü sonlandı.")

print()

for sayi2 in range(1, 8):
    if(sayi2 % 2 == 0):
        continue
    print("Tek sayılar: {}".format(sayi2))

print()

for sayi2 in range(1, 8):
    if(sayi2 % 2 != 0):
        print("Tek sayılar: {}".format(sayi2))

print()

for s in range(1, 20):
    if(s % 3 == 0):
        continue
        print("3'e bölünen sayılar")
    print(f"3'e tam bölünmeyen sayılar: {s}")

print("----------------------------------------------------------------------------------")

# pass
# Continue ifadesine gelince mevcut adım atlanıp devam edilirken, pass ifadesinin bulunduğu
# blok çalışmaya devam eder. 

for h in 'Python':  
    if h == 't':
        pass
        print("t harfine denk gelindi")
    print("Geçerli harf", h)

print()

for h in 'Python':  
    if h == 't':
        pass
        print("t harfine denk gelindi")
    else: print("Geçerli harf", h) # üstteki örneğe göre tek fark else ifadesi olduğunda iki örneğin farklı bir çıktı vermesinin sebebi ne olabilir?

print()

for h in 'Python':  
    if h == 't':
        pass
        print("t harfine denk gelindi")
        continue
    print("Geçerli harf", h)

#######################################################

harfler = ['a', 'b', 'c']
while True:
    arananHarf = input('Bir harf giriniz: ')
    try:
        int(arananHarf)
        print('Sayı girdiniz!!!')
    except:
        if len(arananHarf) != 1:
            print('Birden fazla harf girdiniz!!!')
            continue    # Eğer yukarıdaki şart sağlanmazsa içinde bulunulan döngünün bir sonraki adımından devam et.
        elif arananHarf in harfler:
            print(f'Aranan harf({arananHarf}) bulundu: {harfler}')
            break
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
    continue