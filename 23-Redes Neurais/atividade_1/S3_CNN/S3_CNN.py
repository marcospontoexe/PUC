# -*- coding: utf-8 -*-
#==============================================================================
# INTELIGÊNCIA ARTIFICIAL APLICADA
# REDES NEURAIS - SEMANA 3
# REDE NEURAL CONVOLUCIONAL (CNN)
# PROF. EDSON RUSCHEL
#==============================================================================
#------------------------------------------------------------------------------
# IMPORTAÇÃO DE BIBLIOTECAS
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense


#------------------------------------------------------------------------------
# DEFINIÇÃO DO PERCENTUAL DE DADOS PARA TREINAMENTO
percentual_treinamento = 0.1 # 0.7 significa 70% para treinamento e 30% para teste

#------------------------------------------------------------------------------
# Carregar dados MNIST
(x_train_full, y_train_full), (x_test_full, y_test_full) = mnist.load_data()

#------------------------------------------------------------------------------
# Determinar o tamanho do conjunto de treinamento com base na proporção especificada
train_size = int(len(x_train_full) * percentual_treinamento)

#------------------------------------------------------------------------------
# Dividir os dados em conjuntos de treinamento e teste
x_train = x_train_full[:train_size]
y_train = y_train_full[:train_size]
x_test = x_train_full[train_size:]
y_test = y_train_full[train_size:]

#------------------------------------------------------------------------------
# Pré-processamento dos dados
x_train = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test = x_test.reshape(-1, 28, 28, 1) / 255.0
y_train = tf.keras.utils.to_categorical(y_train)
y_test = tf.keras.utils.to_categorical(y_test)

#------------------------------------------------------------------------------
# DEFINIÇÃO DAS FUNÇÕES DE ATIVAÇÃO
    # relu: Rectified Linear Unit, retorna valor positivo e zero caso contrário.
    # sigmoid: Função logística, retorna valores entre 0 e 1.
    # tanh: Tangente hiperbólica, que retorna valores entre -1 e 1.
    # softmax: Normaliza as saídas em uma distribuição de probabilidade.

fa_C1 = 'tanh' # função de ativação da primeira camada de convolução
fa_C2 = 'tanh' # função de ativação da segunda camada de convolução
fa_D1 = 'tanh' # função de ativação da camada densa oculta
fa_D2 = 'sigmoid' # função de ativação da camada densa de saída

#------------------------------------------------------------------------------
# DEFINIÇÃO DA ESTRUTURA DA REDE

# DEFINA O TAMANHO MxN DAS MATRIZES DE CONVOLUÇÃO
m_C1 = 9 # 9 significa uma matriz 9x9 para a primeira camada de convolução
m_C2 = 9 # 9 significa uma matriz 9x9 para a segunda camada de convolução

# DEFINA O NÚMERO DE NEURÔNIOS DAS CAMADAS DA REDE CNN
n_C1 = 2 # número de neurônios da primeira camada de convolução
n_C2 = 2 # número de neurônios da segunda camada de convolução
n_D1 = 2 # número de neurônios da camada densa oculta

#------------------------------------------------------------------------------
# CONSTRUÇÃO DO MODELO CNN
model = Sequential()

model.add(Conv2D(n_C1, (m_C1, m_C1), activation = fa_C1, input_shape=(28, 28, 1)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(n_C2, (m_C2, m_C2), activation = fa_C2))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(n_D1, activation = fa_D1))
model.add(Dense(10, activation = fa_D2))

#------------------------------------------------------------------------------
# DEFINIÇÃO DO OTIMIZADOR
# adam
# sgd
# rmsprop
# adadelta
# adagrad
# adamax
# nadam

otimizador = 'adadelta'

#------------------------------------------------------------------------------
# DEFINIÇÃO DA FUNÇÃO DE PERDA
# categorical_crossentropy
# binary_crossentropy
# mean_squared_error
# mean_absolute_error
# categorical_hinge
# logcosh

funcao_perda = 'categorical_hinge'

#------------------------------------------------------------------------------
# DEFINIÇÃO DA MÉTRICA DE DESEMPENHO
# accuracy
# mean_squared_error
# mean_absolute_error

metrica = 'mean_absolute_error'

#------------------------------------------------------------------------------
# Compilar o modelo
model.compile(optimizer = otimizador,
              loss = funcao_perda,
              metrics = [metrica])

#------------------------------------------------------------------------------
# DEFINIÇÃO DO NÚMERO DE ÉPOCAS E AMOSTRAS DE TREINAMENTO
epocas = 2
amostras = 1024

#------------------------------------------------------------------------------
# Treinar o modelo
history = model.fit(x_train, y_train, \
                    epochs = epocas, \
                    batch_size = amostras, \
                    validation_data = (x_test, y_test))

#------------------------------------------------------------------------------
# Exibir resultados na aba "Plots"
plt.plot(history.history[metrica], label='Métrica de Treinamento')
plt.plot(history.history['val_' + metrica], label='Métrica de Validação')
plt.plot(history.history['loss'], label='Função de Perda de Treinamento')
plt.plot(history.history['val_loss'], label='Função de Perda de Validação')
plt.xlabel('Épocas')
plt.ylabel('Métrica / Função de Perda')
plt.legend()
plt.show()

#------------------------------------------------------------------------------
# Fazer previsões para imagens de teste aleatórias
random_indices = np.random.choice(len(x_test), size=10, replace=False)
predictions = model.predict(x_test[random_indices])
predicted_labels = np.argmax(predictions, axis=1)

#------------------------------------------------------------------------------
# Exibir imagens de teste aleatórias e suas previsões
fig, axes = plt.subplots(2, 5, figsize=(10, 4))
axes = axes.flatten()

for i, ax in enumerate(axes):
    ax.imshow(x_test[random_indices[i]].reshape(28, 28), cmap='gray')
    
    ax.set_title(f'Real: {np.argmax(y_test[random_indices[i]])},'
             f'\nPrevisto: {predicted_labels[i]}')
    
    ax.axis('off')

# Ajustar o espaçamento e apresentar as imagens
plt.subplots_adjust(hspace=0.5)
plt.show()

#==============================================================================
# AVALIACAO DO MODELO (PERDA E METRICA DE DESEMPENHO)

print('\n\n\n' + '=' * 70)
print('CALCULANDO FUNCAO DE PERDA E METRICA DE DESEMPENHO...\n')
loss, metric = model.evaluate(x_test, y_test)

print('\n' + '=' * 70)
print('*** DESEMPENHO DO MODELO APOS O TREINAMENTO ***\n')


print("Funcao de Perda utilizada: " + funcao_perda)
print("Valor obtido: " + f" = {loss:.4f}" + '\n')

print('-' * 70 + '\n')

print("Metrica de Desempenho utilizada: " + metrica)
print("Valor obtido: " + f" = {metric:.4f}\n")

print('=' * 70)

#==============================================================================