#Receba um número do teclado e exiba os 2 números seguintes
a= int(input("Informa um número inteiro: "))
print(a)

a += 1
print(a)

a += 1
print(a)

#Mesmo exemplo porém utilizando o "for" e assim determinando ele fazer a mesma coisa porém automatizado
#E sem precisar ficar repetindo o código porque esta função já faz isso e repete quantas vezes eu mandar
#Quando sabemos quantas vezes ira repetir usa este padrão "for i in range(3)" o range informando quantas
#Vezes ira repetir o código

a= int(input("Informa um número inteiro: "))
print(a)

for i in range(3):
    a += 1
    print(a)


#dentro do rannge como um numero a mais do que o que precisa porque começa a contar a partir do 0
#outros exemplos com range
for numero in range(0, 11):
    print(numero, end=" ")


#range exibindo tabuada do 5
for numero in range(0, 51, 5): # ele vai começar no 0 e vai até 50 contando de 5 em 5
    print(numero, end=" ") #o end="" ele serve para a cada resultado que for gerado pelo loop
print()                    # ele vai dar um espaço entre as respostas e ficar um ao lado da outra em vez de em baixo
   


#Exemplo usando "for" para percorrer um texto informado, e dentro deste texto ele ira retornar as vogais
texto = input("Informe um texto: ")
VOGAIS= "AEIOU"
                                 # função que esta como letra pode ser chamado de qualquer coisa pórem as vogais encontradas no texto iram ficar armazenas em "letra"
for letra in texto:              # o if se lê "(if)se letra esta(in) dentro de vogal"
    if letra.upper() in VOGAIS:  # upper transforma as letras em maisculo então todo o texto informado vai virar maisculo
        print(letra, end=" ")
else:
    print() #esse print so adiciona uma quebra de linha
    print("Executa quando acabar o laço")
