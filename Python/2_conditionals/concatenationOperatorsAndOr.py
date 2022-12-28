print("Programa de becas 2023")
print("======================")

school_distance = int(input("Introduce la distancia a la escuela en km: "))
print("Distancia escuela: " + str(school_distance))

number_of_siblings = int(input("Introduzca el número de hermanos: "))
print("Número de hermanos: " + str(number_of_siblings))

family_salary = int(input("Introduzca el salario familiar: "))
print("Salario familiar: " + str(family_salary))

if school_distance > 40 and number_of_siblings > 2 or family_salary < 20000:
    print("Solicita tu beca")
else:
    print("No tienes derecho a beca")