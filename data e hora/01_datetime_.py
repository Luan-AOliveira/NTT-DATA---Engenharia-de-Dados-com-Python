# Arquivo: manipula_datas.py
from datetime import date, datetime, time

# date
data = date(2023, 7, 19)
print(data)


# today retorna a data local atual
hoje = date.today() 
print("Hoje é dia:", hoje)


# datetime
data_hora = datetime(2023, 7, 19, 10, 30, 20)
print("A data e hora do saque foi realizado em: ", data_hora)
print(datetime.today())


# time
hora = time(10, 20, 0)
print(hora)
