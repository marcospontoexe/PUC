'''
Aluno: Marcos Daniel Santana
Curso: Inteligência artificial aplicada
'''
import os #usado para enviar comandos para o terminal do sistema operacional
import platform #usado para verificar qual é o sistema operacional

estudante = []  #lista usada para armazenar nome dos estudandtes


def limpar_prompt():
    """
    Essa função limpa a tela
    """
    try:
        sistema_operacional = platform.system()
        if sistema_operacional == "Windows":
            os.system('cls')
        elif sistema_operacional in ["Linux", "Darwin"]:  
            os.system('clear')
        else:
            raise NotImplementedError(f"Sistema operacional '{sistema_operacional}' não suportado.")
    except Exception as e:
        print(f"Erro ao tentar limpar o prompt: {e}")



def leiaInt(i):
    """
    Essa função pede para o usuário digitar um número inteiro, saindo da função apenas quando a condição for fatisfeita.
    :param i: String usada para solicitar um valor ao usuário
    :param temp: Int
    """
    while True:
        try:
            while True:
                temp = int(input(i))
                if temp >=0:
                    break
                else:
                    print("Digite uma número maior doque zero!")

        except (TypeError, ValueError):
            print("\033[34mERRO. Apenas número inteiro!\033[m")
            continue
        except (KeyboardInterrupt):
            print("Programa interrompido pelo usuário.")
        else:
            return temp



def leiaNome(n):
    """
    Essa função pede para o usuário digitar uma String, saindo da função apenas quando a condição for fatisfeita.
    :param n: String usada para solicitar um valor ao usuário
    :param temp: String
    """
    while True:
        temp = input(n).strip()
        if temp == "" or temp.isalpha() == False:
            print("\033[34mERRO! Escreva algum nome.\033[m")
        else:
            return temp


def cabeçalho(txt):
    """
    Essa função imprime na tela um cabeçalho
    :param txt: String que para ser impressa como cabeçalho
    """
    print("-=" * 20)
    print(txt.center(40))
    print("-=" * 20)

def incluir(op):
    """
    Essa função inclui novos valores no banco da dados
    :param op: String relacionada à opção que será inclusa no banco de dados
    """
    if op.upper().strip() == "ESTUDANTES":
        estudante.append(leiaNome("Digite o nome: "))
    else:
        print("Em desenvolvimento!")        

def listar(op):
    """
    Essa função lista os valores do banco da dados
    :param op: String relacionada à opção que será listada
    """
    if len(estudante) == 0: # o banco de dados estaja sem cadastros
        print("Não há estudantes cadastrados!")
    else:
        for nome in estudante:
            print(f"Estudante: {nome}")

def atualizar(op):
    """
    Essa função lista os valores do banco da dados
    :param op: String relacionada à opção que será listada
    """
    print("Em desenvolvimento!")
        
def excluir(op):
    """
    Essa função lista os valores do banco da dados
    :param op: String relacionada à opção que será listada
    """
    print("Em desenvolvimento!")

def menuPrincipal(lista):
    """
    Essa função cria um menu de opções baseado na lista de entrada
    :param lista: Lista contendo os valores a serem impressos como um menu de opções
    :return: Retorna um int relacionado a opção escolhida a partir da lista de entrada
    """
    cabeçalho("MENU PRINCIPAL")
    for p, v in enumerate(lista):
        print(f"{p+1:0>2} - {v}")
    print("--" * 20)
    while True:
        op = leiaInt("Informe a opção desejada: ")
        if op > 0 and op <= len(lista):
            break
        else:
            print("\033[35mOpção inválida!!!\033[m")
    return op

def menuOp(n, lista_opt):
    """
    Essa função cria um menu de opções baseado em uma string e uma lista de entrada
    :param n: String usada como opção de seleção para o menu de operações
    :param lista_opt: Lista contendo os valores a serem impressos como um menu de opções
    """
    strAux = f"[{n}] menu de operações".upper()
    while True:
        cabeçalho(strAux)
        for p, v in enumerate(lista_opt):
            print(f"{p+1:0>2} - {v}")
        print("--" * 20)
        op = leiaInt("Informe a opção desejada: ")
        #limpar_prompt()
        if op > 0 and op <= len(lista_opt):
            if op == 1:
                incluir(n)
                limpar_prompt()
            elif op == 2:
                limpar_prompt()
                listar(n)
            elif op == 3:
                limpar_prompt()
                atualizar(n)
            elif op == 4:
                limpar_prompt()
                excluir(n)
            elif op == 5:
                limpar_prompt()    
                break
            
        else:
            print("\033[35mOpção inválida!!!\033[m")
        


while True:
    # retorna um int relacionada à lista de entrada (menu principal)
    opcao = menuPrincipal(["Gerenciar estudantes", "Gerenciar professores", "Gerenciar disciplinas", "Gerenciar turmas", "Gerenciar matrículas", "Sair"])
    limpar_prompt() #limpa a tela
    
    if opcao == 1:
        escolha = "estudantes"
        menuOp(escolha, ["Incluir", "Listar", "Atualizar", "Excluir", "Voltar ao menu principal"])  # menu de operação
    elif opcao == 2:
        escolha = "professores"
        print("Em desenvolvimento!")
    elif opcao == 3:
        escolha = "disciplinas"
        print("Em desenvolvimento!")
    elif opcao == 4:
        escolha = "turmas"
        print("Em desenvolvimento!")
    elif opcao == 5:
        escolha = "matrículas"
        print("Em desenvolvimento!")
    elif opcao == 6:
        cabeçalho("Saindo... Até logo!")
        break

   