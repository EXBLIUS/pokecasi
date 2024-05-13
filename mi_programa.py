
from random import randint
import random
import os
import readchar  # Import the readchar module

follow = None
TOTAL_WINS_LITTLE = 1
TOTAL_WINS_NORMAL = 2
TOTAL_WINS_MAX = 5
little_victories = "Haz ganado, conseguiste la medalla de bronce!"
normal_victories = "Haz ganado, conseguiste la medalla de oro!"
max_victories = "Haz ganado, conseguiste la medalla de mejor entrenador BRAVO!"
victory_l = False
victory_n = False
victory_m = False
victorias = []
POS_X = 0
POS_Y = 1
NUM_GAME_ITEMS = random.randint(11, 30)
my_position = [7, 0]
game_items = []
kind_fight = None
obstacle_definition = """\
#### ## ## ###  ###       #
####  # #    #    ##  ###  
##        ##### #    #   # 
#        #####    ##       
###        ##   ##    #####
      ###   #      #    ###
#   #   #   #   ####   ####
     ###   ###  ####      #
##       ###   ### #     ##
#  #     ##           ##   
  #####      #    ##    ## 
        ##     ####    ####
   ##  #        ####     ##
######     ###         ####
 ####   ####    ###   ### #\
"""
end_game = False
batalla_pokemon = "¡¡¡comienza la batalla!!!"

obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

while not end_game:
    print("Bienvenido a 'Ciudad portual'")
    os.system("cls")

    print("+" + "-" * MAP_WIDTH * 2 + "+")
    while len(game_items) < NUM_GAME_ITEMS:
        new_position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]

        if new_position not in game_items and new_position != my_position and \
                obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            game_items.append(new_position)

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = "  "
            object_in_cell = None

            for game_item in game_items:
                if game_item[POS_X] == coordinate_x and game_item[POS_Y] == coordinate_y:
                    char_to_draw = " !"
                    object_in_cell = game_item

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = " &"
                if object_in_cell:
                    kind_fight = 1

                    if kind_fight == 1:
                        print("\n\n\n\n{}, HA APARECIDO UN CASSIEL SALVAJE *PONE MUSICA EPICA* !!!\n".format(batalla_pokemon))
                        input("Enter para continuar")
                        os.system("cls")
                        PS_CHARMANDER_INICIAL = 85
                        PS_SQUIRTLE_INICIAL = 100

                        TAMAÑO_BARRA_PS = 20

                        ps_charmander_actual = PS_CHARMANDER_INICIAL
                        ps_squirtle_actual = PS_SQUIRTLE_INICIAL

                        while ps_charmander_actual > 0 and ps_squirtle_actual > 0:
                            os.system("cls")
                            # comienza la batalla

                            # turno Charmander
                            print("\nTurno de CASSIEL\n")
                            ataque_charmander = randint(1, 3,)

                            if ataque_charmander == 1:
                                print("CASSIEL ataca con (llanto falso)")
                                ps_squirtle_actual -= 12
                            if ataque_charmander == 2:
                                print("CASSIEL ataca con (erecccion)")
                                ps_squirtle_actual -= 7
                            if ataque_charmander == 3:
                                print("CASSIEL ataca con (salmonela)")
                                ps_squirtle_actual -= 20

                            barra_de_ps_charmander = int(
                                ps_charmander_actual * TAMAÑO_BARRA_PS / PS_CHARMANDER_INICIAL)
                            print("\nLos ps de CASSIEL son:[{}{}] ({}/{})\n".format("*" * barra_de_ps_charmander,
                                                                                      " " * (
                                                                                              TAMAÑO_BARRA_PS - barra_de_ps_charmander),
                                                                                      ps_charmander_actual,
                                                                                      PS_CHARMANDER_INICIAL))

                            barra_de_ps_squirtle = int(ps_squirtle_actual * TAMAÑO_BARRA_PS / PS_SQUIRTLE_INICIAL)
                            print(
                                "\nLos ps de Squirtle es[{}{}] ({}/{})\n".format("*" * barra_de_ps_squirtle, " " * (
                                        TAMAÑO_BARRA_PS - barra_de_ps_squirtle), ps_squirtle_actual,
                                                                                 PS_SQUIRTLE_INICIAL))

                            input("\nEnter para continuar...\n")
                            os.system("cls")
                            print("Tu turno, elije el ataque de Squirtle")

                            ataque_squirtle = None

                            while ataque_squirtle not in ["A", "B", "C", "N", "F"]:
                                ataque_squirtle = input("\n¿Que ataque deseas realizar?\n"
                                                        "(A) squirt (-30 ps)\n"
                                                        "(B) pistola de leche OMG (-11 ps)\n"
                                                        "(C) pole dance (-50ps)\n"
                                                        "(F) decirle algo a CASSIEL"
                                                        "(H) cocazoQq"
                                                        "(N) No hacer nada\n"
                                                        )

                                if ataque_squirtle == "A":
                                    print("Squirtle ataca con su concha OHHHHHHH")
                                    ps_charmander_actual -= 30

                                elif ataque_squirtle == "B":
                                    print("Squirtle ataca con su pija")
                                    ps_charmander_actual -= 11

                                elif ataque_squirtle == "C":
                                    print("CASSIEL se pone feliz, un golpe critico!!!!")
                                    ps_charmander_actual -= 50
                                elif ataque_squirtle == "H":
                                    print("le da un golpe en la cabeza y se le empieza a salir la yema")
                                    ps_charmander_actual -= 100
                                elif ataque_squirtle == "F":
                                    frase_a_decir = randint (1, 2)
                                    if frase_a_decir == 2:
                                        frase_a_decir = "Soy Pedro"
                                    if frase_a_decir == 1:
                                        frase_a_decir = "no te quiere ni la de lanzarote\nDE ESTA NO SE RECUPERARA NUNCA XD"

                                    print(frase_a_decir)
                                    ps_charmander_actual -= 100
                                elif ataque_squirtle == "N":
                                    print("SQUIRTle no hace nada")
                                    ps_charmander_actual = ps_charmander_actual

                                if ps_squirtle_actual < 0:
                                    ps_squirtle_actual = 0
                                if ps_charmander_actual < 0:
                                    ps_charmander_actual = 0

                            barra_de_ps_charmander = int(
                                ps_charmander_actual * TAMAÑO_BARRA_PS / PS_CHARMANDER_INICIAL)
                            print("\nLos ps de CASSIEL es:[{}{}] ({}/{})\n".format("*" * barra_de_ps_charmander,
                                                                                      " " * (
                                                                                              TAMAÑO_BARRA_PS - barra_de_ps_charmander),
                                                                                      ps_charmander_actual,
                                                                                      PS_CHARMANDER_INICIAL))

                            barra_de_ps_squirtle = int(ps_squirtle_actual * TAMAÑO_BARRA_PS / PS_SQUIRTLE_INICIAL)
                            print(
                                "\nLos ps de Squirtle es[{}{}] ({}/{})\n".format("*" * barra_de_ps_squirtle, " " * (
                                        TAMAÑO_BARRA_PS - barra_de_ps_squirtle), ps_squirtle_actual,
                                                                                 PS_SQUIRTLE_INICIAL))

                            input("\nEnter para continuar...\n")
                            os.system("cls")

                        if ps_charmander_actual > ps_squirtle_actual:
                            print("\nTe a ganado cassiel jajajaja, QUE NOOB\n")
                            game_items.remove(object_in_cell)

                        elif ps_squirtle_actual > ps_charmander_actual:
                            print("\nFELICIDADES, has derrotado a un VIRGEN!!!!\n")
                            game_items.remove(object_in_cell)
                            victorias.append(object_in_cell)

                    if kind_fight == 2:
                        print("\n\n\n\n{}, los pokemones son Pikachu y Squirtle!!!\n".format(batalla_pokemon))
                        input("Enter para continuar...")
                        os.system("cls")
                        PS_PIKACHU_INICIAL = 80
                        PS_SQUIRTLE_INICIAL = 95

                        TAMAÑO_BARRA_PS = 20

                        ps_pikachu_actual = PS_PIKACHU_INICIAL
                        ps_squirtle_actual = PS_SQUIRTLE_INICIAL

                        while ps_pikachu_actual > 0 and ps_squirtle_actual > 0:
                            os.system("cls")
                            # comienza la batalla

                            # Turno pikachu
                            print("\nTurno de Pikachu\n")
                            ataque_pikachu = randint(1, 2)

                            if ataque_pikachu == 1:
                                print("Pikachu ataca con (impactrueno)")
                                ps_squirtle_actual -= 12
                            else:
                                print("Pikachu ataca con (cola de acero)")
                                ps_squirtle_actual -= 9

                            barra_de_ps_pikachu = int(ps_pikachu_actual * TAMAÑO_BARRA_PS / PS_PIKACHU_INICIAL)
                            print("\nLos ps de Pikachu es:[{}{}] ({}/{})\n".format("*" * barra_de_ps_pikachu, " " * (
                                    TAMAÑO_BARRA_PS - barra_de_ps_pikachu), ps_pikachu_actual, PS_PIKACHU_INICIAL))

                            barra_de_ps_squirtle = int(ps_squirtle_actual * TAMAÑO_BARRA_PS / PS_SQUIRTLE_INICIAL)
                            print(
                                "\nLos ps de Squirtle es[{}{}] ({}/{})\n".format("*" * barra_de_ps_squirtle, " " * (
                                        TAMAÑO_BARRA_PS - barra_de_ps_squirtle), ps_squirtle_actual,
                                                                                 PS_SQUIRTLE_INICIAL))

                            input("\nEnter para continuar...\n")
                            os.system("cls")
                            print("Tu turno, elije el ataque de Squirtle")

                            ataque_squirtle = None

                            while ataque_squirtle not in ["A", "B", "C", "N"]:
                                ataque_squirtle = input("\n¿Que ataque deseas realizar?\n"
                                                        "(A) placaje (-10 ps)\n"
                                                        "(B) pistola agua (-8 ps)\n"
                                                        "(C) burbujas (-7 ps)\n"
                                                        "(N) No hacer nada\n"
                                                        )

                                if ataque_squirtle == "A":
                                    print("Tu squirtle ataca con (placaje)")
                                    ps_pikachu_actual -= 10

                                elif ataque_squirtle == "B":
                                    print("Tu squirtle ataca con (pistola de agua)")
                                    ps_pikachu_actual -= 8

                                elif ataque_squirtle == "C":
                                    print("Tu squirtle ataca con (burbujas)")
                                    ps_pikachu_actual -= 7
                                elif ataque_squirtle == "N":
                                    print("Squirtle no hace nada")
                                    ps_pikachu_actual = ps_pikachu_actual

                                if ps_squirtle_actual < 0:
                                    ps_squirtle_actual = 0
                                if ps_pikachu_actual < 0:
                                    ps_pikachu_actual = 0

                            barra_de_ps_pikachu = int(ps_pikachu_actual * TAMAÑO_BARRA_PS / PS_PIKACHU_INICIAL)
                            print("\nLos ps de Pikachu es:[{}{}] ({}/{})\n".format("*" * barra_de_ps_pikachu, " " * (
                                    TAMAÑO_BARRA_PS - barra_de_ps_pikachu), ps_pikachu_actual, PS_PIKACHU_INICIAL))

                            barra_de_ps_squirtle = int(ps_squirtle_actual * TAMAÑO_BARRA_PS / PS_SQUIRTLE_INICIAL)
                            print(
                                "\nLos ps de Squirtle es[{}{}] ({}/{})\n".format("*" * barra_de_ps_squirtle, " " * (
                                        TAMAÑO_BARRA_PS - barra_de_ps_squirtle), ps_squirtle_actual,
                                                                                 PS_SQUIRTLE_INICIAL))

                            input("\nEnter para continuar...\n")
                            os.system("cls")

                        if ps_pikachu_actual > ps_squirtle_actual:
                            print("\nPikachu gana, haz perdido el combate\n")
                            game_items.remove(object_in_cell)

                        elif ps_squirtle_actual > ps_pikachu_actual:
                            print("\nSquirtle gana, FELICIDADES!\n")
                            game_items.remove(object_in_cell)
                            victorias.append(object_in_cell)

                    if kind_fight == 3:
                        print("\n\n\n\n{}, los pokemones son Bulbasaur y Squirtle!!!\n".format(batalla_pokemon))
                        input("Enter para continuar...")
                        os.system("cls")
                        PS_BULBASAUR_INICIAL = 85
                        PS_SQUIRTLE_INICIAL = 95

                        TAMAÑO_BARRA_PS = 20

                        ps_bulbasaur_actual = PS_BULBASAUR_INICIAL
                        ps_squirtle_actual = PS_SQUIRTLE_INICIAL

                        while ps_bulbasaur_actual > 0 and ps_squirtle_actual > 0:
                            os.system("cls")
                            # comienza la batalla

                            # Turno de Bulbasaur
                            print("\nTurno de Bulbasaur\n")
                            ataque_bulbasaur = randint(1, 2)

                            if ataque_bulbasaur == 1:
                                print("Bulbasaur ataca con (Latigazo)")
                                ps_squirtle_actual -= 10
                            else:
                                print("Bulbasaur ataca con (Bomba lodo)")
                                ps_squirtle_actual -= 8

                            barra_de_ps_bulbasaur = int(
                                ps_bulbasaur_actual * TAMAÑO_BARRA_PS / PS_BULBASAUR_INICIAL)
                            print("\nLos ps de Bulbasaur es:[{}{}] ({}/{})\n".format("*" * barra_de_ps_bulbasaur,
                                                                                     " " * (
                                                                                             TAMAÑO_BARRA_PS - barra_de_ps_bulbasaur),
                                                                                     ps_bulbasaur_actual,
                                                                                     PS_BULBASAUR_INICIAL))

                            barra_de_ps_squirtle = int(ps_squirtle_actual * TAMAÑO_BARRA_PS / PS_SQUIRTLE_INICIAL)
                            print(
                                "\nLos ps de Squirtle es[{}{}] ({}/{})\n".format("*" * barra_de_ps_squirtle, " " * (
                                        TAMAÑO_BARRA_PS - barra_de_ps_squirtle), ps_squirtle_actual,
                                                                                 PS_SQUIRTLE_INICIAL))

                            input("\nEnter para continuar...\n")
                            os.system("cls")
                            print("Tu turno, elije el ataque de Squirtle")

                            ataque_squirtle = None

                            while ataque_squirtle not in ["A", "B", "C", "N"]:
                                ataque_squirtle = input("\n¿Que ataque deseas realizar?\n"
                                                        "(A) placaje (-10 ps)\n"
                                                        "(B) pistola agua (-7 ps)\n"
                                                        "(C) burbujas (-8 ps)\n"
                                                        "(N) No hacer nada\n"
                                                        )

                                if ataque_squirtle == "A":
                                    print("Tu squirtle ataca con (placaje)")
                                    ps_bulbasaur_actual -= 10

                                elif ataque_squirtle == "B":
                                    print("Tu squirtle ataca con (pistola de agua)")
                                    ps_bulbasaur_actual -= 7

                                elif ataque_squirtle == "C":
                                    print("Tu squirtle ataca con (burbujas)")
                                    ps_bulbasaur_actual -= 8
                                elif ataque_squirtle == "N":
                                    print("Squirtle no hace nada")
                                    ps_bulbasaur_actual = ps_bulbasaur_actual

                                if ps_squirtle_actual < 0:
                                    ps_squirtle_actual = 0
                                if ps_bulbasaur_actual < 0:
                                    ps_bulbasaur_actual = 0

                            barra_de_ps_bulbasaur = int(
                                ps_bulbasaur_actual * TAMAÑO_BARRA_PS / PS_BULBASAUR_INICIAL)
                            print("\nLos ps de Bulbasaur es:[{}{}] ({}/{})\n".format("*" * barra_de_ps_bulbasaur,
                                                                                     " " * (
                                                                                             TAMAÑO_BARRA_PS - barra_de_ps_bulbasaur),
                                                                                     ps_bulbasaur_actual,
                                                                                     PS_BULBASAUR_INICIAL))

                            barra_de_ps_squirtle = int(ps_squirtle_actual * TAMAÑO_BARRA_PS / PS_SQUIRTLE_INICIAL)
                            print(
                                "\nLos ps de Squirtle es[{}{}] ({}/{})\n".format("*" * barra_de_ps_squirtle, " " * (
                                        TAMAÑO_BARRA_PS - barra_de_ps_squirtle), ps_squirtle_actual,
                                                                                 PS_SQUIRTLE_INICIAL))

                            input("\nEnter para continuar...\n")
                            os.system("cls")

                        if ps_bulbasaur_actual > ps_squirtle_actual:
                            print("\nBulbasaur gana, haz perdido el combate\n")
                            game_items.remove(object_in_cell)
                        elif ps_squirtle_actual > ps_bulbasaur_actual:
                            print("\nSquirtle gana, FELICIDADES!\n")
                            game_items.remove(object_in_cell)
                            victorias.append(object_in_cell)

                    input("\nDoble Enter para continuar...\n")
                if len(victorias) == TOTAL_WINS_LITTLE:
                    victory_l = True
                elif len(victorias) == TOTAL_WINS_NORMAL:
                    victory_n = True
                elif len(victorias) == TOTAL_WINS_MAX:
                    victory_n = True
                    end_game = True
            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = " #"

            print("{}".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 2 + "+")

    # direction=input("Donde te quieres mover? [WASD]")
    direction = readchar.readchar()

    new_position = None
    if direction == "w" or direction == "W":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]

    elif direction == "s" or direction == "S":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]

    elif direction == "a" or direction == "A":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "d" or direction == "D":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "q" or direction == "Q":
        end_game = True

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            my_position = new_position

if victory_l:
    follow_1 = input("{}\n".format(little_victories))
elif victory_n:
    follow_2 = input("{}\n".format(normal_victories))
elif victory_m:
    print("{}".format(max_victories))
