import timeit
import copy



print("Ingrese el tamaño del arreglo.")
basura = input()
print('Ingrese los numeros del arreglo.')
entrada = input()

def transformar_input(entrada):
    res = []
    for num in entrada.split():
        res.append(int(num))
    return res

entrada = transformar_input(entrada)


def crear_lista(tamanio):
    res = list()
    for elem in range(tamanio):
        res.append(0)
    return res

def crear_matriz(tamanio):
    matriz = crear_lista(tamanio+1)
    i = 0
    while(i < tamanio+1):
        matriz[i] = crear_lista(tamanio+1)
        i += 1
    return matriz

def max_posibles_pintados_azules_desde(vector_entrada, matriz, j,fila):
	res = matriz[fila][0]
	for k in range(len(matriz)):
		if(vector_entrada[j-1] < vector_entrada[k-1] and matriz[fila][k] > res):
			res = matriz[fila][k]
	return res


def max_posibles_pintados_rojos_desde(vector_entrada, matriz, j, columna):
	res = matriz[0][columna]		
	for k in range(len(matriz)):		
		if(vector_entrada[j-1] > vector_entrada[k-1] and matriz[k][columna] > res):
			res = matriz[k][columna]
	return res


def ej3(vector_entrada,matriz):
	maximo = 0
	posible_maximo1 = 0
	posible_maximo2 = 0
	tamanio = range(len(matriz))
	for fila in tamanio:
		for column in tamanio:
			if(fila < column):
				posible_maximo2 = max_posibles_pintados_azules_desde(vector_entrada, matriz, column, fila)
				matriz[fila][column] = posible_maximo2 + 1
				maximo = max(maximo,posible_maximo2)
			if(fila > column):
				posible_maximo1 = max_posibles_pintados_rojos_desde(vector_entrada, matriz, fila, column)
				matriz[fila][column] = posible_maximo1 + 1
				maximo = max(maximo,posible_maximo1)
			if(fila == column):
				matriz[fila][column] = 0
	return maximo
		
	

def dinamico(vector_entrada):
	matriz = crear_matriz(len(vector_entrada))
	max_cant_pintados = ej3(vector_entrada,matriz)		
	return (len(vector_entrada) - max_cant_pintados - 1)


start = timeit.default_timer()
print(dinamico(entrada) )
print(timeit.default_timer() - start)
