import json # para manipular arquivos .json

def criarJson(arquivo, nomeArquivo):
    """
    Essa função cria um arquivo json
    
    :param arquivo: Dicionário contendo os dados a serem gravado no arquivo json
    :param nomeArquivo: String contendo o nome do arquivo json a ser criado
    """
    try:
        with open(nomeArquivo + '.json', 'w', encoding="utf-8") as dadosJson: # abre um arquivo json no modo escrita, com possibilidade de uso de caracteres especiais (UTF-8)
            json.dump(arquivo, dadosJson, indent=4, ensure_ascii=False)   # escreve no modo apend, o conteudo de "arquivo" no json arbeto (dadosJson), e permite a codificação correta de caracteres não-ASCII
            dadosJson.close()   # fecha o arquivo "dadosJson"
    except (IOError, FileNotFoundError): # erro durante a leitura ou gravação de um arquivo.
        print(f"Erro ao tentar criar ou atualizar o arquivo {nomeArquivo}.json!")
    finally:
        print(f"{nomeArquivo}.json criado ou atualizado com sucesso!")
         

def abrirJson(nomeArquivo):
    """
    Essa função aber um arquivo json
    
    :param nomeArquivo: String contendo o nome do arquivo json a ser aberto
    :return: Dicionário com os dados do arquivo json aberto
    """
    dados = []  
    try:    # tenta usar  "with open"
        with open(nomeArquivo + '.json', 'r', encoding='utf-8') as dadosJson: # abre um arquivo json em modo de leitura. encoding="utf-8" para usar caracteres especiais
            dados = json.load(dadosJson)    # "dados" recebe o conteúdo do arquivo JSON
            dadosJson.close()   # fecha o arquivo "dadosJson" 
            return dados
    except (IOError, FileNotFoundError):
        print(f"{nomeArquivo}.json não encontrado!")
        return dados
    else:
        print(f"{nomeArquivo}.json aberto com sucesso!")