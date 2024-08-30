nome = "LuAn"

print(nome.upper())
print(nome.lower())
print(nome.title())


texto = " Olá mundo!  "

print(texto.strip())
print(texto.lstrip())
print(texto.rstrip())


menu = "Python"

print("####" + menu + "####")
print(menu.center(14, "#"))
print("-".join(menu))



#f-string pra aparecer só o tanto de casas que eu quero q seja imprimido
PI = 3.14159

print(f"O valor de PI: {PI:.2f}") # vai aparecer 3.14 somente
