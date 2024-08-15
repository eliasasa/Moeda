import random
cc=['cara', 'coroa']

cara=0
coroa=0

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
        cara+=1
    elif y == 'coroa':
        coroa+=1


print(f'De', moeda, 'jogadas:\nCara', cara,'\nCoroa:', coroa )