def cargar_lista ():
    #Devuelve una lista de números ingresados por el usuario. Ingresa Salir para terminar.
    numeros = []    #Creo una lista vacia
    ingreso = True  #Creo una variable verdadera
    while ingreso:  #Bucle mientras sea la variable verdadera
        usuario = input ("Ingrese un número para agregarlo a la lista o escriba 'salir' para terminar:  ")  
        if usuario.isdigit():   #si es digito   
            numeros.append (float (usuario))    #agrega a lista
        elif usuario.lower () == "salir":   #si es str combierte a minusculas igual salir
            ingreso=False   #Sale del bucle
        else:
            print ("Dato inválido") #Ninguno de los anteriores, dato inválido
    return numeros  #retorna lista

def main ():
    print (cargar_lista())

main ()


