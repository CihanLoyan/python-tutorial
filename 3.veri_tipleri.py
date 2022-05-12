# Garbage Collector artık kullanılmayan değerleri otomatik olarak temizlemektedir. 
# Otomatik temizlik yerine kendiniz temizlemek istediğimizde del komutu kullanabiliriz.
# Memory içerisinde bulunan bir nesne eğer kullanılıyorsa silme söz konusu değildir.
# Gereksiz ve artık kullanılmayan değişkenleri 
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
print(karakter + ' Python')
print(karakter, 'Python')


