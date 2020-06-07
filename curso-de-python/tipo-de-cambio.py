# -*- coding: utf-8 -*-

def foreign_exchange_calculator(ammount):
    usd_to_arg_rate = 71.76
    return usd_to_arg_rate * ammount

def run():

    name = str(input('Hola, ¿Cuál es tu nombre? '))
    print('')
    print('Hola, ' + name + '! te presento la: ')
    print('')

    print('C A L C U L A D O R A  D E  D I V I S A S')
    print('Convierte dolares a pesos argentinos.')
    print('')

    ammount = float(input('Ingresa la cantidad de dólares que quieres convertir a pesos argentinos: '))

    result = foreign_exchange_calculator(ammount)

    print('${} dolares son ${:.2f} pesos argentinos'.format(ammount, result))
    print('')

if __name__ == '__main__':
    run()

    print('Gracias por usar la automatic calculator 2000!!')
    print('Adios.')

# :.2f limita en número de decimales en un número float
