import random

# Cargar palabras desde el archivo
sourceDir = "C:/Users/Usuario/Desktop/Python/Juegos/peliculas.txt"

with open(sourceDir, encoding='utf-8') as f:
    words = [line.strip() for line in f if line.strip()]  # Eliminar líneas vacías

# Elegir una palabra aleatoria
word = random.choice(words)

errors = 4
guessed_letters = []
run = True

print("🎬 Adivina la película")

while run:
    display_word = ''
    for letter in word:
        if letter.lower() in guessed_letters or not letter.isalpha():
            display_word += letter  # Mostrar espacios o símbolos
        else:
            display_word += '_'

    print("\nPalabra: " + ' '.join(display_word))

    if '_' not in display_word:
        print(f"✅ ¡Correcto! La palabra era: {word}")
        break

    print(f"❌ Errores restantes: {errors}")
    guess = input("👉 Intenta una letra: ").strip().lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Introduce solo una letra válida.")
        continue

    if guess in guessed_letters:
        print("Ya usaste esa letra.")
        continue

    guessed_letters.append(guess)

    if guess not in word.lower():
        errors -= 1
        if errors == 0:
            print(f"💀 ¡Game over! La palabra era: {word}")
            break
