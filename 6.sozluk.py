dict1 = {} #boş bir dictinary
dict1['ad'] = "osmancık"
dict1['basimYili'] = 1988

# Okunabilirlik açısından tavsiye edilen yazım şekli aşağıdaki gibidir:
dict2 = {
    'name': 'Salih', 
    'age': 24, 
    'department': 'Makine Mühendisliği', 
    'number': '031620016',
    'location': {  # Dict içinde dict
        'born': 'M.K.Paşa',
        'live': 'Bursa'
    }
}

print(dict1)
print(dict2)

print(dict1['ad'])
print(dict2['number'])
print(dict2['location'])
print(dict2['location']['live'])

print(dict1.keys())
print(dict1.values())
print(dict1.items())

dict2Keys = dict2.keys()
dict2Value = dict2.values()
print(dict2Keys, dict2Value)
print(dict1.items())