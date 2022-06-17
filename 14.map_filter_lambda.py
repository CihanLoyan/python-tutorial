# map, fiter, lambda

print('-------------- Map kullanmadan:--------------------')

def karesini_al(i):
    return i**2

# sayilar = [1, 2, 3, 4, 5]
# for i in sayilar:
#     karesi = []  # Aşağıdaki örnekle neden farklı sonuç üretiyorlar?
#     karesi.append(karesini_al(i))

sayilar = [1, 2, 3, 4, 5]
karesi = [] # Yeni bir dizi oluşturmak zorunda kalıyoruz.
for i in sayilar:
    karesi.append(karesini_al(i))
    

print(karesi)


print('-------------- Map kullanarak: -----------------------')

print(list(map(karesini_al, sayilar)))
# Yeni bir dizi oluşturmak zorunda kalmıyoruz. map bize işlem yaptıktan sonra sonucu zaten yeni bir dizi olarak döndürüyor.
print(sayilar) # Ahanda kanıtı :) sayilar dizisinin değişmediğini görüyoruz.


print('--------------- Filter kullanmadan ---------------------')


def tek_sayi_bul(k):
    return k if k % 2 == 1 else None

# sayilar = [1, 2, 3, 4, 5] 
tek_sayilar = []
for i in sayilar:
    if tek_sayi_bul(i) == None: # Bu sorguyu yapmasaydık çift sayıların olduğu yerde None yazacaktı.
        continue
    else: tek_sayilar.append(tek_sayi_bul(i))

print(sayilar)
print(tek_sayilar)

# def tek_sayi_bul(k): # Yukarıdaki örneğin benzer yazımı
#     if k % 2 == 1:
#         return k


print('---------------- Filter Kullanarak ---------------')

print(list(filter(tek_sayi_bul, sayilar))) # Terrrrtemizzz...
print(sayilar) 
# Görüldüğü üzere yeni bir dizi tanımlamaya da ihtiyaç olmadı çünkü filter yeni bir dizi döndürdü.

print('------------- Lambda ve Map ------------------')

# sayilar = [1, 2, 3, 4, 5] 
print(list(map(lambda s: s ** 2, sayilar))) # Aman Yarabbi gözlerime inanamıyorum!!!
# Elimizde sadece dizimiz var, lambda sayesinde önceden fonksiyon oluşturmaya da gerek kalmadı.
# lambda'dan sonraki s ifadesi karesini_al fonksiyonunun parametresi, :'dan sonrası ise return edilen kısımdır.
print(sayilar)
# Aynı zamanda map ve filter gibi bize yeni bir dizi döndürdü.

print('----------- Lambda ve Filter -----------------')
print(list(filter(lambda t: t if t % 2 == 1 else None, sayilar)))
print(sayilar)

    