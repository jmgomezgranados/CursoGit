# declaración de funciones en Phyton
# def nombre_funcion(zona de parametros):
#   instrucciones de la funcion
#   return (opcional)
# #

#declaración
def new_fuction():
    msg = 'testing new fuction'
    print(msg)

#llamada
new_fuction()

def sum():
    num1 = 1
    num2 = 4
    print(num1+num2)

sum()
#función con paso de parametros
def sum_param(number1,number2):
    print(number1+number2)

sum_param(5,7)
sum_param(5,3)
sum_param(7,89)

#Funcion con paso de parametros y return
def sum_with_return(number1,number2):
    result = number1+number2
    return result

#Para mostrar el resultado "almacenado" el return se llama a la función y se le pasa los parametros 
print(sum_with_return(12,34))

#También se puede almacenar el resultado en una variable y pintar esa variable
stored_result = sum_with_return(5,30)

print(stored_result)