import tkinter as tk

#Color de botones

fondo_entrar = "#008037"
fondo_salir = "#ff1616"
fondo_entradas = "#cb6ce6"   
fondo_incorrecto = "#004aad"
fondo_opciones = "#00c2cb"
fondo_deposito = "#d9d9d9"
fondo_mensaje = "#ff914d"
#Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("512x512+500+50")
ventana.resizable(width=False,height=False)
fondo = tk.PhotoImage(file="log.png")
fondo1 = tk.Label(ventana, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)

cuenta= tk.StringVar()
nip = tk.StringVar()
saldo = 1500
cuenta_D = "VIQD345564"
#Entradas
entrada = tk.Entry(ventana, textvar=cuenta, width=22, relief="flat", bg = fondo_entradas)
entrada.place(x=255, y=200)

entrada1 = tk.Entry(ventana, textvar=nip, show = '•', width=22, relief="flat", bg = fondo_entradas)
entrada1.place(x=255, y=270)

def login():
	cuenta_bancaria=cuenta.get()
	nip_cuenta=nip.get()

	if cuenta_bancaria == "Diego" and nip_cuenta == "1234":
		si_correcto()
	else:
		no_correcto()

def si_correcto():

	def regreso():
		window.withdraw()
		ventana.deiconify()

	#Creamos la ventana para la consulta

	def consulta():
		window.withdraw()
		window1 = tk.Toplevel()
		window1.title("Consulta")
		window1.geometry("512x512+500+50")
		window1.resizable(width=False,height=False)
		fondo = tk.PhotoImage(file="Consulta.png")
		fondo1 = tk.Label(window1, image=fondo).place(x=0, y=0, relwidth=1, relheight=1) 
		def regreso1():
			window1.withdraw()
			window.deiconify()

		cadena = "${}.00 MXN".format(saldo)
		boton7=tk.Button(window1, text=cadena, cursor="hand2", relief="flat", bg=fondo_opciones,font=("Comic Sans MS", 12, "bold"))
		boton7.place(x=190, y=250)
		boton8=tk.Button(window1, text="Salir", command=salir, cursor="hand2", relief="flat", bg=fondo_salir,font=("Comic Sans MS", 12, "bold"))
		boton8.place(x=340, y=400)
		boton9=tk.Button(window1, text="Regresar", command=regreso1, cursor="hand2", relief="flat", bg=fondo_incorrecto,font=("Comic Sans MS", 12, "bold"))
		boton9.place(x=90, y=400)

		window1.mainloop()

	def deposito():
		def verifica():
			def ventana(cadena, titulo):
				def regreso2():
					window3.withdraw()
					window.deiconify()

				window2.withdraw()
				window3 = tk.Toplevel()
				window3.title(titulo)
				window3.geometry("512x512+500+50")
				window3.resizable(width=False,height=False)
				fondo = tk.PhotoImage(file="mensaje.png")
				fondo1 = tk.Label(window3, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)
				boton12=tk.Button(window3, text="Salir", command=salir, cursor="hand2", relief="flat", bg=fondo_salir,font=("Comic Sans MS", 12, "bold"))
				boton12.place(x=360, y=410)
				boton13=tk.Button(window3, text="Otra operación", command = regreso2, cursor="hand2", relief="flat", bg=fondo_incorrecto,font=("Comic Sans MS", 12, "bold"))
				boton13.place(x=65, y=405)

				boton14=tk.Button(window3, text=cadena, cursor="hand2", relief="flat", bg=fondo_mensaje,font=("Comic Sans MS", 12, "bold"))
				boton14.place(x=140, y=200)

				window3.mainloop()



			cuenta_destino=cuenta_depo.get()
			monto=deposito.get() #Casteamos a entero el valor del saldo a depositar
			cantidad = int(monto)
			cadena = "Cuenta destino: {}\n Deposito: {}\n".format(str(cuenta_destino), str(monto))
			cadena1 = "La cuenta de origen no es \n correcta o el \n monto a depositar\n es insuficiente."
			titulo1 = "Operación exitosa"
			titulo2 = "Operación denegada"
			if (cantidad > 100) and (cuenta_destino == "AVDET18935"):
				ventana(cadena, titulo1)
			else:
				ventana(cadena1, titulo2)

		def regreso1():
			window2.withdraw()
			window.deiconify()
		#Ventana Deposito
		window.withdraw()
		window2 = tk.Toplevel()
		window2.title("Deposito")
		window2.geometry("512x512+500+50")
		window2.resizable(width=False,height=False)
		fondo = tk.PhotoImage(file="Deposito.png")
		fondo1 = tk.Label(window2, image=fondo).place(x=0, y=0, relwidth=1, relheight=1) 
			
		cuenta_depo= tk.StringVar()
		deposito = tk.StringVar()
		#Entradas
		entrada_sdestino = tk.Entry(window2, textvar=cuenta_depo, width=22, relief="flat", bg = fondo_deposito)
		entrada_sdestino.place(x=270, y=280)
		entrada_monto = tk.Entry(window2, textvar=deposito, width=22, relief="flat", bg = fondo_deposito)
		entrada_monto.place(x=270, y=330)
		boton10=tk.Button(window2, text="Cancelar", command=regreso1, cursor="hand2", relief="flat", bg=fondo_salir,font=("Comic Sans MS", 12, "bold"))
		boton10.place(x=340, y=420)
		boton11=tk.Button(window2, text="Continuar", command=verifica, cursor="hand2", relief="flat", bg=fondo_opciones,font=("Comic Sans MS", 12, "bold"))
		boton11.place(x=90, y=420)
		window2.mainloop()

	def retiro():
		def verifica():
			def ventana(cadena, titulo):
				def regreso2():
					window3.withdraw()
					window.deiconify()

				window2.withdraw()
				window3 = tk.Toplevel()
				window3.title(titulo)
				window3.geometry("512x512+500+50")
				window3.resizable(width=False,height=False)
				fondo = tk.PhotoImage(file="mensaje.png")
				fondo1 = tk.Label(window3, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)
				boton12=tk.Button(window3, text="Salir", command=salir, cursor="hand2", relief="flat", bg=fondo_salir,font=("Comic Sans MS", 12, "bold"))
				boton12.place(x=360, y=410)
				boton13=tk.Button(window3, text="Otra operación", command = regreso2, cursor="hand2", relief="flat", bg=fondo_incorrecto,font=("Comic Sans MS", 12, "bold"))
				boton13.place(x=65, y=405)

				boton14=tk.Button(window3, text=cadena, cursor="hand2", relief="flat", bg=fondo_mensaje,font=("Comic Sans MS", 12, "bold"))
				boton14.place(x=140, y=200)

				window3.mainloop()				

			monto=retiro.get()
			cantidad = int(monto)
			cadena = "Cuenta: {}\n Retiro: {}\n".format(str(cuenta_D), str(monto))
			cadena1 = "El saldo en tu cuenta \n NO es suficiente \n para el monto que \n deseas retirar."
			titulo1 = "Operación exitosa"
			titulo2 = "Operación denegada"
			if (int(saldo) >= cantidad) and (cantidad > 100) :
				ventana(cadena, titulo1)
			else:
				ventana(cadena1, titulo2)

		def regreso1():
			window2.withdraw()
			window.deiconify()
		#Ventana Retiro
		window.withdraw()
		window2 = tk.Toplevel()
		window2.title("Retiro")
		window2.geometry("512x512+500+50")
		window2.resizable(width=False,height=False)
		fondo = tk.PhotoImage(file="retiro.png")
		fondo1 = tk.Label(window2, image=fondo).place(x=0, y=0, relwidth=1, relheight=1) 

		retiro = tk.StringVar()
		#Entradas
		entrada_retiro = tk.Entry(window2, textvar=retiro, width=22, relief="flat", bg = fondo_deposito)
		entrada_retiro.place(x=270, y=305)
		boton10=tk.Button(window2, text="Cancelar", command=regreso1, cursor="hand2", relief="flat", bg=fondo_salir,font=("Comic Sans MS", 12, "bold"))
		boton10.place(x=330, y=390)
		boton11=tk.Button(window2, text="Continuar", command=verifica, cursor="hand2", relief="flat", bg=fondo_opciones,font=("Comic Sans MS", 12, "bold"))
		boton11.place(x=90, y=390)
		window2.mainloop()


	ventana.withdraw()
	window = tk.Toplevel()
	window.title("Bienvenido")
	window.geometry("512x512+500+50")
	window.resizable(width=False,height=False)
	fondo = tk.PhotoImage(file="correcto.png")
	fondo1 = tk.Label(window, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)


	#Botones para el menu de opciones

	boton4=tk.Button(window, text="Retiro", command=retiro,cursor="hand2", relief="flat", bg=fondo_opciones,font=("Comic Sans MS", 12, "bold"))
	boton4.place(x=335, y=270)

	boton5=tk.Button(window, text="Deposito", command=deposito, cursor="hand2", relief="flat", bg=fondo_opciones,font=("Comic Sans MS", 12, "bold"))
	boton5.place(x=100, y=270)

	boton6=tk.Button(window, text="Consulta Saldo", command = consulta, cursor="hand2", relief="flat", bg=fondo_opciones,font=("Comic Sans MS", 12, "bold"))
	boton6.place(x=80, y=380)

	boton7=tk.Button(window, text="Salir", command=salir, cursor="hand2", relief="flat", bg=fondo_opciones,font=("Comic Sans MS", 12, "bold"))
	boton7.place(x=345, y=380)
	window.mainloop()


def no_correcto():
	ventana.withdraw()
	root = tk.Toplevel()
	root.title("Bienvenido")
	root.geometry("512x512+500+50")
	root.resizable(width=False,height=False)
	fondo = tk.PhotoImage(file="incorrecto.png")
	fondo1 = tk.Label(root, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)
	def regreso():
		root.withdraw()
		ventana.deiconify()


	boton4=tk.Button(root, text="Regresar", command=regreso,cursor="hand2", relief="flat", bg=fondo_incorrecto,font=("Comic Sans MS", 12, "bold"))
	boton4.place(x=235, y=405)
	root.mainloop()

def salir():
	ventana.destroy()

#Botones
boton = tk.Button(ventana, text="Entrar", cursor="hand2", command=login,bg = fondo_entrar, width=12, relief="flat", font=("Comic Sans MS",12, "bold"))
boton.place(x=85, y=372)

boton1 = tk.Button(ventana, text="Salir", command=salir,cursor="hand2", bg = fondo_salir, width=12, relief="flat", font=("Comic Sans MS",12, "bold"))
boton1.place(x=310, y=372)

ventana.mainloop()



