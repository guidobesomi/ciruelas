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

                    if nombre_parametros_input in datos_temporales:

                        parametros_input = datos_temporales[nombre_parametros_input]

                        if not (nombre_parametros_output == ''):

                            datos_temporales[nombre_parametros_output] = funcion(parametros_input)

                        else:

                            funcion(parametros_input)

                    else:

                        print u"\nFALTAN DATOS PARA REALIZAR ESTA ACCIÓN: %s" % nombre_parametros_input

                        time.sleep(1)

                else:

                    if not (nombre_parametros_output == ''):

                        datos_temporales[nombre_parametros_output] = funcion()

                    else:

                        funcion()

        elif choice == (len(menus[0]) - 1):

            print u"\nHAS ELEGIDO LA OPCIÓN %d: %s" % (len(menus[0]) - 1 , menus[0][len(menus[0])-1][3:])

            time.sleep(1)

            return False

        else:

            print u"\nESA NO ES UNA OPCIÓN VÁLIDA. VUELVE A INTENTARLO."

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

    return [calibre_promedio , kg_ha_secos_promedio]

def estimar_curva_produccion(calibre_kg_input_lista):

    calibre_promedio = calibre_kg_input_lista[0]
    kg_ha_secos_promedio = calibre_kg_input_lista[1]

    print "\nESTIMANDO..."

    time.sleep(1.5)

    # [] = estimar_parametros_curva(calibre_kg_lista[0],calibre_kg_lista[1])

    pendiente = 135.0
    corte = -25.0

    print u"\n¡LA ESTIMACIÓN HA SIDO LLEVADA A CABO EXITOSAMENTE!"

    time.sleep(0.7)

    print "\nPENDIENTE = " , pendiente
    print "PUNTO DE CORTE = " , corte

    time.sleep(1.5)

    return [pendiente , corte]

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

    time.sleep(1)

    return

def optimizar(pendiente_corte_lista):

    pendiente = pendiente_corte_lista[0]
    corte = pendiente_corte_lista[1]

    print "\nOPTIMIZANDO..."

    time.sleep(1.5)

    margen_bruto_final = 4500.0
    calibre_optimo = 73.0
    presion_optima = 3.6

    print u"\n¡LA OPTIMIZACIÓN HA SIDO LLEVADA A CABO EXITOSAMENTE!"

    time.sleep(0.7)

    print "\nMARGEN BRUTO FINAL = " , margen_bruto_final
    print "CALIBRE OPTIMO = " , calibre_optimo
    print "PRESION OPTIMA = " , presion_optima

    time.sleep(2)

    return [margen_bruto_final , calibre_optimo , presion_optima]

def graficar():

    print "\nGRAFICANDO..."

    time.sleep(0.5)

    X = np.arange(2000) / 10.0
    Y = X ** 2.0 + 3.0

    plt.plot(X,Y)
    plt.xlabel('EJE X')
    plt.ylabel('EJE Y')
    plt.title(u'CURVA DE INTERÉS')
    plt.grid(True)
    plt.show()

    return

def nada_por_ahora():

    return
# ------------------------------------------------------------------------------
# ---------------------------------- LOOP --------------------------------------
# ------------------------------------------------------------------------------

menu_principal = [u"MENÚ PRINCIPAL",u"1. CURVAS DE PRODUCCIÓN",u"2. MODELO DE OPTIMIZACIÓN",
                  u"3. GESTIÓN DE DATOS",u"4. OPCIÓN 4",u"5. SALIR"]
menu_1 = [u"MENÚ CURVAS DE PRODUCCIÓN",u"1. INGRESAR DATOS",
          u"2. ESTIMAR CURVA DE PRODUCCIÓN",u"3. GRAFICAR CURVA ESTIMADA",
          u"4. PREDECIR PRODUCCION",u"5. VOLVER AL MENÚ PRINCIPAL"]
menu_2 = [u"MENÚ MODELO DE OPTIMIZACIÓN",u"1. MAXIMIZAR MARGEN BRUTO FINAL",u"2. GRAFICAR",
          u"3. GRAFICAR",u"4. GRAFICAR",u"5. VOLVER AL MENÚ PRINCIPAL"]
menu_3 = [u"MENÚ GESTIÓN DE DATOS",u"1. AÑADIR DATOS A LA BASE",u"2. VISUALIZAR DATOS",
          u"3. VOLVER AL MENÚ PRINCIPAL"]

menus = [menu_principal,[menu_1,[],[],[],[]],[menu_2,[],[],[],[]],[menu_3,[],[]],[]]

funciones = {menu_1[1] : [ingresar_datos , '' , 'calibre_kg_input'] ,
             menu_1[2] : [estimar_curva_produccion , 'calibre_kg_input' , 'pendiente_corte_estimado'] ,
             menu_1[3] : [graficar_curva_estimada , 'pendiente_corte_estimado' , ''] ,
             menu_1[4] : [predecir_produccion , 'pendiente_corte_estimado' , ''] ,
             menu_2[1] : [optimizar , 'pendiente_corte_estimado' , 'output_optimizacion'] ,
             menu_2[2] : [graficar , '' , ''] ,
             menu_2[3] : [graficar , '' , ''] ,
             menu_2[4] : [graficar , '' , ''] ,
             menu_3[1] : [nada_por_ahora , '' , ''] ,
             menu_3[2] : [nada_por_ahora , '' , '']}

datos_temporales = {}

loop_menu(menus,funciones,datos_temporales)
