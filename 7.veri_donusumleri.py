tamSayi = 5
ondalikSayi = 10.7
karakter = '100'

yeniTamSayi = float(tamSayi)
print(type(yeniTamSayi), yeniTamSayi)

yeniOndalik = str(ondalikSayi)
print(type(yeniOndalik), yeniOndalik)

# karakter öncelikle integer tipine dönüştürülür.
print(int(karakter, 2)) # (100)2 değeri -> (100)10 olarak dönüştürür.
print(int(karakter, 4))
print(int(100, 8))  # (100)8 -> (100)10
print(int(karakter, 16))

karakter = '102'
print(int(karakter, 2)) # Neden hata verir?

