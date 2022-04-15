palabra = input("Introduce la palabra o frase a evaluar: ")
palabra=palabra.upper() #se pasan todas las letras a mayúsculas
lista1=[]
lista2=[] #la lista inversa
coincidencias = 0

#Rellenar las dos listas a comparar, omitiendo los espacios
for i in (palabra):
	if i == " ":
		continue
	else:
		lista1.append(i)

lista2=list(reversed(lista1))

#Iteración comparando las dos listas

for i in range(len(lista1)):
	if lista1[i] == lista2[i]:
		coincidencias+=1

if coincidencias == len(lista1):
	print("Es un palíndromo.")
else:
	print("No es un palíndromo.")

print("De un total de", len(lista1), "letras, han coincidido", coincidencias)

#Palíndromos de ejemplo (las vocales sin tilde)
#Alli ves Sevilla
#Anita lava la tina
#Luz azul
#Girafarig
#Dabale arroz a la zorra el abad