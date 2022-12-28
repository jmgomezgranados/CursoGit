print("Verificación de notas")
print("=====================")

student_grade = int(input("Inserte su nota, por favor; "))

if student_grade < 5:
    print("Insuficiente")
elif student_grade < 6:
    print("Suficiente")
elif student_grade < 7:
    print("Bien")
elif student_grade < 9:
    print("Notable")
else:
    print("Sobresaliente")

print("Gracias por su colaboración.")