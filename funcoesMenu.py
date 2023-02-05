import tratarArquivo
from escolha import*

arq = 'pessoasCadastradas.txt'
enc = tratarArquivo.procura(arq)
if not enc:
    tratarArquivo.criarArquivo(arq)

def menu():
    print('~'*30)
    print(f"{'MENU':.^30}")
    print('~'*30)
    while True:
        try:
            esc = int(input(('''
1 - pessoas cadastradas
2- cadastrar nova pessoa
3- sair

>>> ''')))
        except:
            print('erro! digite uma opção válida.')
            continue
        else:
            if esc == 1:
                pessoas(arq)
            elif esc == 2:
                cadastrar(arq,nome,idade)
            elif esc ==3:
                sair()
                break
            else:
                continue


