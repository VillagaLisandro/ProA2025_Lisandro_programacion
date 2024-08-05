#Escribe un programa que solicite al usuario 
# ingresar una frase y luego cuente e imprima la cantidad de vocales (a, e, i, o, u) que contiene la frase. 
def contarVocales(frase):
    
  vocales = "aeiouAEIOU"
  conteo = 0
  for letra in frase:
    if letra in vocales:
      conteo += 1
  return conteo

frase = input("ingrese una frase")  
numeros_vocales = contarVocales(frase)

print(f"La frase '{frase}' tiene {numeros_vocales} vocales.")

