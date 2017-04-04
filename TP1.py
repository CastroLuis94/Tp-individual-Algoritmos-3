import timeit
import random
from auxiliares import *


#print ('Ingrese los numeros del arreglo.')
#entrada = input()


#entrada = transformar_input(entrada)


#O(N)
def elige_resultado(posibles_res):
    suma_maxima = 0
    res = []
    for elem in posibles_res:
        if(suma_maxima < len(elem[0])+len(elem[1]) ):
            suma_maxima = len(elem[0])+len(elem[1])
            res = elem[0]+elem[1]
    return (res,suma_maxima)


def ejercicio(entrada): 
    lista_de_rojos = rojos(entrada)
    #O(N*(2**N))
    res = []
    cantidad_de_rojos = len(lista_de_rojos)
    #O(1) 
    for indice in range(0,cantidad_de_rojos): #O(N*(2**N))
        res.append((lista_de_rojos[indice],mas_largo(azules(simplificar(entrada,lista_de_rojos[indice])))))
        
    return (res)

def ejercicio_uno(entrada):
    conj_rojos = rojos(entrada)
    conj_azules = azules(entrada)
    res = []
    for rojo in conj_rojos:
        for azul in conj_azules:
            if rojo & azul == set() :
                res.append((rojo,azul,len(rojo)+len(azul)))
    return len(entrada) - (buscar_mas_largo(res)[2])



tamanio_muetras = range(0,26)
tiempos = [] 
numero_de_muestras = 1
for tamanio_muestra in tamanio_muetras:   
    muestras = (generador_entradas_random(numero_de_muestras,tamanio_muestra))
    start_time = timeit.default_timer()
    for muestra in muestras:
       ejercicio_uno(muestra)
    tiempo = (tamanio_muestra,(timeit.default_timer() - start_time)/float(numero_de_muestras))
    tiempos.append(tiempo)
    print (tiempo)


