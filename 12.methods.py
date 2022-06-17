from cmath import exp
from math import ceil, fabs, floor, modf, sqrt
from random import shuffle

list = [1, 2, 3, 4] 
shuffle(list)   # LİSTEYİ KARIŞTIRIR
print(list)

print(abs(-5))  # MUTLAK DEĞER ALIR.

print(fabs(-5)) # MUTLAK DEĞER ALIR.

print(exp(1))   # ÜSTEL

print(ceil(3.1))    # ÜSTE YUVARLAMA YAPAR.

print(floor(3.9))   # ALTA YUVARLAMA YAPAR.

print(max(5, 2, 12, 0))   # EN BÜYÜĞÜ BULUR.

print(min(1, 5, 8, 3))  # EN KÜÇÜĞÜ BULUR.

print(modf(12.78))  # TAM VE KÜSÜRAT DÖNER.

print(pow(4, 3))    # ÜS ALIR.

print(round(0.7))
print(round(-3.8))
print(round(12.49578, 3))   # İKİNCİ PARAMETRE VİRGÜLDEN SONRA KAÇ BASAMAK YUVARLANACAĞIDIR.

print(sqrt(16))


