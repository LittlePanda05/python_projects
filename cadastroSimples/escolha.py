import tratarArquivo
nome=''
idade=''
def pessoas(arq):
    print(f'{"OPÇÃO 1: pessoas":.^30}')
    print(f'{"NOME":<20}  {"IDADE":>5}')
    print(tratarArquivo.lerArquivo(arq))
    


def cadastrar(arq,nome='desconhecido',idade=0):
    print(f'{"OPÇÃO 2: cadastrar":.^30}')
    nome = str(input('nome: '))
    while True:
        try:
            idade= int(input('idade em anos: '))
            break
        except:
            print('digite uma idade válida')
            continue
    tratarArquivo.escreverArquivo(arq,nome,idade)

def sair():
    print(f'{"saindo":.^30}')
