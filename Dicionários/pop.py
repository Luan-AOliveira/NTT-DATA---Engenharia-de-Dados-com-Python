# Ele remove uma chave do dicionario

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)


# Se não encontrar a chave retorna algo que você escrever depois da ,
resultado = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado)
