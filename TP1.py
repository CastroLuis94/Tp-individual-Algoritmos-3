import timeit
import random
import copy

#print('Ingrese los numeros del arreglo.')
#entrada = input()

def transformar_input(entrada):
    res = []
    for num in entrada.split():
        res.append(int(num))
    return res

#entrada = transformar_input(entrada)

class Pintar():
    def __init__(self):
        self.indice = 0
        self.ulti_rojo = None
        self.ulti_azul = None
        self.pintados = 0
        
    def semi_copiador(self):
        res = Pintar()
        res.indice = copy.deepcopy(self.indice)
        res.ulti_azul = copy.deepcopy(self.ulti_azul)
        res.ulti_rojo = copy.deepcopy(self.ulti_rojo)
        res.pintados = copy.deepcopy(self.pintados)
        return res

    def pintar(self,a_pintar):
        if len(a_pintar) == 0:
            return self.pintados
        else:
            copia1 = self.semi_copiador()
            copia2 = self.semi_copiador()
            copia3 = self.semi_copiador()
            return max(copia1.pintar_rojo(a_pintar), copia2.pintar_azul(a_pintar), copia3.no_pintar(a_pintar))
    
    def pintar_rojo(self,a_pintar):
        if len(a_pintar) <= self.indice:
            return self.pintados
        else:
            if (self.ulti_rojo) == None or a_pintar[self.indice] > self.ulti_rojo:
                self.ulti_rojo = a_pintar[self.indice]
                self.indice += 1
                self.pintados += 1
                return self.pintar(a_pintar)
            else:
                self.indice += 1
                return self.pintar(a_pintar)

    def pintar_azul(self,a_pintar):
        if len(a_pintar) <= self.indice:
            return self.pintados
        else:
            if self.ulti_azul is None or a_pintar[self.indice] < self.ulti_azul:
                self.ulti_azul = a_pintar[self.indice]
                self.indice += 1
                self.pintados += 1
                return self.pintar(a_pintar)
            else:
                self.indice += 1
                return self.pintar(a_pintar)
        
    def no_pintar(self,a_pintar):
        if len(a_pintar) <= self.indice:
            return self.pintados
        else:
            self.indice += 1
            return self.pintar(a_pintar)

def generador_entradas_random(cantidad_de_muestras,longitud_de_muestra):
    muestra = []
    res = []
    for muestra_numero in range(0,cantidad_de_muestras):
        for elem in range(0,longitud_de_muestra):
            muestra.append(random.randint(1,100))
        res.append(muestra)
        muestra = []
    return res


start_time = timeit.default_timer()

print(timeit.default_timer() - start_time)

tamanio_muetras = range(0,11)
tiempos = [] 
numero_de_muestras = 100
for tamanio_muestra in tamanio_muetras:   
    muestras = (generador_entradas_random(numero_de_muestras,tamanio_muestra))
    start_time = timeit.default_timer()
    for muestra in muestras:
        pintador = Pintar()
        pintador.pintar(muestra)
    tiempo = (tamanio_muestra,(timeit.default_timer() - start_time)/float(numero_de_muestras))
    tiempos.append(tiempo)
    print (tiempo)
