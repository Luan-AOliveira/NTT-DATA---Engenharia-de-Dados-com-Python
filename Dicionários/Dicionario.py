# Criando dicionario tem essas duas maneiras
# Dicionario é imutavel e mutavel / somente a chave é imutavel o valor é mutavel
pessoa = {"nome": "Guilherme", "idade": 28}

pessoa = dict(nome="Guilherme", idade=28)



# Aqui o dicionario já criado e esta colocando mais dados dentro
pessoa["telefone"] = "3333-1234" # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)



# Acessando os dados dentro do dicionario
dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

dados["nome"]  # Guilherme
dados["idade"] # 28
dados["telefone"]  # 3333-1234

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

dados  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}
print(dados)



# Dicionários aninhados]
# Dentro do dicionario contatos a chave é o email e dentro dos emails foi criado outro dicionario
# onde as chaves são o nome e telefone 
# ai para recuperar o dado que você queira informa as duas chaves e ira retornar o valor necessario
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"}
}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # 3443-2121
print(telefone)



# Iterando dicionarios
# Percorre linha a linha do dicionario e faz retornar todas as chaves e valores
for chave, valor in contatos.items():
    print(chave, valor)

# guilherme@gmail.com {'nome': 'Guilherme', 'telefone': '3333-2221'}
# giovanna@gmail.com {'nome': 'Giovanna', 'telefone': '3443-2121'}
# chappie@gmail.com {'nome': 'Chappie', 'telefone': '3344-9871'}
# melaine@gmail.com {'nome': 'Melaine', 'telefone': '3333-7766'}   
