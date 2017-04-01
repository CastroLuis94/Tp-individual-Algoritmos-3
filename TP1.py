import copy
import timeit
import random




#print ('Ingrese los numeros del arreglo.')
#entrada = input()
#O(N)
def transformar_input(entrada):
    res = []
    for num in entrada.split():
        res.append(int(num))
    return res

#entrada = transformar_input(entrada)
#O(N)
def filtrar_mayores(vector,posicion):
    vector = vector[posicion:]
    res = [vector[0]]
    res += filter(lambda x: x > res[0],vector)
    return res

#O(N)
def filtrar_menores(vector,posicion):
    vector = vector[posicion:]
    res = [vector[0]]
    res += filter(lambda x: x < res[0],vector)
    return res
#O(N)
def creciente(vector):
    for i in range(0,len(vector)-1):
        if(vector[i] >= vector[i+1]): 
            return False
    return True 
#O(N)
def decreciente(vector):
    return creciente(vector[::-1])
#O(2**N)
def potencia(c):
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]
#O(N**2)
def sin_repetidos(lista):
    res = []
    for elem in lista:
        if elem not in res:
            res.append(elem)
    return res

#0(N*(2**N))
def rojos(vector):
    lista_de_rojos = []
    for num in vector:
        solo_los_mayores = filtrar_mayores(vector,vector.index(num))
        lista_de_rojos += filter(lambda x:creciente(x), potencia(solo_los_mayores))
    return sin_repetidos(lista_de_rojos)


#0(N(2**N)) Nota:Es un menor N que la entrada original porque voy a filtrar los numeros que ya use
def azules(vector):
    lista_de_azules = []
    for num in vector:
        solo_los_menores = filtrar_menores(vector,vector.index(num))
        lista_de_azules += filter(lambda x:decreciente(x), potencia(solo_los_menores))
    return sin_repetidos(lista_de_azules)
#O(N**2)
def simplificar(vector,rojos):
    res = copy.deepcopy(vector)
    for elem in rojos:
        res.remove(elem)
    return res    
#O(N)
def mas_largo(listas):
    res=[]
    max_len=0
    for lista in listas:
        if len(lista)>max_len:
            max_len = len(lista)
            res=lista
    return res 

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

def generador_entradas_random(cantidad_de_muestras,longitud_de_muestra):
    muestra = []
    res = []
    for muestra_numero in range(0,cantidad_de_muestras):
        for elem in range(0,longitud_de_muestra):
            muestra.append(random.randint(1,100))
        res.append(muestra)
        muestra = []
    return res




tamanio_muetras = [5,10,15,20,25]
tiempos = [] 
numero_de_muestras = 1
for tamanio_muestra in tamanio_muetras:   
    muestras =  (generador_entradas_random(numero_de_muestras,tamanio_muestra))
    start_time = timeit.default_timer()
    for muestra in muestras:
        elige_resultado(ejercicio(muestra))
    tiempos.append((timeit.default_timer() - start_time)/float(numero_de_muestras))
    print (tiempos)


