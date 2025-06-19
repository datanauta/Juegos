def crear_historia():
    print("¡Vamos a crear tu historia personalizada!\nPor favor, responde las siguientes preguntas:\n")

    nombre = input("Nombre del protagonista: ")
    lugar = input("Lugar mágico: ")
    objeto = input("Objeto misterioso: ")
    criatura = input("Criatura fantástica: ")
    verbo = input("Verbo en infinitivo (como correr, saltar, explorar): ")
    adjetivo = input("Adjetivo (como valiente, loco, brillante): ")

    historia = f"""
    Había una vez un(a) {adjetivo} aventurero/a llamado/a {nombre}, que vivía en un pequeño pueblo cerca de {lugar}.
    Un día, mientras caminaba por el bosque, encontró un {objeto} brillante escondido bajo una roca.
    Sin saberlo, ese objeto era la clave para despertar a un(a) {criatura} dormido/a por siglos.
    {nombre} decidió {verbo} hacia lo desconocido, enfrentándose a peligros y misterios.
    Al final, gracias a su valentía, logró cambiar el destino del mundo mágico de {lugar} para siempre.
    """

    print("\n--- Tu Historia ---")
    print(historia)

if __name__ == "__main__":
    crear_historia()

