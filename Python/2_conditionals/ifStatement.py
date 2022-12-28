print("Programa de evaluación de notas de alumno")
print("========================================")

print("Ingrese la nota del alumno: ")
studend_grades = input()

def evaluation(grades):
    calification = "Pass"
    if grades<5:
        calification = "Fail"
    return calification
print(evaluation(int(studend_grades)))


