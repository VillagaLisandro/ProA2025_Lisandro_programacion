from Personaje_clase import Personaje 
## nombre, altura, velocidad, fuerza

p1 = Personaje("superman", 189, 90, 105)
print(f"el personajese llama {p1.nombre}") 

def menu():
  menuInicio = '''
  #########################################      
  #     1 - crear personaje               #
  #     2 - mostrar personaje             #
  #     3 - salir                         # 
  ######################################### '''
  print(menuInicio)
  opcion = int(input("ingrese su opcion elegida"))
  return opcion 
while True:
     opcion =  menu()
        if opcion == 1: 
    