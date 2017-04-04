import random
#O(N)
def transformar_input(entrada):
    res = []
    for num in entrada.split():
        res.append(int(num))
    return res

#O(N)
def filtrar_mayores(vector, posicion):
    vector = vector[posicion:]
    res = [vector[0]]
    res += filter(lambda x: x > res[0], vector)
    return res

#O(N)
def filtrar_menores(vector, posicion):
    vector = vector[posicion:]
    res = [vector[0]]
    res += filter(lambda x: x < res[0], vector)
    return res
#O(N)
def creciente(vector, posiciones):
    i = 0
    posiciones = list(posiciones)
    posiciones.sort()
    while i < len(posiciones) - 1:
        if vector[posiciones[i]] >= vector[posiciones[i+1]]:
            return False
        i+=1
    return True

#O(N)
def decreciente(vector, posiciones):
    i = 0
    posiciones = list(posiciones)
    posiciones.sort()
    while i < len(posiciones) - 1:
        if vector[posiciones[i]] <= vector[posiciones[i+1]]:
            return False
        i+=1
    return True

#0(N*(2**N))
def rojos(vector):
    lista_de_posiciones_rojos = [posicion for posicion in posicion_conj_partes(vector) if creciente(vector,posicion) ] 
    return(lista_de_posiciones_rojos)


def azules(vector):
    """
    0(N(2**N)) Nota:Es un menor N que la entrada original
    porque voy a filtrar los numeros que ya use
    """
    lista_de_posiciones_azules = [posicion for posicion in posicion_conj_partes(vector) if decreciente(vector,posicion) ] 
    return(lista_de_posiciones_azules)

def generador_entradas_random(cantidad_de_muestras,longitud_de_muestra):
    muestra = []
    res = []
    for muestra_numero in range(0,cantidad_de_muestras):
        for elem in range(0,longitud_de_muestra):
            muestra.append(random.randint(1,100))
        res.append(muestra)
        muestra = []
    return res



"""
tamanio_muetras = [5,10,15,20,25]
tiempos = [] 
numero_de_muestras = 1
for tamanio_muestra in tamanio_muetras:   
    muestras = (generador_entradas_random(numero_de_muestras,tamanio_muestra))
    start_time = timeit.default_timer()
    for muestra in muestras:
        elige_resultado(ejercicio(muestra))
    tiempos.append((timeit.default_timer() - start_time)/float(numero_de_muestras))
    print (tiempos)
"""


def posicion_conj_partes(s):
    x = len(s)
    res = []
    for i in range(1 << x):
        res += [set([j for j in range(x) if (i & (1 << j))] )]
    return res

#O(N**2)
def sin_repetidos(lista):
    res = []
    for elem in lista:
        if elem not in res:
            res.append(elem)
    return res



def simplificar(vector, posiciones_de_rojos):
    """
    O(N**2)
    """
    res = vector[:]
    posiciones_de_rojos = posiciones_de_rojos[::-1]
    for elem in posiciones_de_rojos:
        res.pop(elem)
    return res

def mas_largo(listas):
    """
    O(N)
    """
    res = []
    max_len = 0
    for lista in listas:
        if len(lista)>max_len:
            max_len = len(lista)
            res=lista
    return res 

def buscar_mas_largo(tuplas):
    res = tuplas[0]
    for tupla in tuplas:
        if(res[2] < tupla[2]):
            res = tupla
    return res
