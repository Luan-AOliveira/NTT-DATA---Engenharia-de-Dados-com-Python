curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"] # lista é sensitivo então tem que escrever exatamente igual
saques = [1500, 100]


# IN significa (esta) ele verifica se algo esta dentro de outra coisa
# como python esta dentro da variavel curso, portando deu verdadeiro
# NOT IN(não esta) Maçã não esta na variavel frutas, portanto deu verdadeiro
# e 200 não esta dentro da variavel saques, portanto da falso
print("Python" in curso)
print("maçã" not in frutas)
print(200 in saques)
