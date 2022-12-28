# Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos 
# deberán ser almacenados en una lista y mostrar en consola el mensaje: “Los datos 
# personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por teclado)

personal_info = {input("Nombre: "), input("Dirección: "), input("Telefono: ")}
print("Información personal: ")
for i in personal_info:
    print(i)

name = input("Nombre: ")
address = input("Dirección: ")
phone = int(input("Telefono: "))

personal_data = [name, address, phone]
print("Los datos personales son: ", personal_data[0], personal_data[1] , personal_data[2] )