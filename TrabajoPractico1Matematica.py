#Ejemplo 4
#Generador de Tabla de Verdad:
#Cree un programa que genere la tabla de verdad para una expresión booleana sencilla, como "A AND B".
# #Extensión: Permitan al usuario elegir entre distintas operaciones lógicas.



#Pediremos al usuario que primero elija que tabala de la verdad quiere saber
#Haremos un menu interactivo

#Iniciaremos la variable opcion la cual nos permitira movernos dentro del menu

opcion = 0

#Mostraremos 3 opciones: AND, OR y NOT
while opcion != 4:
    print("\n--Menu--")
    print("1. Compuerta AND")
    print("2. Compuerta OR")
    print("3. Compuerta NOT")
    print("4. Salir")

    
    opcion = int(input("Ingrese una de las opciones: "))


    if opcion == 1:
        print("\nTabla de verdad Puerta AND:")
        print("A | B | Salida")
        print("--------------")
        # Usamos bucles anidados para evaluar todas las combinaciones (0,0), (0,1), (1,0), (1,1)
        for A in range(2):
            for B in range(2):
                resultado = A and B
                print(f"{A} | {B} |   {int(resultado)}")

    elif opcion == 2:
        print("\nTabla de verdad Puerta OR:")
        print("A | B | Salida")
        print("--------------")
        for A in range(2):
            for B in range(2):
                resultado = A or B
                print(f"{A} | {B} |   {int(resultado)}")

    elif opcion == 3:
        print("\nTabla de verdad Puerta NOT:")
        print("A | Salida")
        print("----------")
        # NOT es una operación unaria, solo requiere un bucle
        for A in range(2):
            resultado = not A
            print(f"{A} |   {int(resultado)}")

    elif opcion == 4:
        print("Saliendo del programa...")
    else:
        print("Opción no válida.")