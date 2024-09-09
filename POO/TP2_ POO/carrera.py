personaje = []
def menu():
  menuInicio = '''
  #########################################      
  #     1 - crear personaje               #
  #     2 - mostrar personaje             #
  #     3 - jugar                         # 
  #     4 - salir                         # 
  ######################################### '''
  print(menuInicio)
  opcion = int(input("ingrese su opcion elegida"))
  from typing import List
  from Personaje_clase import Personaje
  p1 = Personaje("superman", 189, 90, 105)
  print(f"el personajese llama {p1.nombre}") 
  return opcion 
cantidadPersonaje = 0 
while True:
     opcion =  menu()          
     if opcion == 1:
         cantidadPersonaje = cantidadPersonaje + 1
         personaje.append(input("nombre:"))
         personaje.append(input("altura:"))
         personaje.append(input("velocidad:"))
         personaje.append(input("resistencia:"))
         personaje.append(input("fuerza:"))
     elif opcion == 2:
         print(personaje)  
     elif opcion == 3:
         print("")
     elif opcion == 4:  
         print("gracias por utilizar este programa")
         break
         

         