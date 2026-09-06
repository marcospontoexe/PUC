# -*- coding: utf-8 -*-

#==============================================================================
# INTELIGENCIA ARTIFICIAL APLICADA
# REDES NEURAIS - SEMANA 4
# REDE NEURAL MLP (MULTI-LAYER PERCEPTRON) - COM DATA AUGMENTATION
# PROF. EDSON RUSCHEL
#
# ATIVIDADE SOMATIVA 1 - EXPERIMENTO COMPLEMENTAR
#
# Este script usa EXATAMENTE os mesmos parametros ajustaveis do S4_MLP.py
# (melhor configuracao encontrada na bateria de testes). A unica diferenca e
# a adicao de camadas de DATA AUGMENTATION (aumento de dados), que aplicam
# rotacoes, deslocamentos e zoom aleatorios em cada imagem durante o
# treinamento. O objetivo e tornar o modelo robusto a variacoes de estilo de
# escrita e melhorar o acerto no segundo conjunto de imagens (sufixo "b"),
# desenhado pelo professor fora do padrao da base MNIST.
#==============================================================================
#------------------------------------------------------------------------------
# IMPORTACAO DE BIBLIOTECAS
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Reshape, Flatten
from tensorflow.keras.layers import RandomRotation, RandomTranslation, RandomZoom
from sklearn.model_selection import train_test_split
from PIL import Image

#------------------------------------------------------------------------------
# SEMENTE ALEATORIA FIXA (reprodutibilidade dos pesos iniciais e do embaralhamento)
tensorflow.keras.utils.set_random_seed(42)

#------------------------------------------------------------------------------
# CRIACAO DO MODELO MLP
model = Sequential()

#------------------------------------------------------------------------------
# DEFINICAO DA QUANTIDADE DE NEURONIOS DAS CAMADAS
n1 = 256  # Quantidade de neuronios da Camada Oculta 1
n2 = 128  # Quantidade de neuronios da Camada Oculta 2
n3 = 2  # Quantidade de neuronios da Camada Oculta 3 (nao utilizada nesta configuracao)
ns = 10  # Quantidade de neuronios da Camada de Sai­da

#------------------------------------------------------------------------------
# DEFINICAO DAS FUNCOES DE ATIVACAO
    # relu    -> Rectified Linear Unit (Unidade Linear Retificada)
    # sigmoid -> sigmoid(x) = 1 / (1 + exp(-x))
    # tanh    -> Tangente hiperbolica
    # softmax -> Utilizada na camada de sai­da

# Selecione a Funcao de Ativacao da Camada Oculta 1
fa1 = 'tanh'

# Selecione a Funcao de Ativacao da Camada Oculta 2
fa2 = 'tanh'

# Selecione a Funcao de Ativacao da Camada de Sai­da
fas = 'softmax'

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
# ADICAO DE CAMADAS A REDE NEURAL

# As camadas de aumento de dados trabalham sobre imagens 2D, mas a MLP recebe
# um vetor de 784 posicoes. Por isso o vetor e remontado como imagem 28x28,
# sofre as transformacoes, e so entao e achatado de volta para 784.
model.add(Reshape((28, 28, 1), input_shape=(784,)))
model.add(RandomRotation(rotacao))
model.add(RandomTranslation(deslocamento, deslocamento))
model.add(RandomZoom(zoom))
model.add(Flatten())

# Primeira Camada Oculta
model.add(Dense(units=n1, activation=fa1))

# Segunda Camada Oculta
model.add(Dense(units=n2, activation=fa2))

# Camada de Sai­da
model.add(Dense(units=ns, activation=fas))

#==============================================================================
#------------------------------------------------------------------------------
# DEFINICAO DA FUNCAO DE PERDA
    # mean_squared_error       -> Erro quadratico medio.
    # binary_crossentropy      -> Entropia cruzada binaria.
    # categorical_crossentropy -> Entropia cruzada categorica.
    # mean_absolute_error      -> Erro absoluto medio.

fp = 'categorical_crossentropy'

#------------------------------------------------------------------------------
# DEFINICAO DO OTIMIZADOR
    # sgd     -> Descida de gradiente estocastico (SGD).
    # adam    -> SGD com adaptacao de taxa de aprendizado.
    # rmsprop -> Baseado em Root Mean Square Propagation.
    # adagrad -> Adapta a taxa de aprendizado para cada parametro.

otimizador = 'adam'

#------------------------------------------------------------------------------
# DEFINICAO DA METRICA DE DESEMPENHO
    # accuracy            -> Acuracia.
    # mean_squared_error  -> Erro quadratico medio.
    # mean_absolute_error -> Erro absoluto medio.

metrica = 'accuracy'

#------------------------------------------------------------------------------
# COMPILACAO DO MODELO

model.compile(loss=fp, optimizer=otimizador, metrics=[metrica])

#==============================================================================
#------------------------------------------------------------------------------
# CARREGAMENTO DOS DADOS DE TREINAMENTO E TESTE

(x_train, y_train), (x_test, y_test) =\
    tensorflow.keras.datasets.mnist.load_data()

#------------------------------------------------------------------------------
# PRE-PROCESSAMENTO DOS DADOS

# Redimensionar as imagens para um vetor unidimensional
x_train = x_train.reshape(-1, 784)
x_test = x_test.reshape(-1, 784)

# Converter para tipo float32
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# Normalizar os valores dos pixels para o intervalo [0, 1]
x_train /= 255.0
x_test /= 255.0

#------------------------------------------------------------------------------
# TRANSFORMACAO DOS ROTULOS EM CODIFICACAO ONE-HOT

y_train = tensorflow.keras.utils.to_categorical(y_train, num_classes=ns)
y_test = tensorflow.keras.utils.to_categorical(y_test, num_classes=ns)

#------------------------------------------------------------------------------
# DEFINICAO DO PERCENTUAL DO CONJUNTO DE DADOS DE TESTE

dados_teste = 0.20 # 0.2 significa 20% para teste (80% para treinamento)

#------------------------------------------------------------------------------
# DIVISAO DOS DADOS EM CONJUNTOS DE TREINAMENTO E TESTE

x_train, x_test, y_train, y_test =\
    train_test_split(x_train, y_train, \
    test_size=dados_teste, random_state=42)

#------------------------------------------------------------------------------
# DEFINICAO DO NUMERO DE EPOCAS E NUMERO DE AMOSTRAS

# ATENCAO: com data augmentation o modelo nunca ve duas vezes exatamente a
# mesma imagem, o que torna o aprendizado mais lento por epoca. Por isso o
# numero de epocas foi triplicado (15 -> 45) em relacao ao S4_MLP.py.
epocas = 45
amostras = 128

#------------------------------------------------------------------------------
# TREINAMENTO DA REDE NEURAL MLP

print('\n' + '=' * 70)
print('INICIANDO O TREINAMENTO DO MODELO (COM DATA AUGMENTATION)... \n')

model.fit(x_train, y_train, epochs = epocas, batch_size = amostras)

#==============================================================================
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
        image = image.reshape(1, 784)  # Redimensionar para (1, 784)

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
        axs[i].imshow(np.squeeze(image.reshape(28, 28)), cmap='gray')
        axs[i].axis('off')
        axs[i].set_title(f'Real: {class_names[real_label]}\n'
                         f'Previsto: {class_names[predicted_class]}')

    print(f"\nTOTAL DE ACERTOS: {acertos}/10")
    fig.suptitle(f'{titulo} - {acertos}/10 acertos')
    plt.tight_layout()
    plt.show()

#==============================================================================
# AVALIACAO DO MODELO (PERDA E METRICA DE DESEMPENHO)

print('\n' + '=' * 70)
print('CALCULANDO FUNCAO DE PERDA E METRICA DE DESEMPENHO...\n')
loss, metric = model.evaluate(x_test, y_test)

print('\n' + '=' * 70)
print('*** DESEMPENHO DO MODELO APOS O TREINAMENTO ***\n')

print("Funcao de Perda utilizada: " + fp)
print("Valor obtido: " + f" = {loss:.4f}" + '\n')

print('-' * 70 + '\n')

print("Metrica de Desempenho utilizada: " + metrica)
print("Valor obtido: " + f" = {metric:.4f} \n")

print('=' * 70)

#==============================================================================
