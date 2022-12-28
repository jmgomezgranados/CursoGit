president_salary = input("Introduce salario presidente: ")
print("Salario presidente: " + str(president_salary)) 
# str funcion que me permite convertir un entero en un string
# así poder concatenar distintos tipos de datos en mismo formato ya que python es un
# lenguaje de programación fuertemente tipado y no deja concatenar distintos tipos de datos.

director_salary = input("Introduce salario director: ")
print("Salario director: " + str(director_salary))

area_manager_salary = input("Introduce salario jefe de area: ")
print("Salario jefe de area: " + str(area_manager_salary))

admin_salary = input("Introduce salario administrativo: ")
print("Salario adminstrativo: " + str(admin_salary))

# vamos a comparar los sueldos de los trabajadores con los concatenadores

if admin_salary < area_manager_salary < director_salary < president_salary:
    print("Está todo correcto")
else:
    print("Algo está chungo")

