from Personaje_clase import Personaje

personajes = []  

def crear_personaje():
    
    nombre = input("Ingrese el nombre del personaje: ")
    altura = int(input("Ingrese la altura: "))
    velocidad = int(input("Ingrese la velocidad: "))
    resistencia = int(input("Ingrese la resistencia: "))
    fuerza = int(input("Ingrese la fuerza: "))
    nuevo_personaje = Personaje(nombre, altura, velocidad, resistencia, fuerza)
    personajes.append(nuevo_personaje)
    print(f"El personaje {nuevo_personaje.nombre} ha sido creado.")

def mostrar_personajes():
    for personaje in personajes:
        personaje.mostrar_info()

def menu():
    print("""
    #########################################      
    #     1 - Crear personaje               #
    #     2 - Mostrar personajes            #
    #     3 - jugar                         #
    #     4 - Salir                         # 
    ######################################### """)
    opcion = int(input("Ingrese su opción elegida: "))
    return opcion

while True:
    opcion = menu()
    if opcion == 1:
        crear_personaje()
    elif opcion == 2:
        mostrar_personajes()
    elif opcion == 3:
      print("terminar")
    elif opcion == 4:
        break
    else:
        print("Opción inválida.")