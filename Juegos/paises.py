from Juegos.juegoconpygame import score

capitals = {
    "Argentina":"Buenos Aires",
    "Mexico":"Ciudad de México",
    "Colombia":"Bogota",
    "Perú":"Lima",
    "Chile":"Santiago",
    "España":"Madrid"
}

def quiz_capitals():

    print('Bienvenido al custionario de capitales del mundo')
    score = 0

    for country, capital in capitals.items():
        print(f'Pregunta:¿Cual es la capital de {country}')
        user_answer = input('Tu respuesta:')

        if user_answer.lower() == capital.lower():
            print('Correcto. Has ganado un punto')
            score += 1
        else:

            print(f'Respuesta incorrecta. La capital de {country} es {capital}\n')
    print(f'Tu puntuacion final es :{score}/len({capitals})')

quiz_capitals()