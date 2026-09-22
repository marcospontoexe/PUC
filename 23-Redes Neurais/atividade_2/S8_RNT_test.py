# -*- coding: utf-8 -*-
#==============================================================================
# INTELIGÃŠNCIA ARTIFICIAL APLICADA
# REDES NEURAIS - SEMANA 8
# REDE NEURAL TEMPORAL (RNT) PARA TESTE
# PROF. EDSON RUSCHEL
#==============================================================================

from tensorflow.keras.models import load_model
import pandas as pd
import matplotlib.pyplot as plt
#import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
#from keras.models import Sequential
#from keras.layers import Dense, LSTM
#import matplotlib.pyplot as plt

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score


#==============================================================================
# AJUSTAR A JANELA DE PREVISÃƒO (DEVE SER A MESMA UTILIZADA NO TREINAMENTO)
#==============================================================================

janela_prev = 50

#==============================================================================
# CARREGAMENTO E PREPROCESSAMENTO DOS DADOS
#==============================================================================

# Ler os arquivos CSV de treinamento e teste
#train_df = pd.read_csv('C:\\RN\\dolar_treinamento.csv')
test_df = pd.read_csv('C:\\RN\\dolar_teste_2.csv')

# Filtrar apenas a coluna 'Valor' nos dados de treinamento e teste
test_data = test_df[['Dolar']].values

# Filtrar apenas a coluna 'Valor' nos dados de treinamento e teste
test_data = test_df[['Dolar']].values

# Normalizar os dados de treinamento entre 0 e 1
scaler = MinMaxScaler(feature_range=(0, 1))
test_data_scaled = scaler.fit_transform(test_data)

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

# Criar os conjuntos de treinamento e teste
X_test, y_test = create_dataset(test_data_scaled, janela_prev)

# Reshape dos dados para o formato esperado pela LSTM [amostras, janela de tempo, caracterÃ­sticas]
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

#==============================================================================
# CRIAÃ‡ÃƒO DO MODELO DA REDE NEURAL TEMPORAL
#==============================================================================

# Carregar o modelo treinado
model = load_model('C:\RN\S8_RNT_treinada.h5')

#==============================================================================
# REALIZAR PREVISÃ•ES DO MODELO
#==============================================================================
# Fazer previsÃµes
test_predict = model.predict(X_test)

#==============================================================================
# POSPROCESSAMENTO DOS DADOS
#==============================================================================
# Desfazer a normalizaÃ§Ã£o dos dados
test_predict = scaler.inverse_transform(test_predict)
y_test = scaler.inverse_transform([y_test])

#==============================================================================
# APRESENTAÃ‡ÃƒO GRÃFICA DOS RESULTADOS
#==============================================================================
# Plotar os resultados em dois grÃ¡ficos separados
fig, (ax1) = plt.subplots(1, 1, figsize=(8, 6))

# GrÃ¡fico 1: Dados de treinamento
ax1.plot(y_test[0], label='Dados de teste reais')
ax1.plot(test_predict[:, 0], label='PrevisÃµes de teste')
ax1.legend()
ax1.set_title('Dados de Teste')
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

mse_test = mean_squared_error(y_test[0], test_predict[:, 0])

print('\n' + '=' * 70)
print("Erro MÃ©dio QuadrÃ¡tico (MSE) - Teste: {:.4f}".format(mse_test))
print('\n')

mae_test = mean_absolute_error(y_test[0], test_predict[:, 0])

print('=' * 70)
print("Erro MÃ©dio Absoluto (MAE) - Teste: {:.4f}".format(mae_test))
print('\n')

r2_test = r2_score(y_test[0], test_predict[:, 0])

print('=' * 70)
print("Coeficiente de DeterminaÃ§Ã£o (RÂ²) - Teste: {:.4f}".format(r2_test))
print('\n' + '=' * 70)