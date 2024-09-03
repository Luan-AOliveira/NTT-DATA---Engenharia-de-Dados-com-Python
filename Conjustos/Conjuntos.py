# O (SET) serve para apagar objetos que estejam duplicados
set((1, 3, 1, 3, 4)) # {1, 2, 3, 4}
set("abacaxi") # {'b', 'a', 'c', 'x', 'i'}
set(("palio", "gol", "celta", "palio")) # {'gol', 'celta', 'palio'}

linguagens = {"python", "java", "python"}
print(linguagens)



# Acessando Dados / Converter o set em listas para acessar os dados
numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])



# Iterar/Contar Conjuntos 
carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
    


# União / Unir dois set
conjunto_a = {1, 2}
conjunto_b = {3, 4}

resultado = conjunto_a.union(conjunto_b)
print(resultado)



# Intersection / pega os objetos iguais de set diferentes
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.intersection(conjunto_b)
print(resultado)



# Difference / pega os objetos que não se repetem em diferentes set separadamente
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b)
print(resultado)

resultado = conjunto_b.difference(conjunto_a)
print(resultado)



# Symmetric Difference / pega os objetos que não se repetem de diferentes set e imprimi juntos
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado)



# Issubset / ele verifica se um conjunto é um subconjunto de outro por exemplo conjunto A é subconunto do B
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b)  # True
print(resultado)

resultado = conjunto_b.issubset(conjunto_a)  # False
print(resultado)



# Issuperset /  Ele é utilizado para determinar se um conjunto 
# contém todos os elementos de outro conjunto, ou seja, se ele é um superconjunto.
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  # False
print(resultado)

resultado = conjunto_b.issuperset(conjunto_a)  # True
print(resultado)



# Isdisjoint / é utilizado para verificar se dois conjuntos não possuem elementos em comum. 
# Em outras palavras, ele determina se dois conjuntos são disjuntos.
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b)  # True
print(resultado)

resultado = conjunto_a.isdisjoint(conjunto_c)  # False
print(resultado)



# Add / é utilizado para adicionar um elemento a um conjunto
sorteio = {1, 23}

sorteio.add(25)  # {1, 23, 25}
print(sorteio)

sorteio.add(42)  # {1, 23, 25, 42}
print(sorteio)

sorteio.add(25)  # {1, 23, 25, 42}
print(sorteio)



# Clear / é utilizado para remover todos os elementos de um conjunto
sorteio = {1, 23}

print(sorteio)  # {1,23}

sorteio.clear()

print(sorteio)  # {}



# Copy / é utilizado para criar uma cópia independente de um conjunto
sorteio = {1, 23}

print(sorteio)  # {1, 23}

sorteio.copy()

print(sorteio)  # {1, 23}



# Discard / é utilizado para remover um elemento específico de um conjunto. Ao contrário do método remove(), 
# o discard() não gera um erro se o elemento que você tentar remover não estiver presente no conjunto
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1)
numeros.discard(45)

print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9, 0}



# Pop / quando aplicado a conjuntos, tem um comportamento um pouco diferente de quando utilizado com listas. 
# Ao invés de remover um elemento por índice (como em listas), 
# o pop() em conjuntos remove e retorna um elemento aleatório do conjunto.
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.pop())  # 0
print(numeros.pop())  # 1
print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9}



# Remove / é utilizado para remover um elemento específico de um conjunto
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.remove(0))  # 0
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}



# Len / é uma função built-in que retorna o número de elementos presentes em um objeto iterável
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(len(numeros))  # 10



#In / é uma ferramenta poderosa para verificar se um determinado elemento está presente em uma sequência
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(1 in numeros)  # True
print(10 in numeros)  # False
