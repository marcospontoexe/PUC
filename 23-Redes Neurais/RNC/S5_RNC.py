# -*- coding: utf-8 -*-
#==============================================================================
# INTELIGÃŠNCIA ARTIFICIAL APLICADA
# REDES NEURAIS - SEMANA 5
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
# CARREGAMENTO DA BASE DE DADOS E SELEÃ‡ÃƒO DAS COLUNAS DE INTERESSE
#==============================================================================

# Carregar o conjunto de dados "base_veiculos.csv"
data = pd.read_csv('C:/RN/base_veiculos.csv')

# Extrair as colunas de interesse
columns = ['Cilindrada', 'Eficiencia']
data = data[columns]

#==============================================================================
# CONFIGURAÃ‡ÃƒO DA BASE DE DADOS
#==============================================================================

# Remover linhas com valores em branco ou zero
data = data.dropna()
data = data[(data != 0).all(axis=1)]

# Converter as colunas em arrays numpy
cilindrada = data['Cilindrada'].values
eficiencia = data['Eficiencia'].values

#------------------------------------------------------------------------------
# Concatenar os dados combinados em um Ãºnico array

# Cilindrada x EficiÃªncia
combinacao = np.column_stack((cilindrada, eficiencia))
inshape = combinacao.shape[1]

#==============================================================================
# CONFIGURAÃ‡ÃƒO DA ESTRUTURA DA REDE NEURAL COMPETITIVA
#==============================================================================

# DEFINA A QUANTIDADE DE NEURÃ”NIOS DA REDE
num_neur_rnc = 3

# DEFINA O NÃšMERO DE Ã‰POCAS PARA TREINAMENTO DA REDE
epocas_rnc = 5

# DEFINA A TAXA DE APRENDIZADO DA REDE
taxa_aprend_rnc = 0.3

#------------------------------------------------------------------------------
# CONFIGURE A ORDEM DO POLINÃ”MIO PARA REGRESSÃƒO LINEAR

# Ordem do PolinÃ´mio para RegressÃ£o cilindrada x efciÃªncia
ordem_pol = 5

#------------------------------------------------------------------------------
# INFORME OS PARÃ‚METROS PARA PREVISÃƒO

# Informe um valor de Cilindrada (em L) para prever a EficiÃªncia (em Km/L)
cilindrada_info = 1.0

#==============================================================================
# CRIAÃ‡ÃƒO DA REDE NEURAL COMPETITIVA
#==============================================================================

# CriaÃ§Ã£o da Rede Neural Competitiva 1
rnc = RNC(input_shape=inshape, num_neurons=num_neur_rnc)

#==============================================================================
# TREINAMENTO DA REDE NEURAL COMPETITIVA
#==============================================================================

# Treinamento da Rede Neural Competitiva 1
rnc.train(combinacao, learning_rate=taxa_aprend_rnc, num_epochs=epocas_rnc)

#==============================================================================
# REALIZAR PREDIÃ‡Ã•ES DA REDE NEURAL COMPETITIVA
#==============================================================================

# Realizar a prediÃ§Ã£o cilindrada x kmpl
predictions = rnc.predict(combinacao)

#==============================================================================
# CALCULAR OS POLINÃ”MIOS DAS REGRESSÃ•ES
#==============================================================================

# CÃ¡lculo do polinÃ´mio para Cilindrada X EficiÃªncia
coefficients = np.polyfit(cilindrada, eficiencia, ordem_pol)
polynomial = np.poly1d(coefficients)

#==============================================================================
# GERAR A TABELA DE AGRUPAMENTOS (CLUSTERS)
#==============================================================================

#------------------------------------------------------------------------------
# Tabela Cilindrada X EficiÃªncia

table_data = {'Cil.': cilindrada,
              'Efic.': eficiencia,
              'Group': predictions}

df_table = pd.DataFrame(table_data)

grouped_table = df_table.groupby('Group').agg({'Cil.': ['min', 'max'],
                                               'Efic.': ['min', 'max'],
                                               'Group': 'size'})

grouped_table.columns = ['Cil. (min)', 'Cil. (max)', 'Efic. (min)',
                          'Efic. (max)', 'Elementos']

# Formatar valores reais para duas casas decimais
grouped_table = grouped_table.round(decimals=2)

#==============================================================================
# REALIZAR AS PREVISÃ•ES DA REGRESSÃƒO
#==============================================================================

#------------------------------------------------------------------------------
# Prever o valor de EficiÃªncia correspondente a Cilindrada informada
previsao_y = polynomial(cilindrada_info)
previsao_y = '{:.2f}'.format(previsao_y)

#==============================================================================
# PLOTAR OS RESULTADOS EM GRÃFICOS DE DISPERSÃƒO
#==============================================================================

#------------------------------------------------------------------------------
# Cilindrada (L) X EficiÃªncia (Km/L)

# Obter os termos do polinÃ´mio formatados
terms = []

for i, coeff in enumerate(polynomial.coeffs):
    power = polynomial.order - i
    term = f"{coeff:.2f}x^{power}" if power > 1 else f"{coeff:.2f}x" if power == 1 else f"{coeff:.2f}"
    terms.append(term)

# Construir a string da funÃ§Ã£o f(x)
function_str = "f(x) = " + " + ".join(terms)

# Plotar o grÃ¡fico de dispersÃ£o
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(cilindrada, eficiencia, c=predictions)
ax.set_xlabel("Cilindrada (L)")
ax.set_ylabel("EficiÃªncia (Km/L)")
ax.set_title("Cilindrada X EficiÃªncia")
ax.set_xticks(np.arange(0, np.max(cilindrada) + 2, 1))
ax.set_xticklabels(['%.1f' % x for x in np.arange(0, np.max(cilindrada) + 2, 1)])
ax.grid(linestyle='dotted')

# Plotar a linha de regressÃ£o
x_values = np.linspace(np.min(cilindrada), np.max(cilindrada), 100)
y_values = polynomial(x_values)
ax.plot(x_values, y_values, color='red')

plt.show()

#==============================================================================
# APRESENTAR DAS TABELAS COM OS CLUSTERS
#==============================================================================

print('\n' + '=' * 70)
print('TABELA DE AGRUPAMENTO (CLUSTERS)')
print('=' * 70)
print('\n' * 1)

#------------------------------------------------------------------------------
# Tabela Cilindrada (L) X EficiÃªncia (Km/L)
print("Tabela 1. Cilindrada (L) X EficiÃªncia (Km/L)")
print('_' * 70)
print(grouped_table)
print('_' * 70)
print('\n' * 2)

#==============================================================================
# APRESENTAR AS PREVISÃ•ES DAS REGRESSÃ•ES
#==============================================================================

print('\n' + '=' * 70)
print('PREVISÃƒO DA REGRESSÃƒO')
print('=' * 70)
print('\n' * 1)

#------------------------------------------------------------------------------
# Imprimir resultados da funÃ§Ã£o f(x) para Cilindrada X EficiÃªncia
print('FunÃ§Ã£o polinomial para Cilindrada X EficiÃªncia')
print('_' * 70)
print(function_str + '\n')
print("Cilindrada informada:", cilindrada_info, "L")
print("EficiÃªncia prevista:", previsao_y, "Km/L")
print('_' * 70)
print('\n' * 1)

#==============================================================================