# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import time

# ------------------------------------------------------------------------------
# ------------------------------- FUNCIONES ------------------------------------
# ------------------------------------------------------------------------------

# --------------------------------- MENÚS --------------------------------------

def print_menu(menu):

    comillas_antes = int(np.floor((66 - len(menu[0])) / 2.0)) - 1
    comillas_despues = int(np.ceil((66 - len(menu[0])) / 2.0)) - 1

    time.sleep(0.3)

    print '\n'

    print  comillas_antes  * "-" , menu[0] , comillas_despues * "-"

    time.sleep(0.3)

    for i in range(len(menu)-1):

        print menu[i+1]

        time.sleep(0.1)

    print 66 * "-"

    time.sleep(0.1)

    return

def loop_menu(menus,funciones,datos_temporales):

    loop = True

    while loop:

        print_menu(menus[0])

        loop = loop_interno(menus,funciones,datos_temporales)

    return

def loop_interno(menus,funciones,datos_temporales):

    prompt = '> '

    loop = True

    while loop:

        print u"\nINGRESE SU ELECCIÓN [1-%d] Y LUEGO PRESIONE 'ENTER':\n" % (len(menus[0]) - 1)

        choice = raw_input(prompt)

        if choice.isdigit():

            choice = int(choice)

        else:

            choice = 0

        if (choice - 1) in range(len(menus[0]) - 2):

            print u"\nHAS ELEGIDO LA OPCIÓN %d: %s" % (choice , menus[0][choice][3:])

            time.sleep(0.7)

            if not (menus[choice] == []):

                loop = loop_menu(menus[choice],funciones,datos_temporales)

            else:

                funcion = funciones[menus[0][choice]][0]

                nombre_parametros_input = funciones[menus[0][choice]][1]

                nombre_parametros_output = funciones[menus[0][choice]][2]

                if not (nombre_parametros_input == ''):

                    #FALTA VER EL CASO EN QUE NO SE HAN AGREGADO LOS PARAMETROS TODAVIA
                    parametros_input = datos_temporales[nombre_parametros_input]

                    if not (nombre_parametros_output == ''):

                        datos_temporales[nombre_parametros_output] = funcion(parametros_input)

                    else:

                        funcion(parametros_input)

                else:

                    if not (nombre_parametros_output == ''):

                        datos_temporales[nombre_parametros_output] = funcion()

                    else:

                        funcion()

        if choice == (len(menus[0]) - 1):

            print u"\nHAS ELEGIDO LA OPCIÓN %d: %s" % (len(menus[0]) - 1 , menus[0][len(menus[0])-1][3:])

            time.sleep(1)

            return False

        if not ((choice - 1) in range(len(menus[0]) - 1)):

            print u"\nESA NO ES UNA OPCCIÓN VÁLIDA. VUELVE A INTENTARLO."

            time.sleep(1)

        return True

# -------------------------------- OPCIONES ------------------------------------

def ingresar_datos():

    prompt = '> '

    print u"\nINGRESE EL CALIBRE PROMEDIO:\n"

    calibre_promedio = float(raw_input(prompt))

    print u"\nINGRESE LOS KILOS SECOS POR HECTÁREA:\n"

    kg_ha_secos_promedio = float(raw_input(prompt))

    print u"\n¡LOS DATOS HAN SIDO INGRESADOS EXITOSAMENTE!"

    time.sleep(0.7)

    return [calibre_promedio,kg_ha_secos_promedio]

def estimar_curva_produccion(calibre_kg_input_lista):

    calibre_promedio = calibre_kg_input_lista[0]
    kg_ha_secos_promedio = calibre_kg_input_lista[1]

    print "\nESTIMANDO...\n"

    time.sleep(1.5)

    # [] = estimar_parametros_curva(calibre_kg_lista[0],calibre_kg_lista[1])

    pendiente = 1.0
    corte = -2.0

    print u"\n¡LA ESTIMACIÓN HA SIDO LLEVADA A CABO EXITOSAMENTE!\n"

    time.sleep(0.7)

    print "PENDIENTE = " , pendiente
    print "PUNTO DE CORTE = " , corte

    return [pendiente,corte]

def graficar_curva_estimada(pendiente_corte_lista):

    pendiente = pendiente_corte_lista[0]
    corte = pendiente_corte_lista[1]

    print "\nGRAFICANDO..."

    time.sleep(0.5)

    X = np.arange(2000) / 10.0
    Y = pendiente * X + corte

    plt.plot(X,Y)
    plt.xlabel('calibre medio')
    plt.ylabel('kg secos por ha')
    plt.title(u'CURVA DE PRODUCCIÓN')
    plt.grid(True)
    plt.show()

    return

def predecir_produccion(pendiente_corte_lista):

    pendiente = pendiente_corte_lista[0]
    corte = pendiente_corte_lista[1]

    prompt = '> '

    print "\nINGRESE UN CALIBRE:\n"

    calibre = float(raw_input(prompt))

    time.sleep(0.5)

    print u"\nLOS KILOS SECOS POR HECTÁREA ESTIMADOS SON: %d KG/HA\n" % (corte + pendiente * calibre)

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

menus = [menu_principal,[menu_1,[],[],[],[]],[menu_2,[],[],[],[]],[],[]]

funciones = {menu_1[1]:[ingresar_datos,'','calibre_kg_input'],
             menu_1[2]:[estimar_curva_produccion,'calibre_kg_input','pendiente_corte_estimado'],
             menu_1[3]:[graficar_curva_estimada,'pendiente_corte_estimado',''],
             menu_1[4]:[predecir_produccion,'pendiente_corte_estimado','']}

datos_temporales = {}

loop_menu(menus,funciones,datos_temporales)
