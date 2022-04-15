from tkinter import Tk, Entry, Button, Label, StringVar

#----------- Raiz -----------

root = Tk()
root.title("Calcular números primos")
root.iconbitmap("calculadora.ico")
root.config(bg="#339900", width=300, height=150)

#----------- Variables de entrada y salida -----------

texto_entrada = StringVar()
texto_salida = StringVar()

#----------- Función que calcula si es un número primo -----------

def calculo(num):
	mensaje=""
	#Primera comprobación: si es un número.
	#No comprueba si es 0 o un número negativo
	if num.isnumeric():
		num = int(num)
		texto_salida.set(num)

		#Variables para operar en la función
		comprobacion = 0
		resultado = 0

		#Bucle para obtener el módulo 
		for i in range(num):
			resultado = num%(i+1)
			if resultado==0: #Si el módulo es 0 se incrementa la variable comprobacion
				comprobacion=comprobacion + 1
			#El valor de la variable comprobación indica si el número es primo
			if comprobacion == 2:
				mensaje="El número " + str(num) + " es un número primo"
				texto_salida.set(mensaje)
			else:
				mensaje="El número " + str(num) + " NO es un número primo"
				texto_salida.set(mensaje)

	else:
		texto_salida.set("Introduce un número")

def salir():
	root.destroy()

#----------- Interfaz gráfica y llamada a las funciones -----------
entrada = Entry(root, textvariable=texto_entrada)
entrada.grid(row=0, column=0, padx=5,pady=5)
entrada.config(fg="#0000FF", font=('Verdana', 12, 'bold'))

boton = Button(root)
boton.grid(row=0, column=1, padx=5,pady=5, sticky="w")
boton.config(text="Comprobar", bg="#0000FF", fg="#FFFFFF", font=("bold"), command=lambda:calculo(texto_entrada.get()))

salida = Label(root, textvariable=texto_salida)
salida.grid(row=1, column=0, columnspan=3, sticky="n", padx=5,pady=5)
salida.config(bg="#339900", fg="#FFFF00", font=('Verdana', 14, 'bold'))

botonSalir = Button(root)
botonSalir.grid(row=0, column=2, padx=5,pady=5, sticky="w")
botonSalir.config(text="Salir", width="4", bg="#FF0000", fg="#FFFFFF", font=("bold"), command=salir)

root.mainloop()