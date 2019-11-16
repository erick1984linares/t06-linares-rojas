#CONDICIONALES-SIMPLES

import os
#CALCULADORA DE LA VELOCIDAD FINAL DE UN MOVIL
#input
velocidad_inicial = int(os.sys.argv[1])
aceleracion = int(os.sys.argv[2])
tiempo = int(os.sys.argv[3])

#processing
velocidad_final = velocidad_inicial+(aceleracion*tiempo)

#verificador
alta_velocidad=(velocidad_final > 200)

#output
print("                                                    ")
print("####################################################")
print("#    CALCULADORA DE VELOCIDAD FINAL DE UN MOVIL    #")
print("####################################################")
print("# Velocidad inicial    :" , velocidad_inicial)
print("# Aceleracion          :" , aceleracion)
print("# Tiempo               :" , tiempo)
print("#--------------------------------------------------#")
print("# Velocidad final del auto :  ", velocidad_final,"km/h")
print("####################################################")


#condicion simple
#si la velocidad es mayor que 200 mostrar advertencia
if (alta_velocidad == True ):
    print("                VAS COMO UN RAYO!!!              ")
#FIN_IF

import os
#CALCULADORA DEL AREA DE UN TRAPECIO
#input
base_mayor=int(os.sys.argv[1])
base_menor=int(os.sys.argv[2])
altura=int(os.sys.argv[3])

#processing
area=((base_mayor+base_menor)*altura)/2

#verificador
area_pequenia=(area<100)

#output
print("                                            ")
print("############################################")
print("#    CALCULADORA DEL AREA DE UN TRAPECIO   #")
print("############################################")
print("# Base mayor:", base_mayor)
print("# Base menor:", base_menor)
print("# Altura    :", altura)
print("#------------------------------------------#")
print("# El valor del area del trapecio es:", area)
print("############################################")


#condicion simple
#si el area es pequeña mostrar
if (area_pequenia == False):
    print("           ESTA AREA ES SUFICIENTE        ")
#FIN_IF

import os
#CALCULADORA DE INDICE DE MASA CORPORAL
#input
peso=float(os.sys.argv[1])
altura=float(os.sys.argv[2])

#processing
imc=peso/altura**2

#verificador
sobrepeso=(imc >= 25)

#output
print("                                                 ")
print("#################################################")
print("#    CALCULADORA DE INDICE DE MASA CORPORAL     #")
print("#################################################")
print("# El valor del peso es:",peso,"kg")
print("# El valor de la altura es:",altura,"m")
print("#-----------------------------------------------#")
print("# El valor del IMC es:", imc)
print("#################################################")
print("El valor normal oscila entre 18.5 - 24.9")
print("mas que eso es obesidad, menos significa delgadez")
print("#################################################")


#condicion simple
#si la persona tiene sobrepeso mostrar
if (sobrepeso == True):
    print(">> USTED AH DESBLOQUEADO NUESTRA DIETA EXCLUSIVA <<")
#FIN_IF

import os
#CALCULADORA DE AHORRO
#input
dinero_inicial=float(os.sys.argv[1])
dinero_mensual=float(os.sys.argv[2])
meses=float(os.sys.argv[3])

#processing
dinero_final=dinero_inicial+(dinero_mensual*meses)

#verificador
ahorro_alto=(dinero_final > 1000)

#output
print("                                                        ")
print("########################################################")
print("#           CALCULADORA DE AHORRO DE DINERO            #")
print("########################################################")
print("# El valor del dinero inicial es:",dinero_inicial,"s/.")
print("# El valor del dinero ahorrado por mes es:",dinero_mensual,"s/.")
print("# El numero de meses a ahorrar es:", meses)
print("#------------------------------------------------------#")
print("# El dinero total al final del ahorro es de:",dinero_final,"s/.")
print("########################################################")

#condicional simple
#si el  ahorro es alto mostrar el siguiente mensaje
if (ahorro_alto == True):
    print("       Usted ha ganado una tarjeta debito premium     ")
    print("                >>>> FELICIDADES <<<<                 ")
#FIN_IF

import os
#CALCULADORA DE PRESION HIDROSTATICA DE UN CUERPO SUMERGIDO
#input
densidad_liquido=float(os.sys.argv[1])
gravedad=float(os.sys.argv[2])
profundidad=float(os.sys.argv[3])

#processing
presion_hidrostatica=densidad_liquido*gravedad*profundidad

#verificador
presion_alta=(presion_hidrostatica>400)

#output
print("                                                              ")
print("##############################################################")
print("# CALCULADORA DE PRESION HIDROSTATICA DE UN CUERPO SUMERGIDO #")
print("##############################################################")
print("# El valor de la densidad del liquido es:",densidad_liquido)
print("# El valor de la gravedad es:",gravedad)
print("# El valor de la profundidad es:",profundidad)
print("#------------------------------------------------------------#")
print("# La presion hidrostatica a la que esta sometida el")
print("# cuerpo es de:",presion_hidrostatica)
print("##############################################################")


#condicion simple
#si la presion es muy alta mostrar
if (presion_alta == True):
    print("             CUIDADO LA PRESION ES MUY ALTA !!         ")
#FIN_IF

import os
#CALCULADORA DE DILATACION LINEAL
#input
longitud=float(os.sys.argv[1])
coef=float(os.sys.argv[2])
variacion_temp=float(os.sys.argv[3])

#processing
dilatacion_lineal=longitud*coef*variacion_temp
longitud_final=longitud+dilatacion_lineal

#verificador
mucha_dilatacion=(dilatacion_lineal>0.5)

#output
print("                                                            ")
print("############################################################")
print("#            CALCULADORA DE DILATACION LINEAL              #")
print("############################################################")
print("# El valor de la longitud inicial de la varilla es:",longitud,"m")
print("# El valor de la variacion de la temperatura es:",variacion_temp,"C")
print("# El valor del coeficiente de dilatacion es:",coef)
print("#----------------------------------------------------------#")
print("# La dilatacion de la varilla es:",dilatacion_lineal,"m")
print("# La longitud final de la varilla es:",longitud_final,"m")
print("############################################################")

#condicion simple
#si la dilatacion lineal es alta mostrar
if (mucha_dilatacion == True):
    print("              LA DILATACION ES EXCESIVA           ")
#FIN_IF

import os
#CALUCLADORA DEL TRABAJO SOBRE UN OBJETO
#Input
masa=float(os.sys.argv[1])
aceleracion=float(os.sys.argv[2])
distancia=float(os.sys.argv[3])

#Processing
fuerza=(masa*aceleracion)
trabajo=(fuerza*distancia)

#verificador
trabajo_alto=(trabajo > 5000)

#Output
print("                                                            ")
print("############################################################")
print("#    CALCULADORA DEL TRABAJO REALIZADO SOBRE UN OBJETO     #")
print("############################################################")
print("# El valor de la masa es:        ",masa)
print("# El valor de la aceleracion es: ", aceleracion)
print("# El valor de la distancia es:   ", distancia)
print("# El valor de la fuerza ejercida es: ", fuerza)
print("#----------------------------------------------------------#")
print("# El valor del trabajo realizado es: ", trabajo)
print("############################################################")

#condicion simple
#Si el trabajo es alto mostrar
if (trabajo_alto == False):
    print("                 HACE FALTA MAS POTENCIA             ")
#FIN_IF



#CONDICIONALES-SIMPLES

import os
#CALCULADORA DE LA VELOCIDAD FINAL DE UN MOVIL
#input
velocidad_inicial = int(os.sys.argv[1])
aceleracion = int(os.sys.argv[2])
tiempo = int(os.sys.argv[3])

#processing
velocidad_final = velocidad_inicial+(aceleracion*tiempo)

#verificador
alta_velocidad=(velocidad_final > 200)

#output
print("                                                    ")
print("####################################################")
print("#    CALCULADORA DE VELOCIDAD FINAL DE UN MOVIL    #")
print("####################################################")
print("# Velocidad inicial    :" , velocidad_inicial)
print("# Aceleracion          :" , aceleracion)
print("# Tiempo               :" , tiempo)
print("#--------------------------------------------------#")
print("# Velocidad final del auto :  ", velocidad_final,"km/h")
print("####################################################")


#condicion simple
#si la velocidad es mayor que 200 mostrar advertencia
if (alta_velocidad == True ):
    print("                VAS COMO UN RAYO!!!              ")
#FIN_IF

import os
#CALCULADORA DEL AREA DE UN TRAPECIO
#input
base_mayor=int(os.sys.argv[1])
base_menor=int(os.sys.argv[2])
altura=int(os.sys.argv[3])

#processing
area=((base_mayor+base_menor)*altura)/2

#verificador
area_pequenia=(area<100)

#output
print("                                            ")
print("############################################")
print("#    CALCULADORA DEL AREA DE UN TRAPECIO   #")
print("############################################")
print("# Base mayor:", base_mayor)
print("# Base menor:", base_menor)
print("# Altura    :", altura)
print("#------------------------------------------#")
print("# El valor del area del trapecio es:", area)
print("############################################")


#condicion simple
#si el area es pequeña mostrar
if (area_pequenia == False):
    print("           ESTA AREA ES SUFICIENTE        ")
#FIN_IF

import os
#CALCULADORA DE INDICE DE MASA CORPORAL
#input
peso=float(os.sys.argv[1])
altura=float(os.sys.argv[2])

#processing
imc=peso/altura**2

#verificador
sobrepeso=(imc >= 25)

#output
print("                                                 ")
print("#################################################")
print("#    CALCULADORA DE INDICE DE MASA CORPORAL     #")
print("#################################################")
print("# El valor del peso es:",peso,"kg")
print("# El valor de la altura es:",altura,"m")
print("#-----------------------------------------------#")
print("# El valor del IMC es:", imc)
print("#################################################")
print("El valor normal oscila entre 18.5 - 24.9")
print("mas que eso es obesidad, menos significa delgadez")
print("#################################################")


#condicion simple
#si la persona tiene sobrepeso mostrar
if (sobrepeso == True):
    print(">> USTED AH DESBLOQUEADO NUESTRA DIETA EXCLUSIVA <<")
#FIN_IF

import os
#CALCULADORA DE AHORRO
#input
dinero_inicial=float(os.sys.argv[1])
dinero_mensual=float(os.sys.argv[2])
meses=float(os.sys.argv[3])

#processing
dinero_final=dinero_inicial+(dinero_mensual*meses)

#verificador
ahorro_alto=(dinero_final > 1000)

#output
print("                                                        ")
print("########################################################")
print("#           CALCULADORA DE AHORRO DE DINERO            #")
print("########################################################")
print("# El valor del dinero inicial es:",dinero_inicial,"s/.")
print("# El valor del dinero ahorrado por mes es:",dinero_mensual,"s/.")
print("# El numero de meses a ahorrar es:", meses)
print("#------------------------------------------------------#")
print("# El dinero total al final del ahorro es de:",dinero_final,"s/.")
print("########################################################")

#condicional simple
#si el  ahorro es alto mostrar el siguiente mensaje
if (ahorro_alto == True):
    print("       Usted ha ganado una tarjeta debito premium     ")
    print("                >>>> FELICIDADES <<<<                 ")
#FIN_IF

import os
#CALCULADORA DE PRESION HIDROSTATICA DE UN CUERPO SUMERGIDO
#input
densidad_liquido=float(os.sys.argv[1])
gravedad=float(os.sys.argv[2])
profundidad=float(os.sys.argv[3])

#processing
presion_hidrostatica=densidad_liquido*gravedad*profundidad

#verificador
presion_alta=(presion_hidrostatica>400)

#output
print("                                                              ")
print("##############################################################")
print("# CALCULADORA DE PRESION HIDROSTATICA DE UN CUERPO SUMERGIDO #")
print("##############################################################")
print("# El valor de la densidad del liquido es:",densidad_liquido)
print("# El valor de la gravedad es:",gravedad)
print("# El valor de la profundidad es:",profundidad)
print("#------------------------------------------------------------#")
print("# La presion hidrostatica a la que esta sometida el")
print("# cuerpo es de:",presion_hidrostatica)
print("##############################################################")


#condicion simple
#si la presion es muy alta mostrar
if (presion_alta == True):
    print("             CUIDADO LA PRESION ES MUY ALTA !!         ")
#FIN_IF

import os
#CALCULADORA DE DILATACION LINEAL
#input
longitud=float(os.sys.argv[1])
coef=float(os.sys.argv[2])
variacion_temp=float(os.sys.argv[3])

#processing
dilatacion_lineal=longitud*coef*variacion_temp
longitud_final=longitud+dilatacion_lineal

#verificador
mucha_dilatacion=(dilatacion_lineal>0.5)

#output
print("                                                            ")
print("############################################################")
print("#            CALCULADORA DE DILATACION LINEAL              #")
print("############################################################")
print("# El valor de la longitud inicial de la varilla es:",longitud,"m")
print("# El valor de la variacion de la temperatura es:",variacion_temp,"C")
print("# El valor del coeficiente de dilatacion es:",coef)
print("#----------------------------------------------------------#")
print("# La dilatacion de la varilla es:",dilatacion_lineal,"m")
print("# La longitud final de la varilla es:",longitud_final,"m")
print("############################################################")

#condicion simple
#si la dilatacion lineal es alta mostrar
if (mucha_dilatacion == True):
    print("              LA DILATACION ES EXCESIVA           ")
#FIN_IF

import os
#CALUCLADORA DEL TRABAJO SOBRE UN OBJETO
#Input
masa=float(os.sys.argv[1])
aceleracion=float(os.sys.argv[2])
distancia=float(os.sys.argv[3])

#Processing
fuerza=(masa*aceleracion)
trabajo=(fuerza*distancia)

#verificador
trabajo_alto=(trabajo > 5000)

#Output
print("                                                            ")
print("############################################################")
print("#    CALCULADORA DEL TRABAJO REALIZADO SOBRE UN OBJETO     #")
print("############################################################")
print("# El valor de la masa es:        ",masa)
print("# El valor de la aceleracion es: ", aceleracion)
print("# El valor de la distancia es:   ", distancia)
print("# El valor de la fuerza ejercida es: ", fuerza)
print("#----------------------------------------------------------#")
print("# El valor del trabajo realizado es: ", trabajo)
print("############################################################")

#condicion simple
#Si el trabajo es alto mostrar
if (trabajo_alto == False):
    print("                 HACE FALTA MAS POTENCIA             ")
#FIN_IF



import os
#CALCULADORA DE LA SUMATORIA DE UNA SUCESION
#input
primer_elemento=int(os.sys.argv[1])
ultimo_elemento=int(os.sys.argv[2])
total_elementos=int(os.sys.argv[3])

#processing
sumatoria=(primer_elemento+ultimo_elemento)*total_elementos/2

#verifcador
sumatoria_baja=(sumatoria < 550)

#output
print("                                                                     ")
print("#####################################################################")
print("#     SUMATORIA DE UNA SUCESION ARITMETICA DE NUMEROS NATURALES     #")
print("#####################################################################")
print("# El valor del primer elemento es:", primer_elemento)
print("# El valor del ultimo elemento es:", ultimo_elemento)
print("# El total de elementos es:",total_elementos)
print("#-------------------------------------------------------------------#")
print("# El valor de la sumatoria de los elementos de la sucesion es:",sumatoria)
print("#####################################################################")

#condicion simple
#si la sumatoria es baja mostrar
if (sumatoria_baja == True):
    print("                         LA SUMATORIA ES BAJA                      ")
#FIN_IF

#CONDICIONALES-DOBLES

import os
#CALCULADORA DE LA VELOCIDAD FINAL DE UN MOVIL
#input
velocidad_inicial = int(os.sys.argv[1])
aceleracion = int(os.sys.argv[2])
tiempo = int(os.sys.argv[3])

#processing
velocidad_final = velocidad_inicial+(aceleracion*tiempo)

#verificador
alta_velocidad=(velocidad_final > 200)

#output
print("                                                    ")
print("####################################################")
print("#    CALCULADORA DE VELOCIDAD FINAL DE UN MOVIL    #")
print("####################################################")
print("# Velocidad inicial    :" , velocidad_inicial)
print("# Aceleracion          :" , aceleracion)
print("# Tiempo               :" , tiempo)
print("#--------------------------------------------------#")
print("# Velocidad final del auto :  ", velocidad_final,"km/h")
print("####################################################")


#condicion doble
#si la velocidad es mayor que 200 mostrar mensaje
if (alta_velocidad == True ):
    print("                VAS COMO UN RAYO!!!              ")
else:
    print("  Tu velocidad es segura  ")
#FIN_IF

import os
#CALCULADORA DEL AREA DE UN TRAPECIO
#input
base_mayor=int(os.sys.argv[1])
base_menor=int(os.sys.argv[2])
altura=int(os.sys.argv[3])

#processing
area=((base_mayor+base_menor)*altura)/2

#verificador
area_pequenia=(area<100)

#output
print("                                            ")
print("############################################")
print("#    CALCULADORA DEL AREA DE UN TRAPECIO   #")
print("############################################")
print("# Base mayor:", base_mayor)
print("# Base menor:", base_menor)
print("# Altura    :", altura)
print("#------------------------------------------#")
print("# El valor del area del trapecio es:", area)
print("############################################")


#condicion doble
#si el area es pequeña mostrar
if (area_pequenia == False):
    print("           ESTA AREA ES SUFICIENTE        ")
else:
    print("  El area es realmente insuficiente  -")
#FIN_IF

import os
#CALCULADORA DE INDICE DE MASA CORPORAL
#input
peso=float(os.sys.argv[1])
altura=float(os.sys.argv[2])

#processing
imc=peso/altura**2

#verificador
sobrepeso=(imc >= 25)

#output
print("                                                 ")
print("#################################################")
print("#    CALCULADORA DE INDICE DE MASA CORPORAL     #")
print("#################################################")
print("# El valor del peso es:",peso,"kg")
print("# El valor de la altura es:",altura,"m")
print("#-----------------------------------------------#")
print("# El valor del IMC es:", imc)
print("#################################################")
print("El valor normal oscila entre 18.5 - 24.9")
print("mas que eso es obesidad, menos significa delgadez")
print("#################################################")


#condicion doble
#si la persona tiene sobrepeso mostrar
if (sobrepeso == True):
    print(">> USTED AH DESBLOQUEADO NUESTRA DIETA EXCLUSIVA <<")
else:
    print(" Usted no tiene sobrepeso ")
#FIN_IF

import os
#CALCULADORA DE AHORRO
#input
dinero_inicial=float(os.sys.argv[1])
dinero_mensual=float(os.sys.argv[2])
meses=float(os.sys.argv[3])

#processing
dinero_final=dinero_inicial+(dinero_mensual*meses)

#verificador
ahorro_alto=(dinero_final > 1000)

#output
print("                                                        ")
print("########################################################")
print("#           CALCULADORA DE AHORRO DE DINERO            #")
print("########################################################")
print("# El valor del dinero inicial es:",dinero_inicial,"s/.")
print("# El valor del dinero ahorrado por mes es:",dinero_mensual,"s/.")
print("# El numero de meses a ahorrar es:", meses)
print("#------------------------------------------------------#")
print("# El dinero total al final del ahorro es de:",dinero_final,"s/.")
print("########################################################")

#condicion doble
#si el  ahorro es alto mostrar el siguiente mensaje
if (ahorro_alto == True):
    print("       Usted ha ganado una tarjeta debito premium     ")
    print("                >>>> FELICIDADES <<<<                 ")
else:
    print("  Buen ahorro, siga así ")
#FIN_IF

import os
#CALCULADORA DEL TIEMPO DE VUELO DE UN PROYECTIL
#input
velocidad_inicial=float(os.sys.argv[1])
gravedad=float(os.sys.argv[2])
import math
y=float(os.sys.argv[3])
x=math.radians(y)

#processing
tiempo_vuelo=(2*velocidad_inicial*math.sin(x))/gravedad

#verificador
vuelo_corto=(tiempo_vuelo<5)

#output
print("                                                         ")
print("#########################################################")
print("#     CALCULADORA DE TIEMPO DE VUELO DE UN PROYECTIL    #")
print("#########################################################")
print("# El valor de la velocidad inicial: ",velocidad_inicial,"m/s")
print("# El valor de la gravedad es: ",gravedad,"m/s^2")
print("# El valor del seno del angulo",y,"es:",math.sin(x))
print("--------------------------------------------------------#")
print("# El tiempo de vuelo del proyectil es:",tiempo_vuelo,"s")
print("#########################################################")


#condicion doble
#si el tiempo de vuelo es corto mostrar
if (vuelo_corto == True):
    print("                 ESTO SERA RAPIDO!             ")
else:
    print(" El tiempo de vuelo no es corto ")
#FIN_IF

import os
#CALCULADORA DE PRESION HIDROSTATICA DE UN CUERPO SUMERGIDO
#input
densidad_liquido=float(os.sys.argv[1])
gravedad=float(os.sys.argv[2])
profundidad=float(os.sys.argv[3])

#processing
presion_hidrostatica=densidad_liquido*gravedad*profundidad

#verificador
presion_alta=(presion_hidrostatica>400)

#output
print("                                                              ")
print("##############################################################")
print("# CALCULADORA DE PRESION HIDROSTATICA DE UN CUERPO SUMERGIDO #")
print("##############################################################")
print("# El valor de la densidad del liquido es:",densidad_liquido)
print("# El valor de la gravedad es:",gravedad)
print("# El valor de la profundidad es:",profundidad)
print("#------------------------------------------------------------#")
print("# La presion hidrostatica a la que esta sometida el")
print("# cuerpo es de:",presion_hidrostatica)
print("##############################################################")


#condicion doble
#si la presion es muy alta mostrar
if (presion_alta == True):
    print("             CUIDADO LA PRESION ES MUY ALTA !!         ")
else:
    print(" La presion no es alta ")
#FIN_IF

import os
#CALCULADORA DE DILATACION LINEAL
#input
longitud=float(os.sys.argv[1])
coef=float(os.sys.argv[2])
variacion_temp=float(os.sys.argv[3])

#processing
dilatacion_lineal=longitud*coef*variacion_temp
longitud_final=longitud+dilatacion_lineal

#verificador
mucha_dilatacion=(dilatacion_lineal>0.5)

#output
print("                                                            ")
print("############################################################")
print("#            CALCULADORA DE DILATACION LINEAL              #")
print("############################################################")
print("# El valor de la longitud inicial de la varilla es:",longitud,"m")
print("# El valor de la variacion de la temperatura es:",variacion_temp,"C")
print("# El valor del coeficiente de dilatacion es:",coef)
print("#----------------------------------------------------------#")
print("# La dilatacion de la varilla es:",dilatacion_lineal,"m")
print("# La longitud final de la varilla es:",longitud_final,"m")
print("############################################################")

#condicion doble
#si la dilatacion lineal es alta mostrar
if (mucha_dilatacion == True):
    print("              LA DILATACION ES EXCESIVA           ")
else:
    print(" La dilatacion es imperceptible ")
#FIN_IF

import os
#CALUCLADORA DEL TRABAJO SOBRE UN OBJETO
#Input
masa=float(os.sys.argv[1])
aceleracion=float(os.sys.argv[2])
distancia=float(os.sys.argv[3])

#Processing
fuerza=(masa*aceleracion)
trabajo=(fuerza*distancia)

#verificador
trabajo_alto=(trabajo > 5000)

#Output
print("                                                            ")
print("############################################################")
print("#    CALCULADORA DEL TRABAJO REALIZADO SOBRE UN OBJETO     #")
print("############################################################")
print("# El valor de la masa es:        ",masa)
print("# El valor de la aceleracion es: ", aceleracion)
print("# El valor de la distancia es:   ", distancia)
print("# El valor de la fuerza ejercida es: ", fuerza)
print("#----------------------------------------------------------#")
print("# El valor del trabajo realizado es: ", trabajo)
print("############################################################")

#condicion doble
#Si el trabajo es alto mostrar
if (trabajo_alto == False):
    print("                 HACE FALTA MAS POTENCIA             ")
else:
    print(" La potencia es suficiente ")
#FIN_IF



import os
#CALCULAR EL VOLUMEN DE UNA PIRAMIDE TRIANGULAR
#input
altura_piramide=float(os.sys.argv[1])
base_triangle=float(os.sys.argv[2])
altura_triangle=float(os.sys.argv[3])

#processing
area_base=((base_triangle*altura_triangle)/2)
volumen=((area_base*altura_piramide)/3)

#verificador
piramide_pequena=(volumen < 78)

#output
print("                                                         ")
print("#########################################################")
print("#        CALCULADORA DE VOLUMEN DE UNA PIRAMIDE         #")
print("#########################################################")
print("# La base de la piramide es un triangulo y su area es:",area_base)
print("# La altura de la piramide es:",altura_piramide)
print("#-------------------------------------------------------#")
print("# El volumen de la piramide es:",volumen,"metros cubicos")
print("#########################################################")

#condicion doble
#si el volumen es mayor del recomendado mostrar
if (piramide_pequena == False):
    print("               ESTO ES LIGERAMENTE GRANDE              ")
else:
    print(" Esto no es grande ")
#FIN_IF


import os
#CALCULADORA DE LA SUMATORIA DE UNA SUCESION
#input
primer_elemento=int(os.sys.argv[1])
ultimo_elemento=int(os.sys.argv[2])
total_elementos=int(os.sys.argv[3])

#processing
sumatoria=(primer_elemento+ultimo_elemento)*total_elementos/2

#verifcador
sumatoria_baja=(sumatoria < 550)

#output
print("                                                                     ")
print("#####################################################################")
print("#     SUMATORIA DE UNA SUCESION ARITMETICA DE NUMEROS NATURALES     #")
print("#####################################################################")
print("# El valor del primer elemento es:", primer_elemento)
print("# El valor del ultimo elemento es:", ultimo_elemento)
print("# El total de elementos es:",total_elementos)
print("#-------------------------------------------------------------------#")
print("# El valor de la sumatoria de los elementos de la sucesion es:",sumatoria)
print("#####################################################################")

#condicion doble
#si la sumatoria es baja mostrar
if (sumatoria_baja == True):
    print("                         LA SUMATORIA ES BAJA                      ")
else:
    print(" La sumatoria tiene un valor alto ")
#FIN_IF

#CONDICIONALES-MULTIPLES

import os
#CALCULADORA DE LA VELOCIDAD FINAL DE UN MOVIL
#input
velocidad_inicial = int(os.sys.argv[1])
aceleracion = int(os.sys.argv[2])
tiempo = int(os.sys.argv[3])

#processing
velocidad_final = velocidad_inicial+(aceleracion*tiempo)

#verificador
alta_velocidad=(velocidad_final > 200)

#output
print("                                                    ")
print("####################################################")
print("#    CALCULADORA DE VELOCIDAD FINAL DE UN MOVIL    #")
print("####################################################")
print("# Velocidad inicial    :" , velocidad_inicial)
print("# Aceleracion          :" , aceleracion)
print("# Tiempo               :" , tiempo)
print("#--------------------------------------------------#")
print("# Velocidad final del auto :  ", velocidad_final,"km/h")
print("####################################################")


#condicion multiple
#si la velocidad es mayor que 200 mostrar advertencia
if (velocidad_final > 200):
    print("                VAS COMO UN RAYO!!!              ")
if (100<velocidad_final<200):
    print(" Buena velocidad ")
if (0<velocidad_final<100):
    print(" La velocidad es muy baja ")
else:
    print(" valores erroneos ")
#FIN_IF

import os
#CALCULADORA DEL AREA DE UN TRAPECIO
#input
base_mayor=int(os.sys.argv[1])
base_menor=int(os.sys.argv[2])
altura=int(os.sys.argv[3])

#processing
area=((base_mayor+base_menor)*altura)/2

#verificador
area_pequenia=(area<100)

#output
print("                                            ")
print("############################################")
print("#    CALCULADORA DEL AREA DE UN TRAPECIO   #")
print("############################################")
print("# Base mayor:", base_mayor)
print("# Base menor:", base_menor)
print("# Altura    :", altura)
print("#------------------------------------------#")
print("# El valor del area del trapecio es:", area)
print("############################################")


#condicion multiple
#si el area es pequeña mostrar
if (area > 100):
    print("           ESTA AREA ES SUFICIENTE        ")
if (area < 100 and area>50):
    print(" Esta area es algo pequeña ")
if (area > 500):
    print(" Esta area es muy grande ")
#FIN_IF

import os
#CALCULADORA DE INDICE DE MASA CORPORAL
#input
peso=float(os.sys.argv[1])
altura=float(os.sys.argv[2])

#processing
imc=peso/altura**2

#verificador
sobrepeso=(imc >= 25)

#output
print("                                                 ")
print("#################################################")
print("#    CALCULADORA DE INDICE DE MASA CORPORAL     #")
print("#################################################")
print("# El valor del peso es:",peso,"kg")
print("# El valor de la altura es:",altura,"m")
print("#-----------------------------------------------#")
print("# El valor del IMC es:", imc)
print("#################################################")
print("El valor normal oscila entre 18.5 - 24.9")
print("mas que eso es obesidad, menos significa delgadez")
print("#################################################")


#condicion multiple
#si la persona tiene sobrepeso mostrar
if (sobrepeso == True):
    print(">> USTED AH DESBLOQUEADO NUESTRA DIETA EXCLUSIVA <<")
if (19<peso<25):
    print(" Usted esta en el peso correcto ")
if (0<peso<19):
    print(" Usted tiene delgadez, visite un medico ")
#FIN_IF


import os
#CALCULADORA DE AHORRO
#input
dinero_inicial=float(os.sys.argv[1])
dinero_mensual=float(os.sys.argv[2])
meses=float(os.sys.argv[3])

#processing
dinero_final=dinero_inicial+(dinero_mensual*meses)

#verificador
ahorro_alto=(dinero_final > 1000)

#output
print("                                                        ")
print("########################################################")
print("#           CALCULADORA DE AHORRO DE DINERO            #")
print("########################################################")
print("# El valor del dinero inicial es:",dinero_inicial,"s/.")
print("# El valor del dinero ahorrado por mes es:",dinero_mensual,"s/.")
print("# El numero de meses a ahorrar es:", meses)
print("#------------------------------------------------------#")
print("# El dinero total al final del ahorro es de:",dinero_final,"s/.")
print("########################################################")

#condicional multiple
#si el  ahorro es alto mostrar el siguiente mensaje
if (ahorro_alto == True):
    print("       Usted ha ganado una tarjeta debito premium     ")
    print("                >>>> FELICIDADES <<<<                 ")
if (100<dinero_final<1000):
    print(" El ahorro es muy bueno ")
if (10<dinero_final<100):
    print(" Este ahorro es muy pobre :( ")
#FIN_IF

import os
#CALCULADORA DEL TIEMPO DE VUELO DE UN PROYECTIL
#input
velocidad_inicial=float(os.sys.argv[1])
gravedad=float(os.sys.argv[2])
import math
y=float(os.sys.argv[3])
x=math.radians(y)

#processing
tiempo_vuelo=(2*velocidad_inicial*math.sin(x))/gravedad

#verificador
vuelo_corto=(tiempo_vuelo<5)

#output
print("                                                         ")
print("#########################################################")
print("#     CALCULADORA DE TIEMPO DE VUELO DE UN PROYECTIL    #")
print("#########################################################")
print("# El valor de la velocidad inicial: ",velocidad_inicial,"m/s")
print("# El valor de la gravedad es: ",gravedad,"m/s^2")
print("# El valor del seno del angulo",y,"es:",math.sin(x))
print("--------------------------------------------------------#")
print("# El tiempo de vuelo del proyectil es:",tiempo_vuelo,"s")
print("#########################################################")


#condicion multiple
#si el tiempo de vuelo es corto mostrar
if (vuelo_corto == True):
    print("                 ESTO SERA RAPIDO!             ")
if (tiempo_vuelo>5 and tiempo_vuelo<30):
    print(" El vuelo sera adecuado ")
if (tiempo_vuelo>50):
    print(" El vuelo sera muy largo ")
#FIN_IF

import os
#CALCULADORA DE PRESION HIDROSTATICA DE UN CUERPO SUMERGIDO
#input
densidad_liquido=float(os.sys.argv[1])
gravedad=float(os.sys.argv[2])
profundidad=float(os.sys.argv[3])

#processing
presion_hidrostatica=densidad_liquido*gravedad*profundidad

#verificador
presion_alta=(presion_hidrostatica>400)

#output
print("                                                              ")
print("##############################################################")
print("# CALCULADORA DE PRESION HIDROSTATICA DE UN CUERPO SUMERGIDO #")
print("##############################################################")
print("# El valor de la densidad del liquido es:",densidad_liquido)
print("# El valor de la gravedad es:",gravedad)
print("# El valor de la profundidad es:",profundidad)
print("#------------------------------------------------------------#")
print("# La presion hidrostatica a la que esta sometida el")
print("# cuerpo es de:",presion_hidrostatica)
print("##############################################################")


#condicion multiple
#si la presion es muy alta mostrar
if (presion_alta == True):
    print("             CUIDADO LA PRESION ES MUY ALTA !!         ")
if (100<presion_hidrostatica<400):
    print(" La presion es normal ")
if (presion_hidrostatica<100):
    print(" Cuidado la presion es muy baja ")
#FIN_IF

import os
#CALCULADORA DE DILATACION LINEAL
#input
longitud=float(os.sys.argv[1])
coef=float(os.sys.argv[2])
variacion_temp=float(os.sys.argv[3])

#processing
dilatacion_lineal=longitud*coef*variacion_temp
longitud_final=longitud+dilatacion_lineal

#verificador
mucha_dilatacion=(dilatacion_lineal>0.5)

#output
print("                                                            ")
print("############################################################")
print("#            CALCULADORA DE DILATACION LINEAL              #")
print("############################################################")
print("# El valor de la longitud inicial de la varilla es:",longitud,"m")
print("# El valor de la variacion de la temperatura es:",variacion_temp,"C")
print("# El valor del coeficiente de dilatacion es:",coef)
print("#----------------------------------------------------------#")
print("# La dilatacion de la varilla es:",dilatacion_lineal,"m")
print("# La longitud final de la varilla es:",longitud_final,"m")
print("############################################################")

#condicion multiple
#si la dilatacion lineal es alta mostrar
if (mucha_dilatacion == True):
    print("              LA DILATACION ES EXCESIVA           ")
if (0<dilatacion_lineal<0.5):
    print(" La dilatacion es imperceptible ")
if (dilatacion_lineal<0):
    print(" valores erroneos ")
#FIN_IF

import os
#CALUCLADORA DEL TRABAJO SOBRE UN OBJETO
#Input
masa=float(os.sys.argv[1])
aceleracion=float(os.sys.argv[2])
distancia=float(os.sys.argv[3])

#Processing
fuerza=(masa*aceleracion)
trabajo=(fuerza*distancia)

#verificador
trabajo_alto=(trabajo > 5000)

#Output
print("                                                            ")
print("############################################################")
print("#    CALCULADORA DEL TRABAJO REALIZADO SOBRE UN OBJETO     #")
print("############################################################")
print("# El valor de la masa es:        ",masa)
print("# El valor de la aceleracion es: ", aceleracion)
print("# El valor de la distancia es:   ", distancia)
print("# El valor de la fuerza ejercida es: ", fuerza)
print("#----------------------------------------------------------#")
print("# El valor del trabajo realizado es: ", trabajo)
print("############################################################")

#condicion multiple
#Si el trabajo es alto mostrar
if (trabajo_alto == False):
    print("                 HACE FALTA MAS POTENCIA             ")
if (1000<trabajo<5000):
    print(" El trabajo es normal ")
if (trabajo_alto == True):
    print(" El valor del trabajo es alto ")
#FIN_IF

import os
#CALCULAR EL VOLUMEN DE UNA PIRAMIDE TRIANGULAR
#input
altura_piramide=float(os.sys.argv[1])
base_triangle=float(os.sys.argv[2])
altura_triangle=float(os.sys.argv[3])

#processing
area_base=((base_triangle*altura_triangle)/2)
volumen=((area_base*altura_piramide)/3)

#verificador
piramide_pequena=(volumen < 78)

#output
print("                                                         ")
print("#########################################################")
print("#        CALCULADORA DE VOLUMEN DE UNA PIRAMIDE         #")
print("#########################################################")
print("# La base de la piramide es un triangulo y su area es:",area_base)
print("# La altura de la piramide es:",altura_piramide)
print("#-------------------------------------------------------#")
print("# El volumen de la piramide es:",volumen,"metros cubicos")
print("#########################################################")

#condicion multiple
#si el volumen es mayor del recomendado mostrar
if (piramide_pequena == False):
    print("               ESTO ES LIGERAMENTE GRANDE              ")
if (piramide_pequena == True):
    print(" La pitamide es pequeña ")
if (volumen > 1000):
    print(" la piramide es gigante ")
#FIN_IF

import os
#CALCULADORA DE LA SUMATORIA DE UNA SUCESION
#input
primer_elemento=int(os.sys.argv[1])
ultimo_elemento=int(os.sys.argv[2])
total_elementos=int(os.sys.argv[3])

#processing
sumatoria=(primer_elemento+ultimo_elemento)*total_elementos/2

#verifcador
sumatoria_baja=(sumatoria < 550)

#output
print("                                                                     ")
print("#####################################################################")
print("#     SUMATORIA DE UNA SUCESION ARITMETICA DE NUMEROS NATURALES     #")
print("#####################################################################")
print("# El valor del primer elemento es:", primer_elemento)
print("# El valor del ultimo elemento es:", ultimo_elemento)
print("# El total de elementos es:",total_elementos)
print("#-------------------------------------------------------------------#")
print("# El valor de la sumatoria de los elementos de la sucesion es:",sumatoria)
print("#####################################################################")

#condicion multiple
#si la sumatoria es baja mostrar
if (sumatoria_baja == True):
    print("                         LA SUMATORIA ES BAJA                      ")
if (sumatoria > 1000):
    print(" El valor de la sumatoria es alto ")
if (sumatoria == 0):
    print(" No existe sumatoria ")
#FIN_IF
