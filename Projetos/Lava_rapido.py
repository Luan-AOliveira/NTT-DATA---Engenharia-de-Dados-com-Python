# Sistema de um lava-rápido
# Sistema que calcula a hora que carro entrou e baseado no tamanho do carro que horas ele ficara pronto
from datetime import timedelta, datetime, time, date

tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now() #datetime e now vão pegar a data e hora e região do mundo atual do pc 


infome_tamanho = input("Informe o tamanho do seu carro com P, M ou G: ")
if infome_tamanho in ["P", "M", "G"]:
    # Calcula a data estimada de conclusão
    if infome_tamanho == "P":
        data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    elif infome_tamanho == "M":
        data_estimada = data_atual + timedelta(minutes=tempo_medio)
    else:
        data_estimada = data_atual + timedelta(minutes=tempo_grande)

    # Imprime o resultado
    print(f"O carro chegou às: {data_atual:%d/%m/%Y às %H:%M} e ficará pronto às: {data_estimada:%d/%m/%Y às %H:%M}")
else:
    print("Tamanho de carro inválido. Por favor, informe P, M ou G.")