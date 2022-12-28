# Crea un programa que pida tres números por teclado. El programa imprime en consola 
# la media aritmética de los números introducidos.#

number_one = int(input("Insert the first number: "))
number_two = int(input("Insert the second number: "))
number_three = int(input("Insert the third number: "))

average = (number_one + number_two + number_three)/3

print("The average is: " , average)