#tupla es una lista inmutable, una lista que no se puede modificar.
#se pueden extraer información, no se puede consultar pero si saber si un elemento existe dentro de la tupla.
#La tupla es más rápida en su ejecución, por una serie de optimizaciones, una tupla va a ocupar siempre menos espacio en memoria.

#Sintaxis
my_new_tuple = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sabado", "Domingo")
print(my_new_tuple[:])
print(my_new_tuple[2])

#El método para convertir una tupla en una lista es "list"

my_list = list(my_new_tuple)
print(my_list[:])

#El método para convertir una lista en una tupla es "tuple"

my_list_to_convert = [1,2,3,4,5]
my_tuple = tuple(my_list_to_convert)
print(my_tuple[:])

#Método para contar el número de elemenos en una tupla es count.
print(my_new_tuple.count("Miércoles"))
print("Lunes" in my_new_tuple)

#Método len para averiguar la lonfigud te la tupla
print(len(my_new_tuple))

#tupla unitaria
my_unit_tuple = ("Chema",)
print(len(my_unit_tuple))

#Desempaquetado de tuplas
tuple_info = ("John", 13,1,1995)
print("Información de la tupla: ")
print(tuple_info[:])
name, day, month, year = tuple_info
print("Informacion en las variables después del desempaquetado: ")
print("Nombre:", name)
print("Dia:", day)
print("Mes:", month)
print("Año:", year)
