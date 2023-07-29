num1= float(input("Digite o primeiro numero: "))
num2= float(input("Digite o segundo nuemro: "))
operacao= float(input("Digite o numero da operacao(1: soma, 2: subtracao, 3: multiplicacao, 4: divisao)"))

resultado = calculadora(num1, num2, operacao)
print(resultado)

def calculadora(num1, num2, operacao):
  if(operacao == 1):
    return num1 + num2 
  elif(operacao == 2):
    return  num1 - num2

  elif(operacao == 3):
    return num1 * num2
  
  elif(operacao == 4):
    if num2 != 0:
      return num1 / num2
      
    else:
     return "divisao por zero não existe"
  else:
      return 0
