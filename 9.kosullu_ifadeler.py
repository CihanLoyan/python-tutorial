
notun = int(input("Notu giriniz:"))
print(type(notun))
if notun > 90:
    print("AA")
elif notun > 80:
    print("BB")
elif notun > 70:
    print("CC")
elif notun > 60:
    print("DD")
else:
    print("Kaldın")

# Tek satırda if-else kullanımı
sumeyye = 10
print("doğru") if sumeyye == 16 else print("yanlış")