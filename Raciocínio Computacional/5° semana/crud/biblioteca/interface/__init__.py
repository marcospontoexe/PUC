from biblioteca.trat_erros import *
import os
import platform

estudantes = []
dados = {}

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
        #estudantes.append(leiaString("Digite o nome: "))
        dados["código"] = leiaInt("Digite o código do estudante: ")
        dados["nome"] = leiaString("Digite o nome do estudante: ")
        dados["cpf"] = str(leiaInt("Digite o CPF do estudante: "))
        estudantes.append(dados.copy()) 
    else:
        print("Em desenvolvimento!")        

def listar(op):
    """
    Essa função lista os valores do banco da dados
    :param op: String relacionada à opção que será listada
    """
    if op.upper().strip() == "ESTUDANTES":
        if len(estudantes) == 0: # o banco de dados estaja sem cadastros
            print("Não há estudantes cadastrados!")
        else:
            print("Estudantes cadastrados:")
            for e in estudantes: # percorre cada índice da lista
                for k, v in e.items():  # percorre cada índice do dicionário
                    print(f"{k}: {v}", end=' | ')
                print("")
                

def atualizar(op):
    """
    Essa função atualiza os valores do banco da dados
    :param op: String relacionada à opção que será atualizada
    """
    print("Em desenvolvimento!")
        
def excluir(op):
    """
    Essa função exclui os valores do banco da dados
    :param op: String relacionada à opção que será excluida
    """
    if op.upper().strip() == "ESTUDANTES":
        if len(estudantes) == 0: # o banco de dados estaja sem cadastros
            print("Não há estudantes para excluir!")
        else:
            apagar = leiaInt("Digite o código do estudante a ser excluido: ")
            for cod in estudantes: # percorre cada índice da lista
                if cod[0][0] == apagar:
                    estudantes.pop(cod)   #apaga o item da posição iterada

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