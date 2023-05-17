"""
Calculadora com while!
"""

while True:
    num1 = input('Digite um numero: ')
    num2 = input('Digite outro numero: ')
    operador = input('Digite o operador (+ - / *): ')

    numeros_validos = None
    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos numeros digitados sao invalidos!')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador Invalido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue


    print('Realizando sua operacao, Aguarde...')
    print('Confira o resultado abaixo! ')
    if operador == '+':
        print(num1_float + num2_float)
    elif operador == '-':
        print(num1_float - num2_float)
    elif operador == '/':
        print(num1_float / num2_float)
    elif operador == '*':
        print(num1_float * num2_float)
    else:
        print('Nao deveria cair aqui!')


    ## Command para sair!
    sair = input('Deseja sair?: [S] ').lower().startswith('s')
    print('Reiniciando App..')

    if sair is True:
        print('App Finalizado!')
        break