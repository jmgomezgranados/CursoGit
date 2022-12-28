#Crea un programa que pida dos números por teclado. El programa tendrá una función 
#llamada “DevuelveMax” encargada de devolver el número más alto de los dos
#introducidos.

number_one = int(input("Inserte el valor del primer número: "))
number_two = int(input("Inserte el valor del segundo número: "))

def DevuelveMax(n1,n2):
    if n1 > n2:
        print("El número ", n1, " es el número más alto.")
    elif n2 > n1:
        print("El número ", n2, " es el más alto.")
    else:
        print("Son iguales")


DevuelveMax(number_one, number_two)