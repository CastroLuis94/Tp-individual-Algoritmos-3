import timeit


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
    def puedo_pintar_rojo(self,numero):
        return (self.ulti_rojo == None) or (self.ulti_rojo < numero)
    
    def puedo_pintar_azul(self,numero):
        return (self.ulti_azul == None) or (self.ulti_azul > numero)
    
    def pintar_azul(self,numero):
        copia1 = self.semi_copiador(self)
        copia1.ulti_azul = numero
        copia1.pintados += 1
        return copia1
    def pintar_rojo(self,numero):
        copia1 = self.semi_copiador(self)
        copia1.ulti_rojo = numero
        copia1.pintados += 1
        return copia1

    def __str__(self):
        return '(' + str(self.ulti_rojo) + ',' + str(self.ulti_azul) + ',' + str(self.pintados) + ')'
    
    def __repr__(self):
        return '(' + str(self.ulti_rojo) + ',' + str(self.ulti_azul) + ',' + str(self.pintados) + ')'
    def __eq__(self,otro):
        return self.ulti_azul == otro.ulti_azul and self.ulti_rojo == otro.ulti_rojo and self.pintados == otro.pintados


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
#arreglo = [3, 11, 0, 1, 3, 5, 2, 4, 1, 0, 9]
#arreglo = [0,7,1,2,2,1,5,0]
arreglo = [1]
while(len(arreglo)< 20):
    i = 0
    res = []
    while(i < len(arreglo)+1):
        res.append([])
        i+=1
    res[0] = [Pintador()]
    tiempo = timeit.default_timer()
    maxima_cant_pintados = 0
    posicion = 0
    while posicion < len(arreglo):
        i = min(maxima_cant_pintados,len(arreglo)-potencial(arreglo,posicion))
        while(i >= 0 ):
            k = 0
            pintados = []
            tamanio = len(res[i])
            while(k < tamanio):
                if(res[i][k].puedo_pintar_rojo(arreglo[posicion])):
                    pintados.append( (res[i][k]).pintar_rojo(arreglo[posicion]) )
                if(res[i][k].puedo_pintar_azul(arreglo[posicion])):
                    pintados.append( (res[i][k]).pintar_azul(arreglo[posicion]) )
                k += 1
            p = 0
            while(p < len(pintados)):
                x = 0
                while x < len(res[i+1]):
                    if res[i+1][x] == pintados[p]:
                        break
                    x+=1
                if(x==len(res[i+1])):
                    res[i+1].append(pintados[p])
                p+=1
            i-=1
        posicion += 1
        if(len(res[i+1]) > 0 ):
            maxima_cant_pintados += 1
            i = maxima_cant_pintados
    #print(res)
    """
    if(len(pintados) > 0 or i == maxima_cant_pintados):
                break
    """

    ultimo = len(res) -1
    while(ultimo >= 0):  
        if(len(res[ultimo]) != 0):
            print ((res[ultimo][0]))
            break
        ultimo -=1


    print(timeit.default_timer() - tiempo)


    cantidad = 0
    for elem in res:
        cantidad += len(elem)
    print(cantidad)
    arreglo.append(len(arreglo)+1)




   
            
