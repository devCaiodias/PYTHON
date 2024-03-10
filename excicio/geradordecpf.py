import random

nove_dijito = ''
for i in range(9):
    nove_dijito += str(random.randint(0,9))

contador_regresivo = 10


resultado_digito_1 = 0
for digito in nove_dijito:
    resultado_digito_1 += int(digito) * contador_regresivo
    contador_regresivo -= 1
    
digito_1 = (resultado_digito_1 * 10) % 11

if digito_1 >= 9:
    reltado = digito_1 = 0
    print(reltado)
else:
    print(digito_1)
    
dez_digito = nove_dijito + str(digito_1)
contador_regresivo_1 = 11

resultado_digito_2 = 0

for digito in dez_digito:
    resultado_digito_2 = int(digito) + contador_regresivo_1
    contador_regresivo_1 -= 1
    
digito_2 = (resultado_digito_2 * 10) % 11

if digito_2 <= 9:
    reltado_1 = digito_2 = 0
    print(reltado_1)
else:
    print(digito_2)
    
cpf_gerado_pelo_calculo = f'{nove_dijito}{digito_1}{digito_2}'

print(cpf_gerado_pelo_calculo)