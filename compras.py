from codigos import *

if __name__ == '__main__':
    lista_produtos = []
    recuperar = []

    while True:
        print('--------- SISTEMA DE COMPRAS ----------')
        print('''1 - Adicionar um produto.
2 - Retirar último produto.
3 - Colocar último produto removido.
4 - Listar produtos.
5 - Para sair.
        ''')
        opcao = leiaint('Selecione uma opção: ')

        if opcao == 5:
            break
        else:
            if opcao == 1:
                produto = []
                temp = []
                dado = input('Nome do produto: ').strip().lower()
                produto.append(dado)
                temp.append(leiafloat('Preço do produto: R$ '))
                temp.append(leiaint('Quantidade: '))
                produto.append(temp)
            elif opcao == 2:
                desfazer(lista_produtos, recuperar)
                continue
            elif opcao == 3:
                refazer(lista_produtos, recuperar)
                continue
            elif opcao == 4:
                listar(lista_produtos)
                continue
            else:
                print('Opção inválida!')
                continue
            adicionar(produto, lista_produtos)



