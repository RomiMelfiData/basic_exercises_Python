#indice empieza en 0
#posicion empieza en 1

def primo(numero):  
    #Devuelve True si es primo o False si no lo es              
    es_primo = True
    divisor = 2
    while es_primo and divisor <= numero / 2:
        if numero % divisor == 0:
            es_primo = False
        divisor += 1
    return es_primo             #Devuelve TRUE or False
    

def factorial(numero):          
    #Devuelve el factorial de un número
    factorial=1
    for i in range( 1, numero+1):
        factorial*=i
    return factorial            # Devuelve el resultado del factorial en número

def factorial_en_lista (lista):
    #retorna una lista de cada factorial a partir de una lista de números.
    lista_de_factorial = []
    for numero in lista:
        factorial = 1
        for i in range (1,numero+1):
            factorial = factorial * i
        lista_de_factorial.append(factorial)
    return lista_de_factorial


def numeros_impares (lista):       
    # Devuelve en una lista los números impares de una lista de números
    num_impares = []    
    for numero in lista:
        if numero % 2 != 0:
            num_impares.append(numero)
    return num_impares         

def numeros_posiciones_impares(lista):  
    #Devuelve en una lista los números de las posiciones impares (tener en cuenta que posicion arranca en 1. y indice arranca en 0.)
    numeros_pares = []
    for i in range(len(lista)):   
        if i % 2 == 0:      #Tomo el INDICE PAR para que me devuelva la POSICIÓN IMPAR
            numeros_pares.append(lista[i])  #Se escrive asi para que escriba el número de la posición.
    return numeros_pares

def sumaposimpares(lista): 
    #Retorna la suma de las posiciones impares, tomando como posición 1 el comienzo.
    suma = 0
    for i in range (len (lista)):
        if i % 2 ==0:
            suma += lista[i]
    return suma 

def cuadrados(n1,n2): 
    #Retorna una lista de los cuadrados de todas las posibilidades entre dos números.
    cuadrado = []
    if n1 > n2:
        n1,n2 = n2,n1
    for numero in range (n1 , n2+1):
        resultado = numero**2
        cuadrado.append (resultado)
    return cuadrado


def es_divisible_por_5(numero):
    #Retorna True si el número es divisible por 5.
    if numero % 5 == 0:
        return True
    else:
        return False
    
def sumatoria_y_promedio(lista):
    #Retorna sumatoria de una lista y el promedio redondeado a 2 decimales
    sumatoria = 0
    for numero in lista:
        sumatoria = sumatoria + numero
    promedio = round(sumatoria / len(lista),2)   
    return sumatoria, promedio    

def menores_mayores_iguales (lista, k):
    #retorna 3 listas de números , con menores, mayores, iguales a k (numero)
    menores = []
    mayores = []
    iguales = []
    for numero in lista:
        if numero < k:
            menores.append (numero)
        elif numero > k:
            mayores.append (numero)
        else:
            iguales.append(numero)
    return menores, mayores, iguales

def multiplos_k (lista,k):
    # b- Devuelva una lista con aquellos que son múltiplos de k. (numeros)
    lista_multiplos = []
    for numero in lista:
        if numero % k == 0:
            lista_multiplos.append (numero)
    return lista_multiplos

def invertir_lista_en_nueva(lista):
    #retorna una nueva lista en orden inverso.
    nueva_lista = []
    for i in range(len(lista)):
        resultado = lista[len(lista)-i-1]  #i es para que recorra la lista. -1 es para q empieze por atras
        nueva_lista.append(resultado)
    return nueva_lista

def invertir_lista(lista):
    #retorna la lista invertida reemplazando la original
    lista.reverse()
    return lista

def encontrar_nombres (cadena,lista):
    #Retorna una lista con la coincidencia, se le pasa una cadena a buscar en una lista.
    encontrados=[]
    for nombre in lista:
        if cadena.lower() in nombre.lower():
            encontrados.append (nombre)
    return encontrados


def main ():
    numero = 10
    lista =[4, 2, 11, 3, 8, 7, 19, 48, 12]
    lista_str =['Di', 'buen', 'día', 'a', 'papa']
    cadena = "a"
    resultado_primo = primo (numero)
    resultado_factorial = factorial (numero)
    resultado_numeros_impares = numeros_impares (lista)
    resultado_numero_divisible_por_5 = es_divisible_por_5 (numero)
    resultado_sumatoria_y_promedio = sumatoria_y_promedio (lista)
    resultado_lista_de_factoriales = factorial_en_lista (lista)
    resultado_mayores, resultado_menores, resultado_iguales = menores_mayores_iguales(lista, numero)
    resultado_invertir_lista = (invertir_lista_en_nueva (lista_str))
    resultado_invertir_lista_en_lista = (invertir_lista (lista_str)) 
    resultado_encontra_nombre = (encontrar_nombres (cadena, lista_str))
    print (resultado_encontra_nombre)


main ()