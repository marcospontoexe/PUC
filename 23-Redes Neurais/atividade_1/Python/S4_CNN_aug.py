# -*- coding: utf-8 -*-

#==============================================================================
# INTELIGÊNCIA ARTIFICIAL APLICADA
# REDES NEURAIS - SEMANA 4
# REDE NEURAL CONVOLUCIONAL (CNN) - COM DATA AUGMENTATION
# PROF. EDSON RUSCHEL
#
# ATIVIDADE SOMATIVA 1 - EXPERIMENTO COMPLEMENTAR
#
# Este script usa EXATAMENTE os mesmos parametros ajustaveis do S4_CNN.py
# (melhor configuracao encontrada na bateria de testes). A unica diferenca e
# a adicao de camadas de DATA AUGMENTATION (aumento de dados), que aplicam
# rotacoes, deslocamentos e zoom aleatorios em cada imagem durante o
# treinamento. O objetivo e tornar o modelo robusto a variacoes de estilo de
# escrita e melhorar o acerto no segundo conjunto de imagens (sufixo "b"),
# desenhado pelo professor fora do padrao da base MNIST.
#==============================================================================
#------------------------------------------------------------------------------
# IMPORTAÇÃO DE BIBLIOTECAS
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.layers import RandomRotation, RandomTranslation, RandomZoom
from PIL import Image

#------------------------------------------------------------------------------
# SEMENTE ALEATORIA FIXA (reprodutibilidade dos pesos iniciais e do embaralhamento)
tf.keras.utils.set_random_seed(42)

#------------------------------------------------------------------------------
# DEFINIÇÃO DO PERCENTUAL DE DADOS PARA TREINAMENTO
percentual_treinamento = 0.4 # 0.4 significa 40% para treinamento e 60% para teste

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

fa_C1 = 'relu' # função de ativação da primeira camada de convolução
fa_C2 = 'relu' # função de ativação da segunda camada de convolução
fa_D1 = 'relu' # função de ativação da camada densa oculta
fa_D2 = 'softmax' # função de ativação da camada densa de saída

#------------------------------------------------------------------------------
# DEFINIÇÃO DA ESTRUTURA DA REDE

# DEFINA O TAMANHO MxN DAS MATRIZES DE CONVOLUÇÃO
m_C1 = 3 # 3 significa uma matriz 3x3 para a primeira camada de convolução
m_C2 = 3 # 3 significa uma matriz 3x3 para a segunda camada de convolução

# DEFINA O NÚMERO DE NEURÔNIOS DAS CAMADAS DA REDE CNN
n_C1 = 32 # número de neurônios (filtros) da primeira camada de convolução
n_C2 = 64 # número de neurônios (filtros) da segunda camada de convolução
n_D1 = 128 # número de neurônios da camada densa oculta

#==============================================================================
# PARAMETROS DO DATA AUGMENTATION (AUMENTO DE DADOS)
#==============================================================================
# Estas camadas so ficam ATIVAS DURANTE O TREINAMENTO. Na hora de prever
# (model.predict) elas sao automaticamente desligadas pelo Keras, ou seja, a
# imagem de teste chega intacta ao modelo.
#
# A cada epoca, cada imagem de treino e transformada de forma diferente, o que
# impede a rede de "decorar" o enquadramento exato usado pela base MNIST
# (digito sempre centralizado numa caixa de 20x20 pixels).

rotacao = 0.08      # 0.08 = +/- 8% de uma volta completa (~ +/- 29 graus)
deslocamento = 0.10 # 0.10 = desloca ate 10% da altura/largura (~ 2,8 pixels)
zoom = 0.10         # 0.10 = amplia ou reduz o digito em ate 10%

#------------------------------------------------------------------------------
# CONSTRUÇÃO DO MODELO CNN
model = Sequential()

# Camadas de aumento de dados (aplicadas antes das convolucoes)
model.add(RandomRotation(rotacao, input_shape=(28, 28, 1)))
model.add(RandomTranslation(deslocamento, deslocamento))
model.add(RandomZoom(zoom))

model.add(Conv2D(n_C1, (m_C1, m_C1), activation = fa_C1))
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

otimizador = 'adam'

#------------------------------------------------------------------------------
# DEFINIÇÃO DA FUNÇÃO DE PERDA
# categorical_crossentropy
# binary_crossentropy
# mean_squared_error
# mean_absolute_error
# categorical_hinge
# logcosh

funcao_perda = 'categorical_crossentropy'

#------------------------------------------------------------------------------
# DEFINIÇÃO DA MÉTRICA DE DESEMPENHO
# accuracy
# mean_squared_error
# mean_absolute_error

metrica = 'accuracy'

#------------------------------------------------------------------------------
# Compilar o modelo
model.compile(optimizer = otimizador,
              loss = funcao_perda,
              metrics = [metrica])

#------------------------------------------------------------------------------
# DEFINIÇÃO DO NÚMERO DE ÉPOCAS E AMOSTRAS DE TREINAMENTO

# ATENCAO: com data augmentation o modelo nunca ve duas vezes exatamente a
# mesma imagem, o que torna o aprendizado mais lento por epoca. Por isso o
# numero de epocas foi triplicado (5 -> 15) em relacao ao S4_CNN.py.
epocas = 15
amostras = 128

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

#==============================================================================
# Carregar e pré-processar as imagens de teste
HD = 'C' # Digite a letra da Unidade de Disco
pasta = 'RN' # Digite a pasta onde estao as imagens

class_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Os dois conjuntos sao testados na mesma execucao, para permitir o comparativo:
# sufixo ''  -> primeiro conjunto (copiado da base MNIST)
# sufixo 'b' -> segundo conjunto (desenhado pelo professor)
nomes_base = ['zero0', 'um1', 'dois2', 'tres3', 'quatro4',
              'cinco5', 'seis6', 'sete7', 'oito8', 'nove9']

for sufixo, titulo in [('', 'CONJUNTO 1 (copiado da base MNIST)'),
                       ('b', 'CONJUNTO 2 (desenhado pelo professor)')]:

    print('\n' + '=' * 70)
    print(f'PREVISOES - {titulo}\n')

    image_paths = {HD + ':\\' + pasta + '\\' + nome + sufixo + '.png': i
                   for i, nome in enumerate(nomes_base)}

    fig, axs = plt.subplots(2, 5, figsize=(8, 5))
    axs = axs.flatten()
    acertos = 0

    for i, (image_path, real_label) in enumerate(image_paths.items()):
        # Carregar a imagem
        image = Image.open(image_path).convert('L')  # Converter para escala de cinza
        image = image.resize((28, 28))  # Redimensionar para 28x28 pixels
        image = np.array(image)  # Converter para matriz numpy
        image = image.reshape(1, 28, 28, 1)  # Adicionar dimensão de lote e canal

        # Normalizar a imagem
        image = image.astype('float32')
        image /= 255.0

        # Fazer a previsão da classe
        prediction = model.predict(image, verbose=0)
        predicted_class = np.argmax(prediction)

        if predicted_class == real_label:
            acertos += 1

        # Imprime no console para conferencia
        nome_arquivo = image_path.split('\\')[-1]
        print(f"{nome_arquivo} -> Real: {class_names[real_label]} | "
              f"Previsto: {class_names[predicted_class]}")

        # Exibir a imagem e as informações sobre o número real e previsto
        axs[i].imshow(np.squeeze(image), cmap='gray')
        axs[i].axis('off')
        axs[i].set_title(f'Real: {class_names[real_label]}\n'
                         f'Previsto: {class_names[predicted_class]}')

    print(f"\nTOTAL DE ACERTOS: {acertos}/10")
    fig.suptitle(f'{titulo} - {acertos}/10 acertos')
    plt.tight_layout()
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
