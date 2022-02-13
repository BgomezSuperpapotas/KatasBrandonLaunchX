# Añadir el código necesario para crear una variable que guarde la velocidad del asteroide.
# Escribe una expresión de prueba para calcular si necesita una advertencia.
# Agregue las instrucciones que se ejecutarán si la expresión de prueba es true o false.
vel_asteroide_sol = 49  #velocidad asteroide
print("Ejercicio 1");
if vel_asteroide_sol > 25:
    print("Advertencia, la velocidad del asteroide referente al sol es superior a 25km/hr.");
else:
    print("El asteroide va a %d km/h referente al sol y por lo tanto no es necesaria una advertencia"%vel_asteroide_sol)

# Agrega el código para crear una variable para un asteroide que viaja a 19 km/s
# Escribe varias expresiones de prueba para determinar si puedes ver el rayo de luz desde la tierra
# Agrega las instrucciones que se ejecutarán si las expresiones de prueba son True o False

print("\n\nEjercicio 2");
vel_asteroide_tierra = 19    #velocidad asteroide
if vel_asteroide_tierra > 20:
    print('Busca un rayo de luz! Un asteroide viene hacia la atmosfera!')
elif vel_asteroide_tierra == 20:
    print('Busca un rayo de luz! Un asteroide viene hacia la atmosfera!')
else:
    print('El asteroide no generara luz.')

# Agrega el código para crear nuevas variables para la velocidad y el tamaño del asteroide
# Para probar el código, prueba con varias velocidades y tamaños
# Escribe varias expresiones de prueba o combinaciones de expresiones de prueba para determinar qué mensaje se debe enviar a Tierra.

print("\n\nEjercicio 3");
vel_asteroide_3 = 25   #velocidad asteroide
tam_asteroide_3 = 40   #tamaño asteroide
if vel_asteroide_3 > 25 and tam_asteroide_3 > 25:
    print('Peligro, este asteroide puede causar daño significativo a la tierra!')
elif vel_asteroide_3 >= 20:
    print('Busca un rayo de luz! Un asteroide viene hacia la atmosfera!')
elif tam_asteroide_3 < 25:
    print('Tranquilos! El asteroide se destruira en la atmosfera')
else:
    print('El asteroide no generara luz.')
