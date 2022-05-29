import tkinter as tk

#Color de botones

fondo_entrar = "#0a5c0e"
fondo_salir = "#d11600"
fondo_entradas = "#dd4ef9"
fondo_incorrecto = "#1817b5"
fondo_opciones = "#25c2d4"
fondo_deposito = "#d3caca"

#Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("512x512+500+50")
ventana.resizable(width=False,height=False)
fondo = tk.PhotoImage(file="log.png")
fondo1 = tk.Label(ventana, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)

cuenta= tk.StringVar()
nip = tk.StringVar()

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

		boton8=tk.Button(window1, text="Salir", command=salir, cursor="hand2", relief="flat", bg=fondo_salir,font=("Comic Sans MS", 12, "bold"))
		boton8.place(x=340, y=400)
		boton9=tk.Button(window1, text="Regresar", command=regreso1, cursor="hand2", relief="flat", bg=fondo_incorrecto,font=("Comic Sans MS", 12, "bold"))
		boton9.place(x=90, y=400)

		window1.mainloop()

	def deposito():
		def mensaje1():
			def regreso1():
				window3.withdraw()
				window.deiconify()
			window2.withdraw()
			window3 = tk.Toplevel()
			window3.title("Consulta")
			window3.geometry("512x512+500+50")
			window3.resizable(width=False,height=False)
			fondo = tk.PhotoImage(file="mensaje.png")
			fondo1 = tk.Label(window3, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)
			boton12=tk.Button(window3, text="Salir", command=salir, cursor="hand2", relief="flat", bg=fondo_salir,font=("Comic Sans MS", 12, "bold"))
			boton12.place(x=340, y=420)
			boton13=tk.Button(window3, text="Otra operación", cursor="hand2", relief="flat", bg=fondo_incorrecto,font=("Comic Sans MS", 12, "bold"))
			boton13.place(x=90, y=420)
			window3.mainloop()
		
		def regreso1():
			window2.withdraw()
			window.deiconify()

		window.withdraw()
		window2 = tk.Toplevel()
		window2.title("Consulta")
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
		cuenta_destino=cuenta_depo.get()
		monto=deposito.get() #Casteamos a entero el valor del saldo a depositar

		boton10=tk.Button(window2, text="Cancelar", command=regreso1, cursor="hand2", relief="flat", bg=fondo_salir,font=("Comic Sans MS", 12, "bold"))
		boton10.place(x=340, y=420)
		boton11=tk.Button(window2, text="Continuar", command=mensaje1, cursor="hand2", relief="flat", bg=fondo_incorrecto,font=("Comic Sans MS", 12, "bold"))
		boton11.place(x=90, y=420)
		window2.mainloop()




	ventana.withdraw()
	window = tk.Toplevel()
	window.title("Bienvenido")
	window.geometry("512x512+500+50")
	window.resizable(width=False,height=False)
	fondo = tk.PhotoImage(file="correcto.png")
	fondo1 = tk.Label(window, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)


	#Botones para el menu de opciones

	boton4=tk.Button(window, text="Retiro", cursor="hand2", relief="flat", bg=fondo_opciones,font=("Comic Sans MS", 12, "bold"))
	boton4.place(x=335, y=270)

	boton5=tk.Button(window, text="Deposito", command=deposito, cursor="hand2", relief="flat", bg=fondo_opciones,font=("Comic Sans MS", 12, "bold"))
	boton5.place(x=100, y=270)

	boton6=tk.Button(window, text="Consulta Saldo", command = consulta, cursor="hand2", relief="flat", bg=fondo_opciones,font=("Comic Sans MS", 12, "bold"))
	boton6.place(x=80, y=380)

	boton7=tk.Button(window, text="Regresar", command=regreso, cursor="hand2", relief="flat", bg=fondo_opciones,font=("Comic Sans MS", 12, "bold"))
	boton7.place(x=330, y=380)
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



