
cpf_pessoa = input('CPF: ')
numcpf = cpf_pessoa.replace('.', '').replace('-', '')


def calcDigito(num_cpf):
    multiply_num = []

    for index, numero in enumerate(num_cpf):
        num_int = int(numero)
        multiply_num += [num_int * (len(num_cpf) + 1 - index)]

    digito = sum(multiply_num)
    digito = (digito * 10) % 11

    if digito >= 9:
        return 0
    else:
        return digito


penultimo_digito = calcDigito(numcpf[:9])
ultimo_digito = calcDigito(numcpf[:9]+str(penultimo_digito))

cpf_gerado = f'{numcpf[:3]}.{numcpf[3:6]}.{numcpf[6:9]}-{penultimo_digito}{ultimo_digito}'

if cpf_gerado != cpf_pessoa:
    print('ESTE CPF NAO E VALIDO!')
    print('CPF INFORMADO: ', cpf_pessoa)
    print('CPF GERADO: ', cpf_gerado)


else:
    print('ESTE CPF E VALIDO!')
    print('CPF INFORMADO: ', cpf_pessoa)
    print('CPF GERADO: ', cpf_gerado)
