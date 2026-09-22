# -*- coding: utf-8 -*-
#==============================================================================
# INTELIGÃŠNCIA ARTIFICIAL APLICADA
# REDES NEURAIS - SEMANA 7
# REDE NEURAL COMPETITIVA (RNC)
# PROF. EDSON RUSCHEL
#==============================================================================

#==============================================================================
# IMPORTAÃ‡ÃƒO DE BIBLIOTECAS
#==============================================================================
import pandas as pd
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt

#==============================================================================
# CRIAÃ‡ÃƒO DA CLASSE PARA REDE NEURAL COMPETITIVA (RNC)
#==============================================================================
class RNC:
    def __init__(self, input_shape, num_neurons):
        self.input_shape = input_shape
        self.num_neurons = num_neurons
        self.weights = np.random.rand(num_neurons, input_shape)
    
    def train(self, input_data, learning_rate=0.1, num_epochs=5):
        progress_bar = tqdm(total=num_epochs, desc='Treinando', unit=' Ã©pocas', ncols=80)
        for epoch in range(num_epochs):
            for input_sample in input_data:
                winner_neuron = self.get_winner_neuron(input_sample)
                self.update_weights(input_sample, winner_neuron, learning_rate)
            progress_bar.set_postfix(epoch=epoch+1)
            progress_bar.update()
        progress_bar.close()
    
    def get_winner_neuron(self, input_sample):
        distances = np.linalg.norm(input_sample - self.weights, axis=1)
        return np.argmin(distances)
    
    def update_weights(self, input_sample, winner_neuron, learning_rate):
        self.weights[winner_neuron] += learning_rate * (input_sample - self.weights[winner_neuron])
        
    def predict(self, input_data):
        predictions = []
        for input_sample in input_data:
            winner_neuron = self.get_winner_neuron(input_sample)
            predictions.append(winner_neuron)
        return predictions

#==============================================================================
# CONFIGURAÃ‡ÃƒO DA BASE DE DADOS
#==============================================================================

# Carregar o conjunto de dados "vehicle_fuel_economy.csv"
data = pd.read_csv('C:/RN/base_veiculos_1.csv')

# Extrair as colunas de interesse
columns = ['Cilindrada', 'Eficiencia', 'CO2']
data = data[columns]

# Remover linhas com valores em branco ou zero
data = data.dropna()
data = data[(data != 0).all(axis=1)]

# Converter as colunas em arrays numpy
cilindrada = data['Cilindrada'].values
eficiencia = data['Eficiencia'].values
co2 = data['CO2'].values

#------------------------------------------------------------------------------
# Concatenar os dados combinados em um Ãºnico array

# Cilindrada x EficiÃªncia
combinacao1 = np.column_stack((cilindrada, eficiencia))
inshape1 = combinacao1.shape[1]

# Cilindrada x CO2
combinacao2 = np.column_stack((cilindrada, co2))
inshape2 = combinacao2.shape[1]

#==============================================================================
# CONFIGURAÃ‡ÃƒO DA ESTRUTURA DA REDE NEURAL COMPETITIVA
#==============================================================================

# DEFINA A QUANTIDADE DE NEURÃ”NIOS DAS REDES
num_neur_rnc1 = 3
num_neur_rnc2 = 10

# DEFINA O NÃšMERO DE Ã‰POCAS PARA TREINAMENTO DAS REDES
epocas_rnc1 = 10
epocas_rnc2 = 10

# DEFINA A TAXA DE APRENDIZADO DAS REDES
taxa_aprend_rnc1 = 0.3
taxa_aprend_rnc2 = 0.5

#------------------------------------------------------------------------------
# CONFIGURE A ORDEM DE CADA POLINÃ”MIO PARA REGRESSÃƒO LINEAR

# Ordem do PolinÃ´mio para RegressÃ£o Cilindrada X EficiÃªncia
ordem_pol1 = 7

# Ordem do PolinÃ´mio para RegressÃ£o Cilindrada X CO2
ordem_pol2 = 5

#------------------------------------------------------------------------------
# INFORME OS PARÃ‚METROS PARA PREVISÃƒO

# Informe um valor de Cilindrada (em L) para prever a EficiÃªncia (em Km/L)
cilindrada1_info = 1.8

# Informe um valor de Cilindrada (em L) para prever a EmissÃ£o de CO2 (em g/Km)
cilindrada2_info = 8.2

#==============================================================================
# CRIAÃ‡ÃƒO DA REDE NEURAL COMPETITIVA
#==============================================================================

# CriaÃ§Ã£o da Rede Neural Competitiva 1
rnc1 = RNC(input_shape=inshape1, num_neurons=num_neur_rnc1)

# CriaÃ§Ã£o da Rede Neural Competitiva 2
rnc2 = RNC(input_shape=inshape2, num_neurons=num_neur_rnc2)

#==============================================================================
# TREINAMENTO DA REDE NEURAL COMPETITIVA
#==============================================================================

# Treinamento da Rede Neural Competitiva 1
rnc1.train(combinacao1, learning_rate=taxa_aprend_rnc1, num_epochs=epocas_rnc1)

# Treinamento da Rede Neural Competitiva 2
rnc2.train(combinacao2, learning_rate=taxa_aprend_rnc2, num_epochs=epocas_rnc2)

#==============================================================================
# REALIZAR PREDIÃ‡Ã•ES DA REDE NEURAL COMPETITIVA
#==============================================================================

# Realizar a prediÃ§Ã£o cilindrada x kmpl
predictions1 = rnc1.predict(combinacao1)

# Realizar a prediÃ§Ã£o cilindrada x co2
predictions2 = rnc2.predict(combinacao2)

#==============================================================================
# CALCULAR OS POLINÃ”MIOS DAS REGRESSÃ•ES
#==============================================================================

# CÃ¡lculo do polinÃ´mio para Cilindrada X EficiÃªncia
coefficients1 = np.polyfit(cilindrada, eficiencia, ordem_pol1)
polynomial1 = np.poly1d(coefficients1)

# CÃ¡lculo do polinÃ´mio para Cilindrada X EmissÃ£o de CO2
coefficients2 = np.polyfit(cilindrada, co2, ordem_pol2)
polynomial2 = np.poly1d(coefficients2)

#==============================================================================
# GERAR AS TABELAS DE AGRUPAMENTOS (CLUSTERS)
#==============================================================================

#------------------------------------------------------------------------------
# Tabela Cilindrada vs. EficiÃªncia

table_data1 = {'Cil.': cilindrada,
              'Efic.': eficiencia,
              'Group': predictions1}

df_table1 = pd.DataFrame(table_data1)

grouped_table1 = df_table1.groupby('Group').agg({'Cil.': ['min', 'max'],
                                               'Efic.': ['min', 'max'],
                                               'Group': 'size'})

grouped_table1.columns = ['Cil. (min)', 'Cil. (max)', 'Efic. (min)',
                          'Efic. (max)', 'Elementos']

# Formatar valores reais para duas casas decimais
grouped_table1 = grouped_table1.round(decimals=2)

#------------------------------------------------------------------------------
# Tabela Cilindrada vs. EmissÃ£o de CO2

table_data2 = {'Cil.': cilindrada,
              'CO2': co2,
              'Group': predictions2}

df_table2 = pd.DataFrame(table_data2)

grouped_table2 = df_table2.groupby('Group').agg({'Cil.': ['min', 'max'],
                                               'CO2': ['min', 'max'],
                                               'Group': 'size'})

grouped_table2.columns = ['Cil. (min)', 'Cil. (max)',
                         'CO2 (min)', 'CO2 (max)', 'Elementos']

# Formatar valores reais para duas casas decimais
grouped_table2 = grouped_table2.round(decimals=2)

#==============================================================================
# REALIZAR AS PREVISÃ•ES DA REGRESSÃƒO
#==============================================================================

#------------------------------------------------------------------------------
# Prever o valor de EficiÃªncia correspondente a Cilindrada informada
previsao_y1 = polynomial1(cilindrada1_info)
previsao_y1 = '{:.2f}'.format(previsao_y1)

#------------------------------------------------------------------------------
# Prever o valor de EmissÃ£o de CO2 correspondente a Cilindrada informada
previsao_y2 = polynomial2(cilindrada2_info)
previsao_y2 = '{:.2f}'.format(previsao_y2)

#==============================================================================
# PLOTAR OS RESULTADOS EM GRÃFICOS DE DISPERSÃƒO
#==============================================================================

#------------------------------------------------------------------------------
# Cilindrada (L) X EficiÃªncia (Km/L)

# Obter os termos do polinÃ´mio formatados
terms1 = []

for i, coeff in enumerate(polynomial1.coeffs):
    power1 = polynomial1.order - i
    term1 = f"{coeff:.2f}x^{power1}" if power1 > 1 else f"{coeff:.2f}x" if power1 == 1 else f"{coeff:.2f}"
    terms1.append(term1)

# Construir a string da funÃ§Ã£o f(x)
function_str1 = "f(x) = " + " + ".join(terms1)

# Plotar o grÃ¡fico de dispersÃ£o
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(cilindrada, eficiencia, c=predictions1)
ax.set_xlabel("Cilindrada (L)")
ax.set_ylabel("EficiÃªncia (Km/L)")
ax.set_title("Cilindrada X EficiÃªncia")
ax.set_xticks(np.arange(0, np.max(cilindrada) + 2, 2))
ax.set_xticklabels(['%.1f' % x for x in np.arange(0, np.max(cilindrada) + 2, 2)])
ax.grid(linestyle='dotted')

# Plotar a linha de regressÃ£o
x_values = np.linspace(np.min(cilindrada), np.max(cilindrada), 100)
y_values = polynomial1(x_values)
ax.plot(x_values, y_values, color='red')

plt.show()

#------------------------------------------------------------------------------
# Cilindrada (L) X EmissÃ£o de CO2 (g/Km)

# Obter os termos do polinÃ´mio formatados
terms2 = []

for i, coeff in enumerate(polynomial2.coeffs):
    power2 = polynomial2.order - i
    term2 = f"{coeff:.2f}x^{power2}" if power2 > 1 else f"{coeff:.2f}x" if power2 == 1 else f"{coeff:.2f}"
    terms2.append(term2)

# Construir a string da funÃ§Ã£o f(x)
function_str2 = "f(x) = " + " + ".join(terms2)

# Plotar o grÃ¡fico de dispersÃ£o
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(cilindrada, co2, c=predictions2)
ax.set_xlabel("Cilindrada (L)")
ax.set_ylabel("EmissÃ£o de CO2 (g/Km)")
ax.set_title("Cilindrada X EmissÃ£o de CO2")
ax.set_xticks(np.arange(0, np.max(cilindrada) + 2, 2))
ax.set_xticklabels(['%.1f' % x for x in np.arange(0, np.max(cilindrada) + 2, 2)])
ax.grid(linestyle='dotted')

# Plotar a linha de regressÃ£o
x_values = np.linspace(np.min(cilindrada), np.max(cilindrada), 100)
y_values = polynomial2(x_values)
ax.plot(x_values, y_values, color='red')

plt.show()

#==============================================================================
# APRESENTAR DAS TABELAS COM OS CLUSTERS
#==============================================================================

print('\n' + '=' * 70)
print('TABELAS DE AGRUPAMENTO (CLUSTERS)')
print('=' * 70)
print('\n' * 1)

#------------------------------------------------------------------------------
# Tabela Cilindrada (L) vs. EficiÃªncia (Km/L)
print("Tabela 1. Cilindrada (L) X EficiÃªncia (Km/L)")
print('_' * 70)
print(grouped_table1)
print('_' * 70)
print('\n' * 2)
#------------------------------------------------------------------------------
# Tabela Cilindrada (L) vs. EmissÃ£o de CO2 (g/Km)
print("Tabela 2. Cilindrada (L) X EmissÃ£o de CO2 (g/Km)")
print('_' * 70)
print(grouped_table2)
print('_' * 70)
print('\n' * 2)

#==============================================================================
# APRESENTAR AS PREVISÃ•ES DAS REGRESSÃ•ES
#==============================================================================

print('\n' + '=' * 70)
print('PREVISÃ•ES DAS REGRESSÃ•ES')
print('=' * 70)
print('\n' * 1)

#------------------------------------------------------------------------------
# Imprimir resultados da funÃ§Ã£o f(x) para Cilindrada vs. EficiÃªncia
print('FunÃ§Ã£o polinomial para Cilindrada X EficiÃªncia')
print('_' * 70)
print(function_str1 + '\n')
print("Cilindrada informada:", cilindrada1_info, "L")
print("EficiÃªncia prevista:", previsao_y1, "Km/L")
print('_' * 70)
print('\n' * 1)

# Imprimir resultados da funÃ§Ã£o f(x) para Cilindrada vs. EmissÃ£o de CO2
print('FunÃ§Ã£o polinomial para Cilindrada X EmissÃ£o de CO2')
print('_' * 70)
print(function_str2 + '\n')
print("Cilindrada informada:", cilindrada2_info, "L")
print("EmissÃ£o de CO2 prevista:", previsao_y2, "g/Km")
print('_' * 70)
print('\n' * 1)
#==============================================================================