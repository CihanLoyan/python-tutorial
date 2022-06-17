list1 = [13, 'cihan', 12.478, '4234']
list2 = ['loyan', 34]

print(list1, list2)
print(list1 + list2)
print(list2[1])
print(list1[1:3])
print(list1[2:])
print(list2 * 3)

list2[1] = 16
print(list2)

# list2 = list2 + 'c'
# print(list2) 
# 14 ve 15. satırlardaki yorum satırını kaldır ve hata mesajına bak!
# Eğer tek bir karakter eklemek istersek:
list2 = list2 + ['c']
print(list2)
# 18. satırda yapılan ekleme işlemi ilkel bir yöntem. Bu işlem için özel bir metot var:
list2.append(5)
print(list2)

print("list2'nin son elemanı:", list2.pop()) # Bu fonksiyon listenin son elemanını listeden çıkarır ve o elemanı return eder.
print("list2 güncel:", list2)

print(list2.pop(1)) # Liste içindeki istediğimiz elemanı listeden çıkarma.
print(list2)

sayilar = [3, 1, 34, 23, 28, 6]

sayilar.reverse() # Diziyi ters çevirir.
print("[3, 1, 34, 23, 28, 6] dizisinin tersi: ", sayilar)

sayilar.sort()  # Dizi içindeki elemanları küçükten büyüğe sıralar.
print("Küçükten büyüğe: ", sayilar)

sayilar.reverse() # Önce sort sonra da reverse kullanarak büyükten küçüğe sıralayabiliriz.
print("Büyükten küçüğe: ", sayilar)

sayilar2 = [45, 23, 52, 16, 8, 23, 45]
print(sayilar2)
print(set(sayilar2)) # Mükerrer elemanları teke indirger.
