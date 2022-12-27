# Un diccionario es una estructura de datos que nos pemite almacenar
# valores de diferentes tipos e incluso listas y otros diccionarios.
# 
# La principial caracteristica es que los datos se almacenan asociados
# a una clave de tal forma que se crea una asociación de tipo
#  clave : valor para cada elemento almacenado
#
# Los elementos almacenados no están ordenados, el orden es indiferente 
# a la hora de almacenar información en un diccionario.
my_diccionary = {"Alemania":"Berlín", "Francia":"París", "Reino Unido": "Londres", "España":"Madrid"}
print(my_diccionary["Francia"])

#Agregar un elemento más al diccionario
my_diccionary["Italia"] = "Lisboa"
print(my_diccionary)

#Modificar un valor
my_diccionary["Italia"] = "Roma"
print(my_diccionary)

#Eliminar un elemento:
del my_diccionary["Reino Unido"]
print(my_diccionary)

#Diccionario dentro de un diccionario con tupla
player = {"number":23 , "Last Name": "Jordan" , "First Name":"Michael" , "Team":"Chicago", "nbaRings":{"seasons":[1991,1992,1993,1996,1997,1998]}}
print("Player", player)

#metodos para diccionarios
print("Metodo Key: ", player.keys())
print("Metodo Values: ", player.values())
print("Metodo lengh: ", len(player))
