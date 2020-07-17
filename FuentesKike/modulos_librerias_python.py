#Hay un montón de modulos disponibles en las librerias de python.
#por ejemplo el modulo sys, el random, el datetime, etc...


import sys # con el import, se importa todo el modulo

def main():
    v = sys.version_info #usamos funciones del modulo importado
    print('Python version {}.{}.{}'.format(*v))

if __name__ == '__main__': main()
