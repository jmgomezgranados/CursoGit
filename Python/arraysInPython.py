#Listas o arrays en Python

#Sintaxis
#list_name = [elem1, elem2, elem3]

my_list = ["Leonard", "Howard", "Sheldon", "Rajesh"]
print("-My list:")
print(my_list[:])

print("-Showing index 2:")
print(my_list[2])

print("-Showing index excluded :")
print(my_list[1:3])

print("-Showing index from on:")
print(my_list[1:])

print("-Showing all my list:")
for i in my_list:
    print(i)

#añadir un elemento al final de un array
my_list.append("Penny")
print(my_list[:])

#añadir un elemento en medio de un array
my_list.insert(2,"Bernadette")
print(my_list[:])

#añadir varios elementos al final de un array
my_list.extend(["Amy", "Stuart"])
print(my_list[:])

#saber en que indice está un elemento
print(my_list.index("Sheldon"))

print("pepe" in my_list)
print("Amy" in my_list)

#para eliminar un elemento de la lista
my_list.remove("Bernadette")
print(my_list[:])

#para eliminar el ultimo elemento de la lista
my_list.pop()
print(my_list[:])

#operadores aritmeticos con listas + y *

my_list_to_sum = ["Bernadettem", "Stuart"]

my_list_result = my_list + my_list_to_sum
print(my_list_result[:])

my_list_to_multiply = ["Show", 5, True, 3.14] * 3
print(my_list_to_multiply[:])