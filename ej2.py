import timeit
import random
'''
print('Ingrese el largo del arreglo.')
basura = input()

print('Ingrese los numeros del arreglo.')
entrada = input()

def transformar_input(entrada):
    res = []
    for num in entrada.split():
        res.append(int(num))
    return res

entrada = transformar_input(entrada)
'''
class Pintador():
    def __init__(self):
        self.indice = 0
        self.ulti_rojo = None
        self.ulti_azul = None
        self.pintados = 0
        
    def semi_copiador(self,otro):
        res = Pintador()
        res.indice = otro.indice
        res.ulti_azul = otro.ulti_azul
        res.ulti_rojo = otro.ulti_rojo
        res.pintados = otro.pintados
        return res

    def pintar(self,a_pintar):
        if len(a_pintar) == self.indice:
            return self.pintados
        else:
            copia1 = self.semi_copiador(self)
            copia2 = self.semi_copiador(self)
            copia3 = self.semi_copiador(self)
            return max(copia1.pintar_rojo(a_pintar), copia2.pintar_azul(a_pintar), copia3.no_pintar(a_pintar))
    
    def pintar_rojo(self,a_pintar):
        if (self.ulti_rojo) == None or a_pintar[self.indice] > self.ulti_rojo:
            self.ulti_rojo = a_pintar[self.indice]
            self.indice += 1
            self.pintados += 1
            return self.pintar(a_pintar)
        else:
            hay_mas_rojos = False
            hay_mas_rojos , self.indice = buscar_siguiente_rojo(a_pintar,self.ulti_rojo,self.indice) 
            if hay_mas_rojos:
                return self.pintar_rojo(a_pintar)
            else:
                return self.pintados
                

    def pintar_azul(self,a_pintar):
        if self.ulti_azul is None or a_pintar[self.indice] < self.ulti_azul:
            self.ulti_azul = a_pintar[self.indice]
            self.indice += 1
            self.pintados += 1
            return self.pintar(a_pintar)
        else:
            hay_mas_azules = False
            hay_mas_azules , self.indice = buscar_siguiente_azul(a_pintar,self.ulti_azul,self.indice) 
            if hay_mas_azules:
                return self.pintar_azul(a_pintar)
            else:
                return self.pintados
        
    def no_pintar(self,a_pintar):
        self.indice += 1
        return self.pintar(a_pintar)


def buscar_siguiente_rojo(a_pintar,ultimo_rojo,indice):
    while indice < len(a_pintar):
        if a_pintar[indice] > ultimo_rojo :
            return (True,indice)
        indice += 1
    return (False,indice)

def buscar_siguiente_azul(a_pintar,ultimo_azul,indice):
    while indice < len(a_pintar):
        if a_pintar[indice] < ultimo_azul :
            return (True,indice)
        indice += 1
    return (False,indice)
'''
objeto = Pintador()
print(len(entrada) - objeto.pintar(entrada))
'''