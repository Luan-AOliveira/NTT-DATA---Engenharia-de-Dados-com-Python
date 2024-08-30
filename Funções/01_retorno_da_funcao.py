def calcular_total(numeros):
  """Calcula a soma de todos os números em uma lista."""
  return sum(numeros)



def retorna_antecessor_e_sucessor(numero):
  """Retorna o antecessor e o sucessor de um número."""
  antecessor = numero - 1
  sucessor = numero + 1
  return antecessor, sucessor



def func_3():
    print("Olá mundo!")
    
    
    
# Exemplos de uso
print(calcular_total([10, 20, 34]))  # Imprime: 64
print(retorna_antecessor_e_sucessor(10))  # Imprime: (9, 11)
print(func_3()) # None
