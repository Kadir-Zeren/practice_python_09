colors = 'red', 'blue' , 'pink','red'

print(type(colors))

set_2 = set(colors)

print(type(set_2))

bos_kume = {}
print(type(bos_kume))

bos_kume = set()
print(type(bos_kume))

kumem = {1,2,2,3,3,3}
print(len(kumem))

a = {1,1,2,2,4,4}
print(a)

import string

alfabe = string.ascii_lowercase

listem = list(alfabe)
print(listem)
print(set(listem))

kumem={1,'1',1.0}
print(len(kumem))

print(1==1.0)

a = 23
b = 23
print(a==b)
print(id(a) == id(b))

flower_list = ['rose', 'violet', 'carnation', 'rose', 'orchid', 'rose', 'orchid' ]
flowerset = set(flower_list)
flowerlist = list(flowerset)
print(flowerset)
print(flowerlist)

a= {1,2,3,4}
print(hash(5))
print(hash('avc'))

if True:
 print('if blogu calisti')

if 'false':
 print('if blogu calisti')

a = 5
b = 7

if a<b:
 print('If blogu calisti 3')
 print('Bu her halukarda calisir')

if 0 or "false" and None:
 print("hello universe")

print(bool(None))

minced = True
h_bread = True
lettuce = True
pepper = True
g_store = True

hamburger = minced and h_bread and g_store and(pepper or lettuce)

if hamburger:
 print('Bon Appetid')

print(1 == 1)
print("henry" == "Henry")
print(12 < 12.1)
print("hard" != "easy")

girdi = input('Yes veya No diye bir girdi yaziniz :  ')

a = input(' Bir sayi giriniz : ')
b = input('Ikinci sayiyi giriniz : ')