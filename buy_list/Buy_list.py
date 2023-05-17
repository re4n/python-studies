"""
Lista de compras 
O user deve conseguir inserir, apagar e listar
 os valores da sua lista
Nao permita que o programa quebre com erros de 
indice inexistentes na lista
"""

buyList = []
using = True

while using:
    print('\n#BUY-LIST#')
    print('Choose one option!')
    print('[1] - See your List')
    print('[2] - Add item')
    print('[3] - Delete item')
    print('[4] - See ya!')
    choose = input('Choose: ')

    if choose == '1':
        print('\n===See your List!===')
        if buyList:
            print(f'\n{buyList}')
        else:
            print('\n###Empty list!###')

    elif choose == '2':
        usingAdd = True
        while usingAdd:
            print('\n===Add Item!===')
            addItem = input('\nAdd an item: ').title()
            buyList.append(addItem)
            print(addItem, 'Added to your list!')
            chooseTwo = input('Add another item?: ').lower().startswith('n')

            if chooseTwo is True:
                break

    elif choose == '3':
        usingDel = True

        while usingDel:
            print('\n===Remove item!===')
            print('Your List:')
            for item in enumerate(buyList):
                indice, nome = item
                print(indice, nome)

            if buyList:

                try:
                    removeItem = int(input('\nRemove an item: '))
                    del buyList[removeItem]
                    print('Success!, item removed!')
                    print('Your list now:')
                    print(buyList)

                except IndexError:
                    print('Select a valid option!')
                except ValueError:
                    print('Enter whole numbers!')
                except Exception:
                    print('Unknown error!!')

                chooseThree = input(
                    'Remove another item?: ').lower().startswith('n')

            else:
                print('\n###Empty list!###')
                break

            if chooseThree is True:
                break

    elif choose == '4':
        print('\nFinish app!')
        using = False

    else:
        print('\nSelect a valid option!!')
