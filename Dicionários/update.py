# Ele atualiza o nosso dicionario com outro dicionario

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}


# Se usar o update com uma chave que já existe atualiza e modifica o que já existe
contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contatos)  # {'guilherme@gmail.com': {'nome': 'Gui'}}


# Porém se não existir essa chave no dicionario, ele somente agrega o que foi adicionado
contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)
