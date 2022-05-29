# Listeye benzer bir veri türüdür. 
# Listelere göre farkı sadece okunabilirdir. (read-only) modda olmasıdır. 
# Öğe sayısı arttırılamaz ve güncellenemezler. "Immutability"

tuple1 = ('abcd', 786 , 2.23, 'Çorlu', 70.2, 'ABCD', 786)
print(tuple1)
print(tuple1[3])
print(tuple1[1:4])

# tuple1[2] = 23.5  # Yorum satırını kaldırıp tekrar çalıştır.

print(tuple1.count('b'))  # Return number of occurrences of value.
print(tuple1.count('abcd'))
print(tuple1.count(786))

print(tuple1.index(2.23)) # Girilen değerin kaçıncı index'te olduğunu gösterir.
print(tuple1.index(786))  # Mükerrer bir değerse ilk konumunu return eder.

# print(tuple1.index('Salih')) # Açıklama satırını kaldır ve hatayı oku.
# ??? count metoduna tuple'da olmayan bir değer girildiğinde 0 döndürmesine rağmen;
#     aynı durum için index metodu neden hata verdi ??? Düşünelim !
