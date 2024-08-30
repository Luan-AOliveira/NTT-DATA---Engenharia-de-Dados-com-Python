# o break serve para forçar o while a parar com uma condição formada ja
# no caso aqui 10 o while ira rodar enquanto for verdade no caso enquanto não informar 10 o codigo nao ira parar
# agora no momento que informar o 10 o código para na hora


while True: # o código ira rodar enquanto for verdadeiro
    numero = int(input("Informe um número: ")) 
    
    if numero == 10:
        break
    
    print(numero)



# break também da para ser usado com for
for numero in range(100):
    
    if numero == 10:
        break

    print(numero, end=" ")



# nos temos o continue ele serve para desviar de algo especifico dentro do laço
# neste caso o número 12 ele ira pular o número 12

for numero in range(100):
    
    if numero == 12:
        continue

    print(numero, end=" ")
    
   
    
# este código mostra todos os numéros impares ate o 99 pulando os pares
for numero in range(100):
    
    if numero % 2 == 0:
        continue

    print(numero, end=" ")
