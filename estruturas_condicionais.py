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
    print("Aubda não pode tirar a CNH")
