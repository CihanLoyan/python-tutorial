user = "anonymous"


def login():
    print ("- giriş işlemi yapılıyor...")
    user = "umut"
    print("- oturumdaki kullanıcı: {}".format(user))
    print(locals())
    print(globals())


print("- oturumdaki kullanıcı: {}".format(user))

login()

print("- fonksiyon dışında oturumdaki kullanıcı: {}".format(user))
print(locals())
print(globals())