import requests
import random
import html

def main():
    response = requests.get('https://opentdb.com/api.php?amount=1')
    trivia = response.json()['results'][0]

    pregunta = html.unescape(trivia['question'])
    correcto = html.unescape(trivia['correct_answer'])
    incorrectas = [html.unescape(i) for i in trivia['incorrect_answers']]

    print(f'\nPregunta: {pregunta}')
    opciones = incorrectas + [correcto]
    random.shuffle(opciones)

    for i, opcion in enumerate(opciones):
        print(f'{i + 1}. {opcion}')

    try:
        respuesta_usuario = int(input('Elige la opción correcta (1-4): '))
        if opciones[respuesta_usuario - 1] == correcto:
            print('¡Correcto!')
        else:
            print(f'Incorrecto. La respuesta correcta es: {correcto}')
    except (ValueError, IndexError):
        print('Opción no válida.')

if __name__ == '__main__':
    main()
