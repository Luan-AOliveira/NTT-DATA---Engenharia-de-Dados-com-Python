frutas = ["laranja", "maca", "uva"]
print(frutas)


frutas = []
print(frutas)


letras = list("python")
print(letras)


numeros = list(range(10))
print(numeros)


carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)


frutas = ["maça", "laranja", "uva", "pera"]
print(frutas[0])
print(frutas[1])


frutas = ["maça", "laranja", "uva", "pera"] # Se quiser pegar o ultimo elemento da lista
print(frutas[-1]) # So colocar -1 ai começa a contar de trás pra frente
print(frutas[-3]) # E começa a contar a partir do -1



# Código copiado
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

# Acessando elementos da matriz
print(matriz[0])  # Imprime [1, "a", 2] (primeira linha)
print(matriz[0][0])  # Imprime 1 (primeiro elemento da primeira linha)
print(matriz[-1][-1])  # Imprime "c" (último elemento da última linha)



lista = ["p", "y", "t", "h", "o", "n"]

lista[2:]  # ["t", "h", "o", "n"]
lista[:2]  # ["p", "y"]
lista[1:3] # ["y", "t"]
lista[0:3:2] # ["p", "t"]
lista[:]  # ["p", "y", "t", "h", "o", "n"]
lista[::-1] # ["n", "o", "h", "t", "y", "p"]



# Buscando um elemento dentro da lista
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)
    

# Este mostra os elementos da lista e inumera eles 
carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")



# Este codigo retorna todos os números pares da lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)



# Este código faz todos os números da lista serem elevados ao quadrado
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
print(quadrado)



# Metodos da classe list (APPREND) serve para adicionar um valor dentro da lista
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)  # Saída: [1, "Python", [40, 30, 20]]



# Metodos da classe list (CLEAR) serve para limpar totalmente a lista
lista = [1, "Python", [40, 30, 20]]
print(lista)  # Saída: [1, "Python", [40, 30, 20]]
lista.clear()
print(lista)  # Saída: []



# Metodos da classe list (COPY) serve para copiar uma outra lista porém são objetos diferentes
lista = [1, "Python", [40, 30, 20]]
nova_lista = lista.copy()  # Cria uma cópia da lista original

print(lista)  # Imprime a lista original
print(nova_lista)  # Imprime a cópia da lista



# Metodos da classe list (COUNT) ele conta quantas vezes a mesma coisa se repetiu na lista
cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))  # Saída: 1
print(cores.count("azul"))     # Saída: 2
print(cores.count("verde"))    # Saída: 1
# Neste exemplo, o código conta quantos votos o candidato A recebeu
votos = ["candidato_A", "candidato_B", "candidato_A", "candidato_C"]
votos_candidato_A = votos.count("candidato_A")
print("O candidato A recebeu", votos_candidato_A, "votos.")



# Metodos da classe list (EXTEND) ele junta duas listas / Ele não elimina elementos duplicados
# Nas duas listas que iram juntar
linguagens = ["python", "js", "c"]
print(linguagens)  # Saída: ['python', 'js', 'c']

linguagens.extend(["java", "csharp"])
print(linguagens)  # Saída: ['python', 'js', 'c', 'java', 'csharp']
#
frutas = ["maçã", "banana"]
novas_frutas = ["laranja", "uva"]
frutas.extend(novas_frutas)
print(frutas)  # Saída: ['maçã', 'banana', 'laranja', 'uva']



# Metodos da classe list (INDEX) ele mostra em que posição da lista esta o objeto informado
linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))  # Saída: 3
print(linguagens.index("python"))  # Saída: 0
#
frutas = ["maçã", "banana", "laranja"]
indice_banana = frutas.index("banana")
print("A banana está na posição:", indice_banana)  # Saída: A banana está na posição: 1



# Metodos da classe list (POP) ele retira o ultimo elemento da lista ou o que você informar a posição
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.pop()  # Remove e retorna o último elemento: 'csharp'
linguagens.pop()  # Remove e retorna o último elemento (agora 'java'): 'java'
linguagens.pop()  # Remove e retorna o último elemento (agora 'c'): 'c'
linguagens.pop(0)  # Remove e retorna o elemento na posição 0: 'python'
#
frutas = ["maçã", "banana", "laranja"]
ultima_fruta = frutas.pop(1)
print("A última fruta removida foi:", ultima_fruta)  
print("A fruta removida foi a:", ultima_fruta)



# Metodos da classe list (REMOVE) ele remove um objeto da lista porém este so tira escrevendo o objeto
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.remove("c")
print(linguagens)  # Saída: ['python', 'js', 'java', 'csharp']
#
frutas = ["maçã", "banana", "laranja", "maçã"]
frutas.remove("maçã")
print(frutas)  # Saída: ['banana', 'laranja', 'maçã']



# Metodos da classe list (REVERSE) ele inverte a lista coloca ao contrario
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.reverse()
print(linguagens)  # Saída: ['csharp', 'java', 'c', 'js', 'python']
#
numeros = [1, 2, 3, 4, 5]
numeros.reverse()
print(numeros)  # Saída: [5, 4, 3, 2, 1]



# Metodos da classe list (SORT) ele serve para ordenar a lista em forma alfabetica
linguagens = ["python", "js", "c", "java", "csharp"]

# Ordenação alfabética crescente (padrão)
linguagens.sort()
print(linguagens)  # Saída: ['c', 'csharp', 'java', 'js', 'python']

# Ordenação alfabética decrescente
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)
print(linguagens)  # Saída: ['python', 'js', 'java', 'csharp', 'c']

# Ordenação por tamanho da palavra (crescente)
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))
print(linguagens)  # Saída: ['c', 'js', 'java', 'python', 'csharp']

# Ordenação por tamanho da palavra (decrescente)
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)  # Saída: ['python', 'csharp', 'java', 'js', 'c']



# Metodos da classe list (LEN) ele conta quantos objetos a dentro da lista
linguagens = ["python", "js", "c", "java", "csharp"]
print(len(linguagens))  # Saída: 5
#
minha_lista = [1, 2, 3, 4, 5]
tamanho_lista = len(minha_lista)
print(tamanho_lista)  # Saída: 5



# Metodos da classe list (SORTED) ele faz o mesmo que o (SORT) de ordenar a em ordem alfabetica
# Porém aqui usada como uma função
linguagens = ["python", "js", "c", "java", "csharp"]

# Ordenação por comprimento da string (crescente)
print(sorted(linguagens, key=lambda x: len(x)))  # Saída: ['c', 'js', 'java', 'python', 'csharp']

# Ordenação por comprimento da string (decrescente)
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # Saída: ['python', 'csharp', 'java', 'js', 'c']
#
palavras = ["casa", "carro", "elefante", "bola"]
palavras_ordenadas_por_tamanho = sorted(palavras, key=lambda x: len(x))
print(palavras_ordenadas_por_tamanho)  # Saída: ['c', 'js', 'java', 'python', 'csharp']
