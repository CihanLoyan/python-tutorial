from pickle import FALSE


a, b = True, False

print(a, b)

c, d = "True", "False"

print(c, d)

print(a == True)
print(b == False)

print(c == True) # ??? NEDEN ??? 
# Nedenini bulamazsan aşağıdaki yorum satırlarını açıp kodu yeniden derle.

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

yas = 10
print(yas == 10)
print(yas > 10)
print(yas >= 10)
print(yas < 10)
print(yas <= 10)
print(yas != 12) # yas değişkeni eşit değil mi 12'ye?
# print(yas !> 10) ! operatörü > ve < operatörleri ile kullanılamaz. Bunun yerine:
print(not yas < 12) # yas değişkeni küçük değil mi 12'den?
print(not yas > 12) # yas değişkeni büyük değil mi 12'den?

print(not yas != 10) # İşin biraz suyunu çıkartalım :)