def listar(produto):
    """
    função que retorna a lista com os produtos
    :param produto: lista dos produtos
    :return: retorna a lista com os produtos adicionados
    """
    print('-' * 30)
    print('CARRINHO DE COMPRAS'.center(30))
    print('-' * 30)
    print('Produto'.center(10), 'Preço'.center(10), 'Quantidade'.center(10))
    if not produto:
        print('Carrinho vazio!!!')
    for prod in produto:
        print(f'{prod[0]:^10}R${prod[1][0]:^10}{prod[1][1]:^10}')


def adicionar(produto, lista_produtos):
    """
    função que adiconar o produto na lista de compras
    :param produto: compra a ser adicioanda na listar
    :param lista_produtos: lista de compras
    :return: retorna a lista de compras
    """
    lista_produtos.append(produto)


def desfazer(lista_produtos, recuperar):
    """
    função que desfazar a compra, remove o útimo elemento da lista de compras
    :param lista_produtos: lista de compras
    :param recuperar: variável que armazena o último produto
    :return: retorna a lista com a alteração de desfazer
    """
    if not lista_produtos:
        print('Nada para desfazer!')
        return
    proximo = lista_produtos.pop()
    recuperar.append(proximo)


def refazer(lista_produtos, recuperar):
    """
    função que adiciona o último item removido
    :param lista_produtos: lista de compras
    :param recuperar:
    :return:
    """
    if not recuperar:
        print('Nada para refazer!')
        return
    proximo = recuperar.pop()
    lista_produtos.append(proximo)


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Por favor digite um número inteiro válido!')
            continue
        except KeyboardInterrupt:
            print("Entrada de dados interrompida pelo usuário!")
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'Por favor digite um número real válido!')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário!')
        else:
            return n