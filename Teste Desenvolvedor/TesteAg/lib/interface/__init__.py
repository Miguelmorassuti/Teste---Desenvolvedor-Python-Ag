from TesteAg.lib.arquivo import *
from time import sleep

arqV = 'arquivoVeiculos.txt'
arqM = 'arquivoMotorista.txt'

def linha(tam = 45):
    return "-"*tam

def menuInicial():
    print(linha())
    print("\033[91mCONTROLE DE VEÍCULOS\033[m".center(55))
    print(linha())
    print("MENU".center(45))
    print("\033[93m[1] -\033[m \033[92mPagina Inicial\033[m \n"
          "\033[93m[2] -\033[m \033[92mNovo Veiculo\033[m \n"
          "\033[93m[3] -\033[m \033[92mNovo Motorista\033[m \n"
          "\033[93m[4] -\033[m \033[92mFazer Consulta de Veículos\033[m \n"
          "\033[93m[5] -\033[m \033[92mFazer Consulta de Motoristas\033[m \n"
          "\033[93m[6] -\033[m \033[92mSair do Sistema\033[m")


# Função para entrada de dados envolvendo o cadastro de novo veículo
def veiculos():
    print(linha())
    print("NOVO CADASTRO DE VEÍCULO".center(45))
    print(linha())
    placa = str(input("Informe a Placa do Veículo: "))
    marca = str(input("Informe a marca do Veículo: "))
    carro = str(input("Informe o nome do veículo: "))
    oleo = str(input("Com quantos KMs rodados ocorrerá a troca de oleo?: "))
    cadastrar(arqV, placa, marca,carro,oleo)

# Função para consultar os dados do arquivo Veiculos
def consultaV():
    """arqV = 'arquivoVeiculos.txt'  """
    if not arqExiste(arqV):
        criaArq(arqV)
    lerArquivo(arqV)

# Função para entrada de dados envolvendo o cadastro de novo motorista
def motorista():
    print(linha())
    print("NOVO CADASTRO DE MOTORISTA".center(45))
    print(linha())
    idMotorista = str(input("Informe o codigo do Motorista: "))
    nome = str(input(("Informe o nome do motorista: ")))
    telefone = str(input("Informe o telefone do motorista: "))
    cnh = str(input("Informe o número da CNH do motorista: "))
    cadastrarM(arqM, idMotorista, nome, telefone, cnh)

# Função para consultar os dados do arquivo Veiculos
def consultaM():
    if not arqExiste(arqM):
        criaArq(arqM)
    lerArquivoMotorista(arqM)


# Função para receber a escolha do usuário, validar se a escolha digitada existe e repassar
# para a função compentente que exerca a atividade que o usuário necessite
def opcoes():
    while True:

        try:
            esc = int(input("\n\033[96mPor gentileza, informe sua escolha -->\033[m"))
            linha()
        except (ValueError, TypeError):
            print("\033[31mERRO: Por favor, digite uma opção válida \nTente novamente!\033[m")
            continue
        else:
            if (esc != 1 and esc != 2 and esc != 3 and esc != 4 and esc !=5 and esc !=6):
                print("-" * 45)
                print("\033[31mOpção não existente, tente novamente!\033[m")
                continue

            else:
                if(esc==1):
                    menuInicial()
                    continue

                elif(esc==2):
                    veiculos()
                    continue

                elif(esc==3):
                    motorista()
                    continue

                elif(esc==4):
                    consultaV()
                    continue

                elif(esc==5):
                    consultaM()
                    continue

                elif(esc==6):
                    sleep(0.5)
                    print("\033[31mSistema Encerrado!\033[m")
                    break

