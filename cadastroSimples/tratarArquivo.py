def procura(arq):
    try:
        a =open(arq,'rt')
        a.close()
        return True

    except FileNotFoundError:
        return False

def criarArquivo(arq):
    try:
        a= open(arq,'wt+')
        a.close()
    except:
        print('erro')


def lerArquivo(arq):
    with open(arq,'rt') as arquivo:
        people = arquivo.readlines()
        for c in people:
            dado = c.split(';')
            dado[1]=dado[1].replace('\n','')
            print(f'{dado[0]:<20}{dado[1]:>5}')


def escreverArquivo(arq,nome,idade):
    with open(arq,'at') as arquivo:
        return arquivo.write(f'{nome}; {str(idade)}\n')
