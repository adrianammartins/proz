def calculadora(numero1, numero2,opcao):
    
    
    if opcao == 0:
      print("sair") 
    elif opcao == 1:
      return numero1 + numero2
    elif opcao == 2:
      return numero1 - numero2
    elif opcao == 3:
     return numero1 * numero2
    elif opcao == 4:
     return numero1 / numero2
    else:
      return "essa opção não existe"


while True:
    
    opcao= int(input("Digite o numero da opção3: (1: soma, 2: subtracao, 3:multiplicação, 4: divisão, 0:sair): "))
    
    numero1= float(input("Digite o primeiro número: "))
    numero2= float(input("Digite o segundo número: "))
    
    resultado = calculadora(numero1, numero2, opcao)
    print("Resultado: ", resultado)
