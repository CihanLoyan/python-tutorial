# Garbage Collector artık kullanılmayan değerleri otomatik olarak temizlemektedir. 
# Otomatik temizlik yerine kendiniz temizlemek istediğimizde del komutu kullanabiliriz.
# Memory içerisinde bulunan bir nesne eğer kullanılıyorsa silme söz konusu değildir.

sayi1 = 2
sayi2 = 4

print(sayi1, sayi2)

del sayi1, sayi2


#############################################################################################

karakter = "Merhaba"

print(karakter)
print(karakter[2])
print(karakter[3:6])
print(karakter[2:])
print(karakter * 2)
print(karakter + 'Python')
print(karakter, 'Python')
print(karakter[-4])
print(karakter[-4:])
print(karakter[-3:-1])
print(karakter[1:6:2])
print(len(karakter))

karakter = karakter + 'Python'
print(karakter)
# MerhabaPython
print("Bulunduğu index:", karakter.find('y'))

print(karakter.upper())
print(karakter.lower())

karakter2 = 'Salih Kılıç'
print("karakter2.split:" ,karakter2.split())

ayirKarakter2 = karakter2.split()
print("ayirKarakter2'nin 1. index:", ayirKarakter2[1])

print(karakter2.split('l'))

cumle = "Merhaba ben Salih Kılıç. Python öğreniyorum."
kelimeSayisi = cumle.split(' ') # yukarıdaki gibi parametresiz split kullanımı ile aynı işi görür.
print("cumle:", kelimeSayisi)
print("cumle kelime sayısı:", len(kelimeSayisi))

cumle2 = "Merhaba ben Cihan. Python öğreniyorum. Kolay gelsin."
maxSplitKullanimi = cumle2.split(sep='.', maxsplit=2) # maxsplit değerini değiştirip farkı gör.
print(maxSplitKullanimi)
print(len(maxSplitKullanimi))
