import random
cc=['cara', 'coroa']

moeda=20
cont=0
cont2=0

for i in range(moeda):
    y=random.choice(cc)
    if y == 'cara':
        #armazenar cara(roberto)
        cont+=1
    elif y == 'coroa':
        #armazenar coroa(roberto)
        cont2+=1

#print do resultado(roberto )
print(cont, cont2)