import math


def calculate():
    operation = input('''
Por favor indique qual a operação a realizar:
+ para soma (3 + 4 = 7)
- para subtração (3 - 4 = -1)
* para multiplicação (5 * 4 = 20)
/ para divisão (10 / 2 = 5)
^ para potência (4 ^ 2 = 16)
r para raiz quadrada (raiz quadrada de 4 = 2)
% para percentagem (50% de 10 = 5)
>> ''')
    try:
        number_1 = float(input('Insira um numero: '))
        if operation != 'r':
            number_2 = float(input('Insira outro numero: '))
        else:
            number_2 = 0

        if operation == '+':
            print('{} + {} = {}'.format(number_1, number_2, number_1 + number_2))

        elif operation == '-':
            print('{} - {} = {}'.format(number_1, number_2, number_1 - number_2))

        elif operation == '*':
            print('{} * {} = {}'.format(number_1, number_2, number_1 * number_2))

        elif operation == '/':
            if number_2 != 0.0:
                print('{} / {} = {}'.format(number_1, number_2, number_1 / number_2))
            else:
                print('Erro divisão por zero!')

        elif operation == '^':
            print('{} ^ {} = {}'.format(number_1, number_2, math.pow(number_1, number_2)))

        elif operation == 'r':
            if number_1 >= 0.0:
                print('raiz quadrada de {} = {}'.format(number_1, math.sqrt(number_1)))
            else:
                print('Erro raiz de numero negativo.')

        elif operation == '%':
            print('{}% de {} = {}'.format(number_1, number_2, number_2 * (number_1 / 100)))

        else:
            print('Operação inválida.')
    except ValueError:
        print('Numeros invalidos')

    again()


def again():
    calc_again = input('''
        Quer calcular novamente? S para sim ou N para não.
        >> ''')

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('Obrigada e até a próxima!')
    else:
        again()


calculate()
