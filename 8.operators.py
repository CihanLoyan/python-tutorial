# Tam bölme yapar. Sonuç negatifse negatif tarafa doğru yuvarlar.
print(9/2)
print(9//2)

print(11/3)
print(11//3)

print(-9/2) 
print(-9//2) # Sonuç -4.5 çıkmasına rağmen negatif tarafa yuvarlanmıştır.

print("<----(-6)----(-5)----(-4)----(-3)---(-2)----(-1)----(0)----(1)----(2)----(3)----(4)--(5)--(6)-->")

# Her zaman küçük olan tama yuvarlanır diyebiliriz.

print(-11/3)
print(-11//3)

print("************************************************************************************************************")

##################################################################################################

sayi1 = 10
sayi2 = 5

print(sayi1 < 20 and sayi2 > 3)
print(sayi1 < 8 and sayi2 > 3)
print(sayi1 < 8 or sayi2 > 3)

print(sayi1 > sayi2)
print(not(sayi1 > sayi2))

print(sayi1**sayi2)
sayi1**=sayi2
print(sayi1, sayi2)

print("************************************************************************************************************")

#######################################################################################################

c, d, f, g = 1, 2, 3, 4
print(format(c, 'b'))   # 2'lik tabana çevirir.
print(format(d, 'b'))
print(format(f, 'b'))
print(format(g, 'b'))

print(format(c, 'd'))   # 10'luk tabana çevirir.
print(format(d, 'd'))
print(format(f, 'd'))
print(format(g, 'd'))

x, y, z, g = 1, 0, 0, 60
print(format(g, 'b'))   # 2'lik tabana çevirir.
print(format(13, 'b'))   # 2'lik tabana çevirir.

print(f"{x} & {y} =", x & y)
print(f"{x} | {y} =", x | y)
print(f"{x} ^ {z} =", x ^ z) # XOR - İki bitten yalnızca biri 1 ise, her biti 1 olarak ayarlar.
print(f"{y} ^ {z} =", y ^ z) 
print(f"{x} & {y} =", ~(x & y))
print(f"{y} & {z} =", ~(y & z))

x, y = 2, 3
print("x", bin(x))
print("y", bin(y))

print("****************************************************************************************************")

#################################################################################################

meyveler = ["elma", "armut", "kiraz"]
print("elma" in meyveler)
print("muz" not in meyveler)

ogrenciler = ["yavuz", "salih", "cihan", "sümeyye"]
ad = input("adınızı giriniz: ")
if(ad in ogrenciler):
    print("bulundu")
else:
    print("bulunamadı")
    
print("***********************************************************************************")

sm, cn = 1, 1
print(id(sm) == id(cn))
print(id(sm) != id(cn))

print(sm is cn)
print(sm is not cn)

