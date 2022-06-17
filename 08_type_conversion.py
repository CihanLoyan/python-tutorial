tamSayi = 5
ondalikSayi = 10.7
karakter = '100'

yeniTamSayi = float(tamSayi)
print(type(yeniTamSayi), yeniTamSayi)

yeniOndalik = str(ondalikSayi)
print(type(yeniOndalik), yeniOndalik)

# karakter öncelikle 2'li tabana dönüştürülür. 
# Ardından int() ile 10'luk tabana dönüştürmüş oluruz.
print(int(karakter, 2)) # (100)2 değeri -> (100)10 olarak dönüştürülür.
print(int(karakter, 4))
print(int(karakter, 8))  # (100)8 -> (100)10
print(int(karakter, 16))

karakter = '102'
print(int(karakter, 2)) # Neden hata verir?