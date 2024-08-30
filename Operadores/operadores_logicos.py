saldo = 1000
saque = 250
limite = 200
conta_especial = True

# o and significa (E) para dar verdadeiro ambas as comparações tem que estar corretas
print(True and True)
print(True and False)
print(True and True)
print(True and False)

# o or significa (ou) para dar verdadeiro apenas um dos dois tem que estar corretos
print(True or True)
print(True or False)



exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) 
print(exp_2)

conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite)
conta_especial_com_suficiente = (conta_especial and saldo >= saque) 
print(conta_normal_com_saldo_suficiente)
print(conta_especial_com_suficiente)

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_suficiente
print(exp_3)
