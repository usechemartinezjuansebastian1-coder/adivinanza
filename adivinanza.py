print ("hola y bienvenido al juego de adivinanza")
print ("adivina que numero estoy pensado entre el 1 y el 10")

numero = 5

intento = int (input ("ingresa el numero: "))

if intento == numero:
    print ("felicidades adivinaste el numero/")
elif intento > numero:
    print ("el numero es menor")
elif intento < numero:
    print ("el numero es mayor")
else:
    print ("intentalo de nuevo")
