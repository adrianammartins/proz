print("Dados do usuário: ")

ano_atual = 2022

while True:
  try:
    print("Digite o nome completo: ")
    nome= str(input())
    print("Digite o ano de nascimento entre 1922 e 2021: ")
    ano_nascimento = int(input())

    idade = ano_atual - ano_nascimento

    if(ano_nascimento>=1922) and (ano_nascimento <=2021):
      
      print("Idade: ", idade, "anos")
      break
    else:
      print("O ano está incorreto! Precisa ser entre 1922 e 2021.")
      
  except:
    print("Dados Incorretos!")

print("FINALIZADO!")

