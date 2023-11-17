import os
import time
import random


def game(word):
    if word == "0":
        words = ["humanidad", "persona", "gente", "hombre", "mujer", "bebe", "adolescente", "cuerpo", "cabeza", "cabello", "diente", "cerebro", "muñeca", "trasero", "sangre", "familia", "amigo", "esposa", "matrimonio", "padre", "madre", "hermano", "nacimiento", "muerte", "bosque", "naturaleza", "desierto", "montaña", "perro", "gato", "elefante", "langosta", "saltamontes", "sardina", "cocodrilo", "alimento", "flor", "zanahoria", "durazno", "manzana", "tiempo", "segundo", "mañana", "ambiente", "domingo", "mundo", "galaxia", "universo", "lluvia", "tormenta", "metal", "oro", "plata", "cantidad", "sociedad", "comunidad", "empresa", "departamento", "democracia", "representante", "consumo", "dinero", "escritorio", "pantalla", "electricidad", "cremallera", "zapato", "camiseta", "falda", "vestido", "transporte", "carretera", "aeropuerto", "ambulancia", "coma", "diccionario", "computadora", "programacion", "rojo", "negro", "entretenimiento", "competencia", "esfuerzo", "contenido", "proyecto", "consecuencia", "defensa", "diferencia", "personalidad", "pensamiento", "improbable", "internacional", "delgado", "picante", "interesado", "sorprendido", "apestoso", "alcanzar", "interesarse", "encanto", "atemorizarse", "retroceder", "comenzar"]
        word = random.choice(words)
        del words
    lifes = 5
    number_characters = len(word)
    to_found = number_characters
    unknown = word
    for i in unknown:
             unknown = unknown.replace(i,"_ ")
    
    while to_found > 0 and lifes > 0:
        os.system("clear")
        print(unknown)
        character = input("\nQue letra?\n\n\t")
        character = character.lower()
        found = word.find(character)
        if found == -1:
            lifes -= 1
            print("\n\"" + str(character) + "\" no esta en la palabra.\n \nHas pedido una vida, te quedan: " + str(lifes))
            time.sleep(3)
        else:
            if character == "":
                print("\nNo has ingresado ninguna letra.\n \nIntenta nuevamente...")
                time.sleep(3)
            elif len(character) < 2:
                found = found * 2
                unknown = "".join((unknown[:found], character, unknown[found + 1:]))
                to_found -= 1
                found = found // 2
                found_second = word.find(character, found + 1)
                if found_second == -1:
                    pass
                else:
                    found_second = found_second * 2
                    unknown = "".join((unknown[:found_second], character, unknown[found_second +1:]))
                    to_found -= 1
            elif character == word:
                print("\nCorrecto! La palabra era \"" + word + "\". Felicitaciones!")
                time.sleep(5)
                run()
            else:
                lifes -= 1
                print("\nLa palabra no es \"" + character + "\".\n \nHas pedido una vida, te quedan: " + str(lifes))
                time.sleep(3)
    
    if to_found == 0:
        print("\nCorrecto! La palabra era \"" + word + "\". Felicitaciones!")
        time.sleep(5)
        run()
    else:
        print("\nTus vidas han llegado a 0.\nLa palabra era \"" + word + "\". pero haz perdido!")
        time.sleep(5)
        run()
                

    


def run():
    os.system("clear")
    print("Bienvenido al Ahorcado de H&G Games\n\nElija una opcion:\n")
    option = input("1 - Jugar contra la IA.\n\n2 - Multijugador.\n\n3 - Salir.\n\n\t")

    if option == "1":
        os.system("clear")
        print("La maquina piensa una palabra y coloca tantas rayas como letras tenga ésta.\n\nEl jugador tiene que adivinarla diciendo letras individuales hasta decifrarla.\n\nSin embargo, perdera una vida por cada intento fallido...")
        input("\n\n\nPresione Enter para continuar. . .")
        word = "0"
        game(word)
    elif option == "2":
        print("Un usuario ingresa una palabra y la computadora colocara tantas rayas como letras tenga ésta.\n\nEl segundo jugador tiene que adivinarla ingresando letras individuales hasta decifrarla.\n\nSin embargo, perdera una vida por cada intento fallido...")
        print("\n\nIngresa la palabra sin que el segundo jugador la vea:")
        word = input("\n\n\t")
        game(word)
    elif option == "3":
        print("\nGracias por confiar en nosotros.")
        exit()
    else:
        print("\nOpcion no valida. Vuelva a intentarlo...")
        time.sleep(3)
        run()


if __name__ == "__main__":
    run()

