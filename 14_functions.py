
def yazdir():
    print(3)
yazdir()


def dondur():
    return 3
dondur() # Neden bu satırı basmayıp es geçti ve alttaki satırı bastı ???
print(dondur())

print('-------------------------------------------------------------')

def mesaj_ver( msj ):   # Parametreli fonksiyon
    print(msj)
mesaj_ver('Merhaba') 


def islem_yap(a, b):
    return a + b
islem_yap(4, 3) # Bu satırı neden yazdırmadığını öğrendiğimizi düşünüyorum :)
print(islem_yap(6, 9))

print('----------------- PRINT VE RETURN FARKI  ---------------------')

yazdir_degiskeni = yazdir()
dondur_degiskeni = dondur()

print('Yazdir değişkeni: ', yazdir_degiskeni)
print('Döndür değişkeni: ', dondur_degiskeni)

print(' ----------- AMAN ALLAHIM YUKARIDA NELER OLDU ÖYLE! :) ------------')

def func( sayi ):
    return sayi
print(func(5))

def func2( sayi = 23):
    return sayi
print(func2())  # Parametre göndermezsem fonksiyondaki varsayılan parametreyi kabul eder.

print(func2(34))  # Parametre gönderirsem, fonksiyonda varsayılan olarak tanımlanmış parametreyi ezmiş olurum.

print('----------------------------------------------')

def buyuk_sayiyi_dondur(x, y):
    if x != y:
        if x > y: return x
        else: return y
    return 'sayilar eşit' # Sayıların eşit olması durumunda, "sayılar eşit" mesajını print olarak bassaydık ne olurdu ?
    # Eğer bu şekilde return olarak String ifade döndürmeyip, "sayılar eşit" mesajını print içerisinde bassaydık, sayıların eşit olması durumunda ekrana None basılmış olurdu(sebebi print ve return farkı kısmında açıklandı).

buyuk_sayi = buyuk_sayiyi_dondur(3, 3)
print(buyuk_sayi)


print('----------------------------------------------')

def yas_soyle( yas ):
    return str(yas) # Neden tip dönüşümü yaptık? Tip dönüşümü yapmadan denesek ne olurdu?

def tanisma(ad, yas):
    return 'Ben ' + ad + ' ' + yas_soyle(yas) + ' yaşındayım.'

print(tanisma('Cihan', 25))

print('----------------------------------------------')

def isim_soyisim_ayir(isim_soyisim):
    isim = isim_soyisim.split()[0]
    soy_isim = isim_soyisim.split()[1]
    return isim, soy_isim

isim, soy_isim = isim_soyisim_ayir('cihan loyan')
print(isim, soy_isim)

print('----------------------------------------------------')

def sonuc(a):
    return a
sonuc_degisken = sonuc(10)
print(f'return ile tek parametre dönerse tipi {type(sonuc_degisken)} olur')

def sonuc2(x, y):
    return x, y
sonuc2_degisken = sonuc2(5, 9)
print(f'return ile birden fazla parametre dönerse tipi {type(sonuc2_degisken)} olur')


print('-----------------------------------------------------------------')

def birlestir(ad, soyad):
    return ' '.join([ad, soyad])  # Birleştirme yapan ve sonucu str tipinde döndüren metottur.

ad_soyad = birlestir('salih', 'kılıç')
print(ad_soyad)

# ad_soyad2 = birlestir('tayyip', 'salih', 'kılıç')  # Yorum satırını kaldır ve hatayı gör.
# print(ad_soyad2)   
# Çok basit bir problem, bunu çözmek için ne yapmalıyız?

def birlestir2(*args):  # Sınırsız parametre yazabilmemize imkan sağlar.
    return ' '.join(args)

ad_soyad3 = birlestir2('tayyip', 'salih', 'kılıç')
print(ad_soyad3)

ad_soyad_yas = birlestir2('tayyip', 'salih', 'kılıç', '25')
print(ad_soyad_yas)

ad_soyad_yas_memleket = birlestir2('tayyip', 'salih', 'kılıç', '25', 'bursa')
print(ad_soyad_yas_memleket)


def sirala(*args):
    for i in args:
        print(i)
sirala('cihan', 'loyan', 'bursa', '25')


def kimlik(**kwargs):  #keyword-arguments.  Dictionary tipinde parametre girmek gerekiyor. 
    if 'departman' in kwargs:  # Girilen dict'nin içinde key değeri olarak 'departman'ı arıyor.
        print(kwargs['departman'])  # Eğer varsa departman key'inin value'sunu döndürüyor.
    else:
        print('Böyle bir key değeri yok.')

kimlik(ad = 'cihan', soyad = 'loyan', departman = 'yazılım')