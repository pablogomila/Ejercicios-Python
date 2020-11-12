nombre = input("Tu nombre: ")
edad = int(input("Tu edad: "))
def calculo():
    sumar = 100 - edad
    total = sumar + 2020
    return total


print("Hola " + nombre,",")
print("vas a cumplir 100 años en el año")
print(calculo())