nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
anio = int(input("Ingresa el año actual: "))
edad_muerte = int(input("A que edad calculas llegar a vivir?: "))


def calculo_muerte() -> int:
    sumar = edad_muerte - edad
    total = sumar + anio
    return total


def meses_de_vida() -> int:
    meses = edad * 12
    return meses


def dias_de_vida() -> int:
    dias = meses_de_vida() * 30
    return dias


def dias_restantes() -> int:
    aniosrestantes = edad_muerte - edad
    diasrestantes = aniosrestantes * 365
    return diasrestantes


def meses_a_muerte() -> int:
    meses = (edad_muerte - edad) * 12
    return meses


def meses_totales() -> int:
    mesestotales = edad_muerte * 12
    return mesestotales


def porcentaje_vivido() -> float:
    porcentaje = (meses_de_vida() * 100) / meses_totales()
    return porcentaje


print("----------------------------------------------------------------")
print("Hola " + nombre)
print("----------------------------------------------------------------")
print("Llevas con vida", int(meses_de_vida()), "meses")
print("lo que equivale a alrededor de", int(dias_de_vida()), "días")
print("----------------------------------------------------------------")
print("Si calculas morir a los", int(edad_muerte), ",")
print("quiere decir que te quedan", int(dias_restantes()), "dias para vivir")
print("----------------------------------------------------------------")
print("Llevas vivido el", int(porcentaje_vivido()), "% de tu vida")
print("----------------------------------------------------------------")
print("Según tus cálculos vas a morir en el año", int(calculo_muerte()))
