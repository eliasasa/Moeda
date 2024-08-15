import random
cc=['cara', 'coroa']

moeda=20
cont=0
cont2=0

def jogamoeda():
  while True:
    try:
      moeda = int(input("Digite o número de vezes que a moeda será jogada: "))
      if moeda > 0:
        break
      else:
        print("Por favor, digite um número inteiro positivo.")
    except ValueError:
      print("Entrada inválida. Por favor, digite um número inteiro.")
  return moeda

moeda = jogamoeda()
print(f"A moeda será jogada {moeda} vezes.")

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

