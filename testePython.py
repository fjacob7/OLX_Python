import pandas as pd

df = pd.read_json('Funcionarios-1M.json', typ='series')

# QUESTÃO 1

salario_global = []
for i in range(len(df[1])):
    salario_global.append(df[1][i]['salario'])
	
salario_max_global = df[1][salario_global.index(max(salario_global))]['salario']
nome_max_global = df[1][salario_global.index(max(salario_global))]['nome']
sobrenome_max_global = df[1][salario_global.index(max(salario_global))]['sobrenome']
print("global_max|{} {}|{}".format(nome_max_global,sobrenome_max_global,salario_max_global))

salario_min_global = df[1][salario_global.index(min(salario_global))]['salario']
nome_min_global = df[1][salario_global.index(min(salario_global))]['nome']
sobrenome_min_global = df[1][salario_global.index(min(salario_global))]['sobrenome']
print("global_min|{} {}|{}".format(nome_min_global,sobrenome_min_global,salario_min_global))

media_global = round(sum(salario_global) / len(salario_global),2)
print("global_avg|{}".format(media_global))

# QUESTÃO 2

area_global = []
for i in range(len(df[1])):
    area_global.append(df[1][i]['area'])
	
codigo_area, nome_area = [],[]
for i in range(len(df[0])):
    if df[0][i]['codigo'] in area_global:
        codigo_area.append(df[0][i]['codigo'])
        nome_area.append(df[0][i]['nome'])
		
salario_area, salario_parcial = [],[]
for i in range(len(codigo_area)):
    for j in range(len(df[1])):
        if df[1][j]['area'] == codigo_area[i]:
            salario_parcial.append(df[1][j]['salario'])
    salario_area.append(salario_parcial)
    salario_parcial = []
	
for i in range(len(codigo_area)):
    salario_max_area = df[1][salario_global.index(max(salario_area[i]))]['salario']
    nome_max_area = df[1][salario_global.index(max(salario_area[i]))]['nome']
    sobrenome_max_area = df[1][salario_global.index(max(salario_area[i]))]['sobrenome']
    print("area_max|{}|{} {}|{}".format(nome_area[i],nome_max_area,sobrenome_max_area,salario_max_area))
	
for i in range(len(codigo_area)):
    salario_min_area = df[1][salario_global.index(min(salario_area[i]))]['salario']
    nome_min_area = df[1][salario_global.index(min(salario_area[i]))]['nome']
    sobrenome_min_area = df[1][salario_global.index(min(salario_area[i]))]['sobrenome']
    print("area_min|{}|{} {}|{}".format(nome_area[i],nome_min_area,sobrenome_min_area,salario_min_area))
	
for i in range(len(codigo_area)):
    media_area = round(sum(salario_area[i]) / len(salario_area[i]),2)
    print("area_avg|{}|{}".format(nome_area[i],media_area))
	
# QUESTÃO 3

codigo_quantidade = []
for i in range(len(df[0])):
    codigo_quantidade.append(area_global.count(df[0][i]['codigo']))
	
nome_max_quantidade = df[0][codigo_quantidade.index(max(codigo_quantidade))]['nome']
quantidade_max = max(codigo_quantidade)
print("most_employees|{}|{}".format(nome_max_quantidade,quantidade_max))

for i in range(len(codigo_quantidade)):
    if i >= codigo_quantidade.index(min(codigo_quantidade)):
        nome_min_quantidade = df[0][codigo_quantidade.index(min(codigo_quantidade),i)]['nome']
        quantidade_min = min(codigo_quantidade)
        print("least_employees|{}|{}".format(nome_min_quantidade,quantidade_min))
		
# QUESTÃO 4

sobrenome_geral = []
for i in range(len(df[1])):
    sobrenome_geral.append(df[1][i]['sobrenome'])
	
sobrenome_especifico = []
for i in range(len(df[1])):
    if sobrenome_geral[i] not in sobrenome_especifico:
        sobrenome_especifico.append(sobrenome_geral[i])
		
sobrenome_quantidade = []
for i in range(len(sobrenome_especifico)):
    sobrenome_quantidade.append(sobrenome_geral.count(sobrenome_especifico[i]))
	
if min(sobrenome_quantidade) > 1:
    salario_max_sobrenome = df[1][salario_global.index(max(salario_global))]['salario']
    nome_max_sobrenome = df[1][salario_global.index(max(salario_global))]['nome']
    sobrenome_max_sobrenome = df[1][salario_global.index(max(salario_global))]['sobrenome']
    print("last_name_max|{}|{} {}|{}".format(sobrenome_max_sobrenome,nome_max_sobrenome,sobrenome_max_sobrenome,salario_max_sobrenome))