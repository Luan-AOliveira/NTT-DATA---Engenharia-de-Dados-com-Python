# O (,) no final do código e o () significa que é uma tupla e não uma lista
# A tupla não é possivel mudar os dados dentro dela enquanto as listas são possiveis
frutas = ("laranja", "pera", "uva")
letras = tuple("python")
numeros = tuple([1, 2, 3, 4]) # esta passando uma lista dentro de uma tupla ai a lista não podera ser alterada
pais = ("Brasil",)


# Imprimindo os elementos das tuplas
print(frutas)
print(letras)
print(numeros)
print(pais)



# Para acessar os dados da tupla é igual aos da lista
frutas = ("maçã", "laranja", "uva", "pera")
print(frutas[0])  # Acessando o primeiro elemento (índice 0)
print(frutas[-2])  # Acessando o terceiro elemento (índice -2)



# Tuplas aninhadas / matriz
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c")
)

print(matriz[0])  # Imprime: (1, 'a', 2)
print(matriz[0][0])  # Imprime: 1
print(matriz[0][-1])  # Imprime: 2
print(matriz[-1][-1])  # Imprime: c



# Fatiamento
tupla = ("p", "y", "t", "h", "o", "n")

tupla[2:]  # ('t', 'h', 'o', 'n')
tupla[:2]  # ('p', 'y')
tupla[1:3]  # ('y', 't')
tupla[0:3:2]  # ('p', 't')
tupla[:]  # ('p', 'y', 't', 'h', 'o', 'n')
tupla[::-1]  # ('n', 'o', 'h', 't', 'y', 'p')



# Iterar
carros = ("gol", "celta", "palio")

for carro in carros:
    print(carro)
#
carros = ("gol", "celta", "palio")

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")



# Metodos da classe tuplas (COUNT) contando quantos elementos tem dentro da tupla
cores = ("vermelho", "azul", "verde", "azul")

print(cores.count("vermelho"))  # Imprime: 1
print(cores.count("azul"))      # Imprime: 2
print(cores.count("verde"))    # Imprime: 1



# Metodos da classe tuplas (INDEX) mostra a posição do objeto dentro da tupla
linguagens = ("python", "js", "c", "java", "csharp")

print(linguagens.index("java"))
print(linguagens.index("python"))



# Metodos da classe tuplas (LEN) conta quantos objetos a dentro das tuplas
linguagens = ("python", "js", "c", "java", "csharp")
print(len(linguagens))
