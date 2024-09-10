#pacote (biblioteca) é a junção de vários módulos

from biblioteca.interface import *   #importa todos as funções do módulo interface, do pacote biblioteca
from biblioteca.trat_erros import *
import os   #usado para limpar o prompt de comando




while True:

    opcao = menuPrincipal(["Gerenciar estudantes", "Gerenciar professores", "Gerenciar disciplinas", "Gerenciar turmas", "Gerenciar matrículas", "Sair"])
    limpar_prompt()
    
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

    menuOp(escolha, ["Incluir", "Listar", "Atualizar", "Excluir", "Voltar ao menu principal"])
    #limpar_prompt()