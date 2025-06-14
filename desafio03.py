#Objetivo, calcular estatísticas básicas de um conjunto de dados.
#Crie um dicionário com valores de 30 produtos:
#Extraia para uma lista todos os valores com um loop
#Crie um arquivo separado com as funções para revolver para uma das solicitações:
#1. Calcule a média.
#2. Calcule a mediana.
#3. Calcule a moda.
#4. Calcule a variância.
#5. Calcule o desvio padrão.
#6. Calcule a amplitude.

from funcoes_estatisticas import 

produtos = {
    'produto1': 50, 'produto2': 65, 'produto3': 70,
    'produto4': 55, 'produto5': 80, 'produto6': 60,
    'produto7': 45, 'produto8': 90, 'produto9': 75,
    'produto10': 50, 'produto11': 65, 'produto12': 70,
    'produto13': 55, 'produto14': 80, 'produto15': 60,
    'produto16': 45, 'produto17': 90, 'produto18': 75,
    'produto19': 50, 'produto20': 65, 'produto21': 70,
    'produto22': 55, 'produto23': 80, 'produto24': 60,
    'produto25': 45, 'produto26': 90, 'produto27': 75,
    'produto28': 50, 'produto29': 65, 'produto30': 70
}

#Extrair valores para uma lista
valores = [valor for valor in produtos.values()]

#Calculando as estatísticas
print("Média:", calcular_media(valores))
print("Mediana:", calcular_mediana(valores))
print("Moda:", calcular_moda(valores))
print("Variância:", calcular_variancia(valores))
print("Desvio Padrão:", calcular_desvio_padrao(valores))
print("Amplitude:", calcular_amplitude(valores))

import statistics

def calcular_media(dados):
    return statistics.mean(dados)

def calcular_mediana(dados):
    return statistics.median(dados)

def calcular_moda(dados):
    try:
        return statistics.mode(dados)
    except statistics.StatisticsError:
        return "Não há moda única"

def calcular_variancia(dados):
    return statistics.variance(dados)

def calcular_desvio_padrao(dados):
    return statistics.stdev(dados)

def calcular_amplitude(dados):
    return max(dados) - min(dados)

# Perguntas 
#1. Qual é a diferença entre média e mediana?
#2. Por que a moda é importante?
#3. Qual é o significado da variância?
#4. Como o desvio padrão relaciona-se com a variância?

# Respostas
#1. Média é a soma de todos valores dividido pela quantidade de valores. Mediana é o valor do meio de todos os valores. 
#Exemplo: Média: (2+8)/10 = 1 
#Mediana: [1,2,3,4,5] - Três é a **MEDIANA**
#2. A moda é importante porque representa o valor que ocorre com maior frequência em um conjunto de dados, sendo útil para identificar tendências ou padrões.
#3. A variância mede a dispersão dos dados em relação à média, indicando o quão espalhados os valores estão. É calculada como a média dos quadrados das diferenças entre cada valor e a média.
#4. O desvio padrão é a raiz quadrada da variância. Ele também mede a dispersão dos dados, mas está na mesma unidade dos valores originais, tornando-o mais interpretável.

