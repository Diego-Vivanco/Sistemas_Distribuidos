## Antes de comenzar con el programa, se crea una tabla llamada BANCO_SD
## donde se tienen las cuentas y se realizaran los moviemientos en el saldo
## El código para la creación de BANCO_SD viene en otro archivo

import os
import sys

import random

## Se utiliza la libreria cx_Oracle para poder conectarnos con SQL Plus
import cx_Oracle


##cuenta1 = "123456"
##pass1 = "abc"
##saldo1 = 1000

##cuenta2 = "789123"
##pass2 = "qwe"
##saldo2 = 5000

##cuenta3 = "147258"
##pass3 = "asd"
##saldo3 = 700

##cuenta4 = "369258"
##pass4 = "bnm"
##saldo4 = 90

##cuenta5 = "258789"
##pass5 = "pin"
##saldo5 = 80000


# def validar():
    # print("\t **TRANSACCIONES** \n")
    # cuenta = str(input("Ingresa número de cuenta: "))
    # if(cuenta == cuenta1):
        # contraseña = str(input("Ingrese contraseña: "))
        # if (contraseña == pass1):
            # inicio = opciones(cuenta, saldo1)
        # else:
            # print("Contraseña incorrecta")
    # elif(cuenta == cuenta2):
        # contraseña = str(input("Ingrese contraseña: "))
        # if (contraseña == pass2):
            # inicio = opciones(cuenta, saldo2)
        # else:
            # print("Contraseña incorrecta")
    # elif(cuenta == cuenta3):
        # contraseña = str(input("Ingrese contraseña: "))
        # if (contraseña == pass3):
            # inicio = opciones(cuenta, saldo3)
        # else:
            # print("Contraseña incorrecta")
    # elif(cuenta == cuenta4):
        # contraseña = str(input("Ingrese contraseña: "))
        # if (contraseña == pass4):
            # inicio = opciones(cuenta, saldo4)
        # else:
            # print("Contraseña incorrecta")
    # elif(cuenta == cuenta5):
        # contraseña = str(input("Ingrese contraseña: "))
        # if (contraseña == pass5):
            # inicio = opciones(cuenta, saldo5)
        # else:
            # print("Contraseña incorrecta")
    # else:
        # print("*Usuario no encontrado*\n")
        # val = validar()

""" Función para crear la ID de la transacción,
    se escoge un numero del 100 al 999 """
def transaccion():
    id_t = random.randint(100, 999)
    return id_t



# Para escribir en el archivo
def editar_archivo_retiro(id_trans, tipo, cuenta, saldo, monto):
    archivo=open("registro.txt", "a")
    mensaje="*************************\n ID transacción:  {} \n Tipo de operación: {} \n Monto: {} \n Cuenta: {} \n Saldo actual: {}\n*************************\n".format(str(id_trans), str(tipo), str(monto), cuenta, str(saldo))
    archivo.write(mensaje)
    archivo.close()
    


 # Verifica que el archivo plano existe, de lo constario lo crea           
def estado_archivo(nueva_ruta,id_trans, tipo, cuenta, saldo, monto, otra_cuenta, otro_saldo):
    os.chdir(nueva_ruta) # Nos movemos a la nueva ruta
    if os.path.exists('registro.txt'):
        if tipo == "Retiro":
            editar_archivo_retiro(id_trans, tipo, cuenta, saldo, monto)
        elif tipo == "Deposito":
            print("Ingresar datos de las transacciones.")
            editar_archivo_deposito(id_trans, tipo, cuenta, saldo, monto, otra_cuenta, otro_saldo)
    else:
        if tipo == "Retiro":
            editar_archivo_retiro(id_trans, tipo, cuenta, saldo, monto)
        elif tipo == "Deposito":
            print("Ingresar datos de las transacciones.")
            editar_archivo_deposito(id_trans, tipo, cuenta, saldo, monto, otra_cuenta, otro_saldo)
       # editar_archivo(id_trans, monto, tipo, saldo, cuenta, otra_cuenta, otro_saldo)



# Función para cerrar la transacción
def cerrar_trans(id_trans, tipo, cuenta, saldo, monto, otra_cuenta, otro_saldo):
    directorio = os.getcwd()
    ruta=os.path.join(directorio, 'coordinador_transacciones')
    if os.path.exists(ruta):
        os.chdir(ruta)  #Nos movemos a la nueva ruta
        estado_archivo(ruta,id_trans, tipo, cuenta, saldo, monto, otra_cuenta, otro_saldo)
        os.chdir(directorio)
    else:
        os.mkdir(ruta)
        estado_archivo(ruta,id_trans, tipo, cuenta, saldo, monto, otra_cuenta, otro_saldo)
        os.chdir(directorio)

# Función para abortar el retiro
def abortar_retiro(id_trans, tipo, cuenta, saldo, monto):
    abort_op=str(input("Presione 1 si desea abortar la operación: "))
    if (abort_op == '1'):
        print("Se abortó el movimiento\n")
    else:
        if (saldo < monto):
            print("\nSaldo insuficiente...")
        else:
            saldo = saldo - monto
            print("\nTú cuenta: ", cuenta)
            print("Saldo actual: ",saldo)
            otra_cuenta="---"
            otro_saldo="0000"
            cerrar_trans(id_trans, tipo, cuenta, saldo, monto, otra_cuenta, otro_saldo)
            opciones(cuenta, saldo)

def abortar_deposito(id_trans, tipo, cuenta, saldo, monto):
    global saldo1, saldo2, saldo3, saldo4, saldo5
    abort_op=str(input("Presione 1 si desea abortar la operación: "))
    if (abort_op == '1'):
        print("Se abortó el movimiento\n")
    else:
        if (saldo < monto):
            print("\nSaldo insuficiente...")
        else:
            if cuenta == cuenta1:
                saldo1=saldo1+monto
                saldo=saldo-monto
                print("\nTú cuenta: ", cuenta)
                print("Saldo actual: ",saldo)
                print("Cuenta destino: ", cuenta1)
                print("Saldo actual de cuenta destino; ", saldo1)
                cerrar_trans(id_trans, tipo, cuenta, saldo, monto, cuenta1, saldo1)
                opciones(cuenta, saldo)
            elif cuenta == cuenta2:
                saldo2=saldo2+monto
                saldo=saldo-monto
                print("\nTú cuenta: ", cuenta)
                print("Saldo actual: ",saldo)
                print("Cuenta destino: ", cuenta2)
                print("Saldo actual de cuenta destino; ", saldo2)
                cerrar_trans(id_trans, tipo, cuenta, saldo, monto, cuenta2, saldo2)
                opciones(cuenta, saldo)
            elif cuenta==cuenta3:
                saldo3=saldo3+monto
                saldo=saldo-monto
                print("\nTú cuenta: ", cuenta)
                print("Saldo actual: ",saldo)
                print("Cuenta destino: ", cuenta3)
                print("Saldo actual de cuenta destino; ", saldo3)
                cerrar_trans(id_trans, tipo, cuenta, saldo, monto, cuenta3, saldo3)
                opciones(cuenta, saldo)
            elif cuenta==cuenta4:
                saldo4=saldo4+monto
                saldo=saldo-monto
                print("\nTú cuenta: ", cuenta)
                print("Saldo actual: ",saldo)
                print("Cuenta destino: ", cuenta4)
                print("Saldo actual de cuenta destino; ", saldo4)
                cerrar_trans(id_trans, tipo, cuenta, saldo, monto, cuenta4, saldo4)
                opciones(cuenta, saldo)
            elif cuenta==cuenta5:
                saldo4=saldo4+monto
                saldo=saldo-monto
                print("\nTú cuenta: ", cuenta)
                print("Saldo actual: ",saldo)
                print("Cuenta destino: ", cuenta5)
                print("Saldo actual de cuenta destino; ", saldo5)
                cerrar_trans(id_trans, tipo, cuenta, saldo, monto, cuenta5, saldo5)
                opciones(cuenta, saldo)


# Función para escoger la operación
def opciones(cuenta, saldo):
    """ Se crea la ID de la transacción """
    id_trans = transaccion()
    print("\n- Para realizar un RETIRO presione el 1")
    print("- Para realizar un DEPOSITO presione el 2")
    print("- Para cerrar sesión presione el 3")
    selec = str(input(">> "))
    if(selec == '1'):
        tipo = "Retiro"
        monto =int(input("\nMonto que desea retirar: "))
        abort = abortar_retiro(id_trans, tipo, cuenta, saldo, monto)
    elif(selec == '2'):
        tipo = "Deposito"
        otra_cuenta = str(input("Número de cuenta para el deposito: "))
        monto =str(input("Monto que desea depositar: "))
        #abort = abortar(id_trans, tipo, monto)
        abort=abortar_deposito(id_trans, tipo, otra_cuenta, saldo, int(monto))
    elif(selec == '3'):
        print("\nFin de sesión...")
    else:   
        print("* Intente de nuevo *\n")
        opciones()


def inicio():
    try:
        usuario=str(input('Usuario: '))
        passw = str(input("Password: "))
        
        connection=cx_Oracle.connect(
            user=usuario,
            password=passw,
            dsn='localhost:1521/ORCL',
            encoding='UTF-8'
        )
        cursor=connection.cursor()
        print(connection.version)
    except Exception as ex:
        print(ex)
        inicio()
    else:
        resultado = cursor.execute("SELECT * FROM MASTER.BANCO_SD")
        ## Borrar dato de la tabla    
        #borrarD = "DELETE FROM BANCO_SD WHERE cuenta=123456"
        #cursor.execute(borrarD)
        
        #cuenta = str(input("\nCuenta: "))
        
        #inicio = "SELECT password FROM BANCO_SD WHERE cuenta = "+cuenta
        #cursor.execute(inicio)

        resultado.fetchone()
        
        rows=cursor.fetchall()
        for row in rows:
            print(str(row))

        connection.commit()
        cursor.close()

sesion = inicio()