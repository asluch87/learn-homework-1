import ephem

from pprint import pprint



Newproduct = [ 
    {"price": 50000,
    "color": ['white','black'],
    "Nalichie":[True,False],
    "discount" : 10
},
 {  "price": 125812321319,
    "color": ['whit333e','b333lack'],
   "Nalichie":[True,False]}
]




newnew = {
a:3,
b:4

}
print (newnew)            

print(Newproduct)


print(Newproduct[1]['Nalichie'][1])

print (Newproduct[0]['price'] + 100000000000000) 

Newproduct[0]['color'].append('red')


print(Newproduct) 


Newproduct[0]['color'][0]




#Функции#



price = 100
discount = 95
def discounted(price,discount,max_discount = 20):
    if max_discount >= 100:
        raise ValueError ('Максимально до 100')
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - price*discount/100
    return price_with_discount
print 
#print(discounted(Newproduct[0]['price'],Newproduct[0]['discount']))

#Newproduct[3]['withdiscount'] = discounted(Newproduct[0]['price'],Newproduct[0]['discount'])
#print (Newproduct)


 
Newproduct = [ 
    {"price": 50000,
    "color": ['white','black'],
    "Nalichie":[True,False],
    "discount" : 10,
    "dis": 99
},
 {  "price": 1234,
    "color": ['whit333e','b333lack'],
   "Nalichie":[True,False],
   "discount" : 10,
   "dis": 99
   }
]



for phone  in Newproduct:
   phone['NEW_PRICE'] = discounted(phone['price'],phone['discount'],max_discount= phone['dis'])
print (Newproduct)








for phone in Newproduct:

    print(phone['price'])




x = 1 
while x<50:
    print(x)
    x+=1






def find_person():
    try:
        name = ['Вася','Маша','Петя','Саша']
        i = 0
        while name[5] != 'Сашаfff' :
            i +=1
            print(name[i])
            print('найден')
    except:
        print('Не найден такого нет')

find_person()


def zero_dev():
    try:
        a = 1/0
        print (a)
    except:
        print("На ноль делить нельзя")
zero_dev()

