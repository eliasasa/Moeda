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