# O while diferente do for ele serve para quando não tem definido quantas vezes o código ira rodar
# Ele so ira parar de rodar o codigo quando algo forçar ele a parar

opcao = -1 #precisa criar essa função
# enquanto opcao for diferente de 0 o codigo roda se se tornar 0 o codigo para
#por isso começa a funão com -1 e no while bota 0

while opcao != 0: # o código só ira parar de rodar quando o usuario escolher a opção 0
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \nInforme o número da opção: ")) # o \n serve para quando for exibir o input ficar uma oção abaixo da outra
    
    if opcao == 1:
        print("Sacando...")
    elif opcao ==2:
        print("Exibindo extrato...")
        
print("Obrigado por usar nosso sistema bancário, até logo!")