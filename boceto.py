import timeit
import copy


class Pintador():
    def __init__(self):
        self.ulti_rojo = None
        self.max_azul = None

    def semi_copiador(self,otro):
        res = Pintador()
        res.max_azul = otro.max_azul
        res.ulti_rojo = otro.ulti_rojo
        return res
    def puedo_pintar_rojo(self,numero):
        return (self.ulti_rojo == None) or (self.ulti_rojo < numero)
    
    def puedo_pintar_azul(self,numero):
        return (self.max_azul == None) or (self.max_azul > numero)
    
    def pintar_azul(self,numero):
        copia1 = self.semi_copiador(self)
        copia1.max_azul = numero
        return copia1
    def pintar_rojo(self,numero):
        copia1 = self.semi_copiador(self)
        copia1.ulti_rojo = numero
        return copia1

    def __str__(self):
        return '(' + str(self.ulti_rojo) + ',' + str(self.max_azul) + ')'
    
    def __repr__(self):
        return '(' + str(self.ulti_rojo) + ',' + str(self.max_azul) + ')'
    def __eq__(self,otro):
        return self.max_azul == otro.max_azul and self.ulti_rojo == otro.ulti_rojo

def levanta_archivo(nombre):
    archivo = open(nombre, "r") 
    contenido = archivo.read()
    contenido = contenido.split()
    res = []
    muestra = []
    def insertar(muestra,contenido,cantidad_elementos,indice):
        i = 0
        while(i < cantidad_elementos):
            muestra.append(int(contenido[indice+1]))
            indice += 1
            i+=1
        return muestra
    i = 0
    while(i < len(contenido)):
        insertar(muestra,contenido,int(contenido[int(i)]),i)
        res.append(muestra)
        muestra=[]
        i += (int(contenido[i])+1) 
    return res


def potencial(arreglo,indice):
    numero = arreglo[indice]
    mayores = 0
    menores = 0
    while indice < len(arreglo):
        if numero < arreglo[indice]:
            menores += 1
        else:
            if numero > arreglo[indice]:
                mayores += 1
        indice+=1
    return max(mayores,menores)


def esta_el_rojo(lista,rojo):
    for elem in lista:
        if elem.ulti_rojo == rojo:
            return True
    return False

def dame_el_rojo(lista,rojo):
    for elem in lista:
        if elem.ulti_rojo == rojo:
            return elem


#arreglos = [[1,2,3]]
#arreglos = [[3, 11, 0, 1, 3, 5, 2, 4, 1, 0, 9, 3]]
arreglos = levanta_archivo("muestra_tamanio1000")
#print(len(arreglos))
tiempo = timeit.default_timer()
numero_elemento = 0
for arreglo in arreglos:




    
    i = 0
    res = []
    while(i < len(arreglo)+1):
        res.append([])
        i+=1
    res[0].append(Pintador())
    max_pintados = 0
    i=0
    while i < len(arreglo):
        k = i+1
        while k >= 0:
            for elem in res[k]:
                if(elem.ulti_rojo == None or elem.ulti_rojo < arreglo[i]):
                    nuevo_pintador = Pintador()
                    nuevo_pintador.ulti_rojo = arreglo[i]
                    nuevo_pintador.max_azul = elem.max_azul
                    if not esta_el_rojo(res[k+1],nuevo_pintador.ulti_rojo):
                        res[k+1].append(nuevo_pintador)
                    else:
                        rojo = dame_el_rojo(res[k+1],nuevo_pintador.ulti_rojo)
                        if (rojo.max_azul != None) and (nuevo_pintador.max_azul == None or rojo.max_azul < nuevo_pintador.max_azul):
                            rojo.max_azul = nuevo_pintador.max_azul
                if(elem.max_azul == None or elem.max_azul > arreglo[i]):
                    nuevo_pintador = Pintador()
                    nuevo_pintador.ulti_rojo = elem.ulti_rojo
                    nuevo_pintador.max_azul = arreglo[i]
                    if not  esta_el_rojo(res[k+1],elem.ulti_rojo):
                         res[k+1].append(nuevo_pintador)
                    else:
                        rojo = dame_el_rojo(res[k+1],nuevo_pintador.ulti_rojo)
                        if (rojo.max_azul != None) and (nuevo_pintador.max_azul == None or rojo.max_azul < nuevo_pintador.max_azul):
                            rojo.max_azul = nuevo_pintador.max_azul
            k-=1
        i+=1
        print(i)








    
    ultimo = len(res)-1
    while(ultimo >= 0 ):
        if len(res[ultimo]) != 0 :
            print(len(arreglo) -ultimo)
            break
        ultimo -= 1
    
    
    
    print(timeit.default_timer() - tiempo)
    cantidad = 0
    for elem in res:
        cantidad += len(elem)
    print(cantidad)

   
            
