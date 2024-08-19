Tareas_anadidas = []
def menu():
  menuInicio = '''
  #########################################      
  #     1 - añadir tarea                  #
  #     2 - ver todas las tareas          #
  #     3 - marcar tarea como completa    #
  #     4 - Salir                         #
  ######################################### '''
  print(menuInicio)
  opcion = int(input("Ingrese la opción deseada: "))
  return opcion
while True:
 opcion = menu()
  if opcion == 1:
      while True:
          nueva_tarea = input("Ingrese su tarea (o 'salir' para finalizar): ")
          if nueva_tarea.lower() == 'salir':
              break
          Tareas_anadidas.append(nueva_tarea)
  elif opcion == 2:
      print("Tareas ingresadas:")
      for tarea in Tareas_anadidas:
          print(tarea)
  elif opcion == 3:
      if Tareas_anadidas:
          print("Tareas pendientes:")
          for i, tarea in enumerate(Tareas_anadidas, start=1):
              print(f"{i}. {tarea}")
          tarea_a_marcar = int(input("Ingrese el número de la que desea marcar: "))
          if 1 <= tarea_a_marcar <=  len(Tareas_anadidas):
              Tareas_anadidas[tarea_a_marcar - 1] = f"{Tareas_anadidas[tarea_a_marcar - 1]}"
              print("su tarea se marco como completada.")
          else:
              print("Número de tarea inválido.")
      else:
          print("No hay tareas pendientes.")
  elif opcion == 4:
      print("Gracias por utilizar este programa")
      break
  else:
      print("Opción no válida. Intente nuevamente.")
