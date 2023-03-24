phone={
    'samsung':{
    'name':'galaxy m21',
    'front camera':'16mp',
    'back camera':'48mp',
    'ram':'4gb',
    'rom':'48mp',
    'price':'14000',
    'battery':'5000mah',
    'os':'android',
    'processor':'exynos 9811'

    },
    'redmi':{
    'name':'redmi 9 activ',
    'front camera':'8mp',
    'back camera':'12mp',
    'ram':'4gb',
    'rom':'48mp',
    'price':'9000',
    'battery':'5000mah',
    'os':'android',
    'processor':'helio g95'
    },
    'vivo':{
    'name':'1987',
    'front camera':'8mp',
    'back camera':'12mp',
    'ram':'8gb',
    'rom':'12mp',
    'price':'14000',
    'battery':'5000mah',
    'os':'android',
    'processor':'exynos 9811'
    }
}
'''print(phone)   #print the entire dictionary
print(phone['samsung'])  #print specific item
print(len(phone))

print(phone['redmi'].keys())
print(phone['redmi'].values())

phone['redmi']['price']=9000

print(phone['redmi'].values())
print(phone['redmi'])

print(phone['redmi'].items())'''

'''user=input("enter the brand name:").lower()  #get a user input and printing a price and checking the phone in our shop
if user in phone.keys():
    print(f"{user} is in our shop.Its price is {phone[user]['price']}" )
else:
    print(f"{user} is not in our shop")'''

'''phone['redmi'].update({'color':'Red'}) #updating a key and values
print(phone['redmi'].items())

phone['redmi'].pop('processor')  #deleting a processor key values
print(phone['redmi'].items())'''

'''phone['redmi'].popitem()   #deleting a last items(stack concept)
print(phone['redmi'].items())'''


'''del phone['redmi']['price']
print(phone['redmi'].items())'''

'''print(phone)

del phone['redmi']   #deleting the redmi dictionary
print(phone)

del phone  #deleting the whole dictionary
print(phone)'''

'''for i in phone:     #looping the for
    print(f"{i} {phone[i]['price']}")'''

'''print(phone['samsung'].items())


for i,j  in phone['samsung'].items(): #printing one by one
    print(i,j)

yourphones=dict(phone)
print(yourphones)'''

androidphones={
    'androidphone1': phone['redmi'],
    'androidphone2': phone['samsung']
}
#print(androidphones)

for i,j in androidphones.items():
    print(f"{j['name']}:{j['price']}")

for i in androidphones:
    androidphones[i].setdefault('fingerprint','indisplay')
print(androidphones)
