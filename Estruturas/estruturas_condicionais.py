maior_idade = 18
idade_especial = 17

idade = int(input("Informe sua idade: "))

#if
if idade >= 18:
    print("Pode tirar a CNH")

if idade <18:
    print("Não pode tirar a CNH, ainda não completou 18 anos")



#if else
if idade >= 18:
    print("Pode tirar a CNH")
else:
    print("Não pode tirar a CNH, ainda não completou 18 anos")



#if elif else
if idade >= 18:
    print("Pode tirar a CNH")
elif idade == idade_especial:
    print("Você pode fazer aulas teoricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH")



# if aninhado / if dentro de if
conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saldo <= (cheque_especial + saque):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Salldo insuficiente")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!") 
else:
    print("Tipo de conta invalida, escolha uma disponivel")




# if ternário / código de if somente em uma linha
saldo = 2000
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")
