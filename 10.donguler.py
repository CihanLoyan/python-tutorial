
toplam = 0
while toplam <= 5:
    print(f"toplam: {toplam}")
    toplam += 1
else:
    print("donguden çıkıldı")


print("***********************************************************************************")


sayi = int(input('Faktöriyeli hesaplanacak sayıyı giriniz: '))
fakt = 1
while sayi > 0:
    fakt = fakt * sayi
    sayi -= 1 
print('Sonuç: ', fakt)


print("***********************************************************************************")

devamMi = 'e'
while devamMi == 'e':
    sayi = int(input('Sayiyi giriniz: '))
    asalMi = True
    if sayi >= 2:
        for i in range(2, sayi):
            if sayi % i == 0:
                asalMi = False
                break 
        print('asal değildir') if asalMi == False else print('asaldır')
        devamMi = input('Devam etmek istiyor musunuz?(e/h)')


print("***********************************************************************************")

for harf in 'Bursa':
    print("Geçerli harf:", harf)
    
print("**********************************************************************************")

for harf in 'Bursa':
    print(f"Geçerli harf: {harf}")

print("**********************************************************************************")

meyveler = ["muz", "çilek", "ananas", "kiraz", "erik", "şeftali", "armut", "ayva"]
for meyve in meyveler:
    print("Meyve:", meyve)

print("***********************************************************************************")

# Tek parametre verirsek start 0, stop verdiğimiz parametre değerini alır. Step ise otomatik olarak 1 olur.
for i in range(2):  # for(i=0; i<2; i++)
    print("Geçerli meyve: ", meyveler[i])   

print("***********************************************************************************")

# İki parametreli olursa start 1. parametre, stop 2. parametre, step ise 1 olarak ayarlanır.
for m in range(2, 6):   # for(i=2; i<6; i++)
    print("Geçerli meyve: ", meyveler[m])

print("***********************************************************************************")
    
# Üç parametreli olursa 3. parametre step değerini alır.
for k in range(3, 7, 2):    # for(i=3; i<7; i+=2)
    print(f"{k}. meyve: ", meyveler[k])

print("***********************************************************************************")

# Tek parametre almakla aynıdır. start 0, stop verilen parametre, step 1 olarak ayarlanır.
for t in range(len(meyveler)):
    # print(f"{t}. Meyve:", meyveler[t])
    print(str((t+1)) + ".", "Meyve:", meyveler[t])

print("***********************************************************************************")

liste = [[1, 2], [3, 4]]
for x in liste:
    print(x)


print("***********************************************************************************")


liste1 = [[1, 2],[3, 4]]
for k, t in liste1:
    print(f'Liste1:  k:{k} t:{t}')


# liste2 = [[1, 2], [3, 4], [5, 6]]
# for x, y, z in liste2:
#     print(x, y, z)    # ÇALIŞIR MI?


liste3 = [[1, 2, 3], [4, 5, 6]]
for x, y, z in liste3:
     print(f'Liste3:  x:{x} y:{y} z:{z}')


print("***********************************************************************************")


bilgi = {
    'ad': 'cihan',
    'yas': 24
}
print('Bilgi:', bilgi.items())

print("***********************************************************************************")

for b in bilgi.items():
    print(b)

print("***********************************************************************************")

print('Keys:', bilgi.keys())
print('Values:', bilgi.values())

print("***********************************************************************************")

for k, v in bilgi.items():
    print(f'Key: {k} \t Value: {v}')

