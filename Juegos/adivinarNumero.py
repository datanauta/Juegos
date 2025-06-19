import random

randomNum = random.randint(1, 25)
intents = 0

print('Intenta adivinar el número con 5 intentos')

while intents < 5:
    print(f'Intento {intents + 1}: ')

    try:
        intent = int(input('Introduce un número: '))
    except ValueError:
        print('Por favor, introduce un número válido.')
        continue  # No contar el intento inválido

    intents += 1

    if intent < randomNum:
        print('Tu intento es demasiado bajo.')
    elif intent > randomNum:
        print('Tu intento es demasiado alto.')
    else:
        print(f'¡Adivinaste el número! Era {randomNum}')
        break
else:
    print(f'Lo siento, se te acabaron los intentos. El número era {randomNum}')
