placa = int(input())

resultado = placa % 10

if resultado == 1 or resultado == 2:
  print("segunda-feira")

elif resultado == 3 or resultado == 4: 
  print("terça-feira")

elif resultado == 5 or resultado == 6:
  print("quarta-feira")

elif resultado == 7 or resultado == 8:
  print("quinta-feira")

elif resultado == 9 or resultado == 0:
  print("sexta-feira")
  