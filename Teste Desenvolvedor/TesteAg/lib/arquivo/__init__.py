from TesteAg.lib.interface import *

# FUNÇÃO UTILIZADA PARA CADASTRAMENTO DE MOTORISTA E VEÍCULO (Verifica se o arquivo
# onde serão guardados os dados ja existe)
def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

# FUNÇÃO UTILIZADA PARA CADASTRAMENTO DE MOTORISTA E VEÍCULO (caso o arquivo
# onde serão guardados não existe, essa função ira criar)
def criaArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Ocorreu um ERRO na criação do arquivo Veiculos!")
    else:
        print(f"Arquivo {nome} criado com sucesso!")


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("Erro ao ler os dados")
    else:
        print("-"*45)
        print("\033[91mVEICULOS CADASTRADOS:\033[m".center(55))
        print("-"*45)
        print("Placa   Marca  Veiculo  Km_Oleo")
        print("-"*45)
        for Lin in a:
            dado = Lin.split(';')
            dado = Lin.replace('\n', '')
            dado = Lin.replace(';', '   ')
            """print(f" {dado[Lin:1]}")"""

            print(f'{dado}', '-'*45)
    finally:
        a.close()

def cadastrar(arq, placa='desconhecida', marca ='desconhecida', carro = 'desconhecido', oleo = 'desconhecido'):
    try:
        a = open(arq, 'at')
    except:
        print("Houve um ERRO no cadastramento")
    else:
        try:
            a.write(f'{placa};{marca};{carro};{oleo}\n')
        except:
            print("Houve um ERRO na hora de escrever os dados")
        else:
            print("Novo registro de veículo adicionado!")
            a.close()

###########################################################################################
def lerArquivoMotorista(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("Erro ao ler os dados")
    else:
        print("-"*45)
        print("\033[91mMOTORISTAS CADASTRADOS:\033[m".center(55))
        print("-"*45)
        print("Codigo   Nome  Telefone  CNH")
        print("-"*45)
        for Lin in a:
            dado = Lin.split(';')
            dado = Lin.replace('\n', '')
            dado = Lin.replace(';', '   ')
            """print(f" {dado[Lin:1]}")"""

            print(f'{dado}', '-'*45)
    finally:
        a.close()

def cadastrarM(arq, codigo='desconhecido', nome='desconhecido', telefone='desconhecido', CNH= 'desconhecido'):
    try:
        a = open(arq, 'at')
    except:
        print("Houve um ERRO no cadastramento")
    else:
        try:
            a.write(f'{codigo};{nome};{telefone};{CNH}\n')
        except:
            print("Houve um ERRO na hora de escrever os dados")
        else:
            print("Novo registro de Motrista adicionado!")
            a.close()