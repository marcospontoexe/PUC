#pacote (biblioteca) é a junção de vários módulos

from biblioteca.interface import *   #importa todos as funções do módulo interface, do pacote biblioteca
#from biblioteca.trat_erros import * #importa todos as funções do módulo trat_erros, do pacote biblioteca
#from biblioteca.arquivos import *   #importa todos as funções do módulo arquivos, do pacote biblioteca
import os   #usado para limpar o prompt de comando

while True:
    # retorna um int relacionada à lista de entrada (menu principal)
    opcao = menuPrincipal(["Gerenciar estudantes", "Gerenciar professores", "Gerenciar disciplinas", "Gerenciar turmas", "Gerenciar matrículas", "Sair"])
    #limpar_prompt() #limpa a tela
    
    if opcao == 1:
        escolha = "estudantes"
    elif opcao == 2:
        escolha = "professores"
    elif opcao == 3:
        escolha = "disciplinas"
    elif opcao == 4:
        escolha = "turmas"
    elif opcao == 5:
        escolha = "matrículas"
    elif opcao == 6:
        cabeçalho("Saindo... Até logo!")
        break

    menuOp(escolha, ["Incluir", "Listar", "Atualizar", "Excluir", "Voltar ao menu principal"])  # menu de operação

 