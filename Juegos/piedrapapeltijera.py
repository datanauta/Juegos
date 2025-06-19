import random

from django.contrib.admin.templatetags.admin_list import result_list_tag

listaEleccion = ['piedra','papel','tijera']

def obtener_eleccion_usuario():

    eleccion = input('Elige : piedra, papel, tijera').lower()
    while eleccion not in listaEleccion:
        print('La elección no es válida,intenta de nuevo')
        eleccion = input('Elige: piedra,papel,tijera').lower()
    return eleccion

def obtener_eleccion_computadora():
    return random.choice(listaEleccion)


def determinar_ganador(usuario,computadora):

    if usuario == computadora:
        return 'Empate'
    elif (usuario == 'piedra' and computadora == 'tijera') or \
            (usuario== 'papel' and computadora == 'piedra') or \
            (usuario == 'tijera' and computadora == 'papel'):
            return 'Ganas'
    else:
        return 'Pierdes'

def jugar():
    print('Bienvenido al juego pidra,papel,tijera')
    usuario = obtener_eleccion_usuario()
    computadora = obtener_eleccion_computadora()
    print(f'La computadora eligió {computadora}')
    resultado = determinar_ganador(usuario, computadora)
    print(f'Resultado: {resultado}')


if __name__ == '__main__':
    jugar()
