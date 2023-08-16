quantidade_rodas = int(input("informe q quantidade de rodas do veículo: "))
peso_bruto = float(input("Informe o peso bruto em quilogramas: "))
quantidade_pessoas= int(input("Informe a quantidade de pessoas no veículo: "))

if(quantidade_rodas == 2) or (quantidade_rodas == 3):
  print("Categoria A")
elif(quantidade_rodas == 4) and (quantidade_pessoas == 8) and (peso_bruto <= 3500):
    print("Categoria B")
elif(quantidade_rodas >= 4) and (3500> peso_bruto< 6000):
      print("Categoria C")
elif (quantidade_rodas >= 4) and (quantidade_pessoas >= 8):
        print("Categoria D")
elif(quantidade_rodas >=4) and (peso_bruto > 6000):
          print("categoria D")
else:
          print("categoria desconhecida")
