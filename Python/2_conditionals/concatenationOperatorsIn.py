print("Asignaturas optativas 2023:")
print("Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")
print("==========================")

option = input("Escribe la asignatura escogida: ")
course = option.lower()#convierto la cadena de texto en minusculas ya que python es case sensitive

if course in ("informática gráfica" , "pruebas de software", "usabilidad y accesabilidad"):
    print("Asignatura elegida: " + course)

else:
    print("La asignatura elegida no está entre las opcionales.")
