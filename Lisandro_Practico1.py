#Escribe un programa que solicite al 
# usuario ingresar 10 números y luego imprima una lista con los números pares ingresados.
def pares():
  Numeros_pares = []

  for _ in range(10):
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
      Numeros_pares.append(num)

  print("Los números pares ingresados son:", Numeros_pares)

pares()
