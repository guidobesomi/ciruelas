# -*- coding: utf-8 -*-

import numpy as np

# ------------------------------------------------------------------------------
# ------------------------------- FUNCIONES ------------------------------------
# ------------------------------------------------------------------------------

# --------------------------------- MENÚS --------------------------------------

def print_menu(menu):

    comillas_antes = int(np.floor((66 - len(menu[0])) / 2.0)) - 1
    comillas_despues = int(np.ceil((66 - len(menu[0])) / 2.0)) - 1

    print '\n'
    print  comillas_antes  * "-" , menu[0] , comillas_despues * "-"

    for i in range(len(menu)-1):

        print menu[i+1]

    print 66 * "-"

    return

def loop_interno_menu_1(menus):

    prompt = '> '

    while True:

        print u"\nINGRESE SU ELECCIÓN [1-5] Y LUEGO PRESIONE 'ENTER':"

        choice = int(raw_input(prompt))

        if choice == 1:

            print u"\nHAS ELEGIDO LA OPCIÓN 1: INGRESAR DATOS"

        elif choice == 2:

            print u"\nHAS ELEGIDO LA OPCIÓN 2:"

        elif choice == 3:

            print u"\nHAS ELEGIDO LA OPCIÓN 3:"

        elif choice == 4:

            print u"\nHAS ELEGIDO LA OPCIÓN 4:"

        elif choice == 5:

            print u"\nHAS ELEGIDO LA OPCIÓN 5: VOLVER ATRÁS"

            return False

        else:

            print u"\nESA NO ES UNA OPCCIÓN VÁLIDA. VUELVE A INTENTARLO."

def loop_menu_1(menus):

    loop = True

    while loop:

        print_menu(menus[0])

        loop = loop_interno_menu_1(menus)

    return False

def loop_interno_menu_2(menus):

    prompt = '> '

    while True:

        print u"\nINGRESE SU ELECCIÓN [1-3] Y LUEGO PRESIONE 'ENTER':"

        choice = int(raw_input(prompt))

        if choice == 1:

            print u"\nHAS ELEGIDO LA OPCIÓN 1:"

        elif choice == 2:

            print u"\nHAS ELEGIDO LA OPCIÓN 2:"

        elif choice == 3:

            print u"\nHAS ELEGIDO LA OPCIÓN 3: VOLVER ATRÁS"

            return False

        else:

            print u"\nESA NO ES UNA OPCCIÓN VÁLIDA. VUELVE A INTENTARLO."

def loop_menu_2(menus):

    loop = True

    while loop:

        print_menu(menus[0])

        loop = loop_interno_menu_2(menus)

    return False

def loop_interno_menu_principal(menus):

    prompt = '> '

    loop = True

    while loop:

        print u"\nIngrese su elección [1-5] y luego presione ENTER:\n"

        choice = int(raw_input(prompt))

        if choice == 1:

            print u"\nHAS ELEGIDO LA OPCIÓN 1"

            loop = loop_menu_1(menus[1:2])

        elif choice == 2:

            print u"\nHAS ELEGIDO LA OPCIÓN 2"

            loop = loop_menu_2(menus[2:])

        elif choice == 3:

            print u"\nHAS ELEGIDO LA OPCIÓN 3"
            ## You can add your code or functions here

        elif choice == 4:

            print u"\nHAS ELEGIDO LA OPCIÓN 4"
            ## You can add your code or functions here

        elif choice == 5:

            print u"\nHAS ELEGIDO LA OPCIÓN 5"

            return False # This will make the while loop to end as not value of loop is set to False

        else:

            print u"\nESA NO ES UNA OPCCIÓN VÁLIDA. VUELVE A INTENTARLO."

    return True

def loop_menu_principal(menus):

    loop = True

    while loop:

        print_menu(menus[0])

        loop = loop_interno_menu_principal(menus)

    return

# ------------------------------------------------------------------------------
# ---------------------------------- LOOP --------------------------------------
# ------------------------------------------------------------------------------

menu_principal = [u"MENÚ PRINCIPAL",u"1. CURVAS DE PRODUCCIÓN",u"2. OPCIÓN 2",
                  u"3. OPCIÓN 3",u"4. OPCIÓN 4",u"5. SALIR"]
menu_1 = [u"MENÚ CURVAS DE PRODUCCIÓN",u"1. INGRESAR DATOS",
          u"2. ESTIMAR CURVA DE PRODUCCIÓN",u"3. GRAFICAR CURVA ESTIMADA",
          u"4. PREDECIR PRODUCCION",u"5. VOLVER AL MENÚ PRINCIPAL"]
menu_2 = [u"MENÚ 2",u"1. OPCIÓN 1",u"2. OPCIÓN 2",
          u"3. OPCIÓN 3",u"4. OPCIÓN 4",u"5. VOLVER AL MENÚ PRINCIPAL"]

menus = [menu_principal,menu_1,menu_2]

loop_menu_principal(menus)
