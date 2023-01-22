ano = int(input())

if ano <= 100:
  print("1")
elif ano % 100 == 0:
  seculo = ano //100
  print(seculo)
else:
   resultado = ano //100 + 1
   print (resultado)