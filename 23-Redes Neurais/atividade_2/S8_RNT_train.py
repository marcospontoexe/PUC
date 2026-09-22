# -*- coding: utf-8 -*-
#==============================================================================
# INTELIGÃŠNCIA ARTIFICIAL APLICADA
# REDES NEURAIS - SEMANA 8
# REDE NEURAL TEMPORAL (RNT) PARA TREINAMENTO
# PROF. EDSON RUSCHEL
#==============================================================================

#==============================================================================
# IMPORTAÃ‡ÃƒO DE BIBLIOTECAS
#==============================================================================
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

#==============================================================================
# CONFIGURAÃ‡ÃƒO DO ENDEREÃ‡O DOS ARQUIVOS
#==============================================================================

# INSIRA O CAMINHO DOS ARQUIVOS DE TREINAMENTO E TESTE
# 'C:\RN\dolar_treinamento.csv' e 'C:\RN\dolar_teste.csv'

arquivo_treinamento = 'C:\RN\dolar_treinamento_2.csv'

#==============================================================================
# DEFINA A JANELA DE PREVISÃƒO PARA A REDE NEURAL TEMPORAL
#==============================================================================

janela_prev = 50

#==============================================================================
# DEFINA A FUNÃ‡ÃƒO DE PERDA (FUNÃ‡ÃƒO CUSTO) E O OTIMIZADOR
#==============================================================================

# -----------------------------------------------------------------------------
# mean_squared_error
# mean_absolute_error
# categorical_crossentropy
# binary_crossentropy

funcao_perda = 'mean_squared_error'

# -----------------------------------------------------------------------------
# sgd
# adam
# RMSprop

otimizador = 'RMSprop'

#==============================================================================
# DEFINA O NÃšMERO DE NEURÃ”NIOS DA CAMADA LSTM E DA CAMADA DENSA
#==============================================================================

# Quantidade de neurÃ´nios da Camada LSTM
neuronios_LSTM = 4

# Quantidade de neurÃ´nios da Camada Densa
# Precisa ser 1: esta e a camada de saida, e o alvo e um unico numero (a cotacao
# do dia seguinte). Com qualquer valor maior o Keras aborta por incompatibilidade
# entre a forma da saida e a do alvo.
neuronios_densa = 1

#==============================================================================
# DEFINA O NÃšMERO DE Ã‰POCAS E O TAMANHO DO LOTE DE TREINAMENTO PARA CADA Ã‰POCA
#==============================================================================

epocas = 50

lote = 32

#==============================================================================
# CARREGAMENTO E PREPROCESSAMENTO DOS DADOS
#==============================================================================

# Ler os arquivos CSV de treinamento e teste
train_df = pd.read_csv(arquivo_treinamento)

# Filtrar apenas a coluna 'Valor' nos dados de treinamento e teste
train_data = train_df[['Dolar']].values

# Normalizar os dados de treinamento entre 0 e 1
scaler = MinMaxScaler(feature_range=(0, 1))
train_data_scaled = scaler.fit_transform(train_data)

#==============================================================================
# PREPROCESSAMENTO DO CONJUNTO DE DADOS DE ACORDO COM A JANELA DE TEMPO
#==============================================================================

# FunÃ§Ã£o auxiliar para criar os conjuntos de dados com base na janela de tempo
def create_dataset(dataset, window_size=1):
    X, Y = [], []
    for i in range(len(dataset) - window_size):
        window = dataset[i:(i + window_size), 0]
        X.append(window)
        Y.append(dataset[i + window_size, 0])
    return np.array(X), np.array(Y)

# Criar os conjuntos de treinamento
X_train, y_train = create_dataset(train_data_scaled, janela_prev)

# Reshape dos dados para o formato esperado pela LSTM [amostras, janela de tempo, caracterÃ­sticas]
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

#==============================================================================
# CRIAÃ‡ÃƒO DO MODELO DA REDE NEURAL TEMPORAL
#==============================================================================

# Criar o modelo da rede neural
model = Sequential()
model.add(LSTM(neuronios_LSTM, input_shape=(janela_prev, 1)))
model.add(Dense(neuronios_densa))
model.compile(loss=funcao_perda, optimizer=otimizador)

#==============================================================================
# TREINAMENTO DA REDE NEURAL TEMPORAL
#==============================================================================
# Treinar o modelo
model.fit(X_train, y_train, epochs=epocas, batch_size=lote, verbose=1)

#==============================================================================
# REALIZAR PREVISÃ•ES DO MODELO
#==============================================================================
# Fazer previsÃµes
train_predict = model.predict(X_train)

#==============================================================================
# SALVAR O MODELO TREINADO
#==============================================================================
# Salvar o modelo treinado
model.save('C:\RN\S8_RNT_treinada.h5')

#==============================================================================
# POSPROCESSAMENTO DOS DADOS
#==============================================================================
# Desfazer a normalizaÃ§Ã£o dos dados
train_predict = scaler.inverse_transform(train_predict)
y_train = scaler.inverse_transform([y_train])

#==============================================================================
# APRESENTAÃ‡ÃƒO GRÃFICA DOS RESULTADOS
#==============================================================================
# Plotar os resultados em dois grÃ¡ficos separados
fig, (ax1) = plt.subplots(1, 1, figsize=(8, 6))

# GrÃ¡fico 1: Dados de treinamento
ax1.plot(y_train[0], label='Dados de treinamento reais')
ax1.plot(train_predict[:, 0], label='PrevisÃµes de treinamento')
ax1.legend()
ax1.set_title('Dados de Treinamento')
ax1.set_xlabel('PerÃ­odo')
ax1.set_ylabel('Valor do DÃ³lar (R$)')
ax1.grid(True)

# Ajustar espaÃ§amento entre subplots
plt.tight_layout()

# Exibir os grÃ¡ficos
plt.show()

#==============================================================================
# APRESENTAÃ‡ÃƒO DAS MÃ‰TRICAS DE DESEMPENHO
#==============================================================================

mse_train = mean_squared_error(y_train[0], train_predict[:, 0])

print('\n' + '=' * 70)
print("Erro MÃ©dio QuadrÃ¡tico (MSE) - Treinamento: {:.4f}".format(mse_train))
print('\n')

mae_train = mean_absolute_error(y_train[0], train_predict[:, 0])

print('=' * 70)
print("Erro MÃ©dio Absoluto (MAE) - Treinamento: {:.4f}".format(mae_train))
print('\n')

r2_train = r2_score(y_train[0], train_predict[:, 0])

print('=' * 70)
print("Coeficiente de DeterminaÃ§Ã£o (RÂ²) - Treinamento: {:.4f}".format(r2_train))
print('\n' + '=' * 70)