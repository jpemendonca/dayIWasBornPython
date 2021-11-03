# Calculadora do dia que nasceu e quantos ja viveu até hoje
# Importante escrever a data no formato (dd/mm/aaa)
# Ex: 18/06/1944
import datetime

semana = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']

data_quero = input('Digite o dia (dd/mm/aaa):  ')
data_formatada = datetime.datetime.strptime(data_quero, '%d/%m/%Y')
hoje = datetime.datetime.today()
delta = hoje - data_formatada

dia = 0

for x in semana:
    if semana.index(x) == data_formatada.weekday():
        dia = x

print(f'\nVoce nasceu num(a) {dia}\n')
print(f'Voce ja viveu {delta.days} dias até hoje')
