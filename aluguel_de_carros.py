print('===== Bem Vindo ao Aluguél de Carros =====')
print('-'*8)
print('Cadastro')
print('-'*8)

nome = str(input('Nome Completo: '))
carro = str(input('Carro: '))
while True:
    placa = str(input('Placa: '))
    if len(placa) <= 5:
        print('Oops!  That was no valid value.  Try again...')
    elif len(placa) > 5:
        break

dias = int(input('Quantos Dias: '))
kms = float(input('Kms Rodados: '))


preço_por_dia = dias * 60
preço_por_km = kms * 0.15
preço_a_pagar = preço_por_dia + preço_por_km
pagamento = int(input('''Formas de Pagamento:
    [1]-Cartão
    [2]-Dinheiro
    >>> '''))


if pagamento == 1:
    dividir = int(input('''De quantas vezes:
    [1]- 2 vezez
    [2]- 3 vezes
    >>> '''))
    print('=' * 15)
    print('Nota Fiscal:')
    print('Nome: {}'.format(nome))
    print('Carro: {}'.format(carro))
    print('Placa: {}'.format(placa))
    print('Total de dias: {} dias'.format(dias))
    print('Total de Kilometros: {}Km'.format(kms))
    if dividir == 1:
        divisão = preço_a_pagar / 2
        print('Formas de Pagamento: CARTÃO')
        print('Total a pagar: 2x de R${:.2f}'.format(divisão))
        print('Valor Final: R${:.2f}'.format(preço_a_pagar))
    elif dividir == 2:
        divisão = preço_a_pagar / 3
        print('Formas de Pagamento: CARTÃO')
        print('Total a pagar: 3x de R${:.2f}'.format(divisão))
        print('Valor Final: R${:.2f}'.format(preço_a_pagar))
elif pagamento == 2:
    preço_a_pagar
    print('=' * 15)
    print('Nota Fiscal:')
    print('Nome: {}'.format(nome))
    print('Carro: {}'.format(carro))
    print('Placa: {}'.format(placa))
    print('Total de dias: {} dias'.format(dias))
    print('Total de Kilometros: {}Km'.format(kms))
    print('Formas de Pagamento: DINHEIRO')
    print('Total a pagar: R${:.2f}'.format(preço_a_pagar))
    print('Valor Final: R${:.2f}'.format(preço_a_pagar))
print('='*15)















