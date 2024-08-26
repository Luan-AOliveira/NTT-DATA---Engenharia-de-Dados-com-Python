def sacar(valor):
    valor = float(input("Informa o valor de saque: "))
    saldo = 500.0
    
    if saldo >= valor:
        print("Valor Sacado!")
        saldo_total = saldo - valor
        print(f"Seu saldo agora é: {saldo_total}")
    else:
        print("Valor Insuficiente")

        
sacar(100)


#if
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Saque realizado com sucesso")
    total_saldo = saldo - saque
    print(f"Seu saldo agora é {total_saldo}")
    
if saldo < saque:
    print("Saldo insuficiente")


# agora fazendo o mesmo com if else
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Saque realizado com sucesso")
    total_saldo = saldo - saque
    print(f"Seu saldo agora é {total_saldo}")
    
else:
    print("Saldo insuficiente")



#agora com if/elif/else
opcao = int(input("Informe uma opção: [1] Sacar\n[2] Extratp"))

if opcao == 1:
    valor = float(input("Informa a quantia para o saque: "))
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    sys.exit("Opção inválidada")
