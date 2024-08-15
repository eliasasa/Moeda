import random
moeda=['cara', 'coroa']

X=12
cont=0
cont2=0

for i in range(X):
    y=random.choice(moeda)
    if y == 'cara':
        #armazenar cara(roberto)
        cont+=1
    elif y == 'coroa':
        #armazenar coroa(roberto)
        cont2+=1

#print do resultado(roberto )