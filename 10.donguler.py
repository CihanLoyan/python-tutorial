from operator import le

toplam = 0
while toplam <= 5:
    print(f"toplam: {toplam}")
    
    toplam += 1
else:
    print("donguden çıkıldı")
    
print("***********************************************************************************")

for harf in 'Bursa':
    print("Geçerli harf:", harf)
    
print("**********************************************************************************")

for harf in 'Bursa':
    print(f"Geçerli harf: {harf}")

print()

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
