import sqlite3
def menu():
    while True:
        print(" Menu de opciones:")
        print("1. Nuevo rgistro")
        print("2. Modificar")
        print("3. Mostrar")
        print("4. Eliminar")
        print("5. Salir")
        opcion = input("Seleccione una opción (1-5): ").strip()
        match opcion:
            case 1:
                def nuevo_registro()
            case 2:
                def modificar()
            case 3:
                def mostrar()
            case 4:
                def eliminar()
            case 5:
                print("Saliendo del programa...")
                break


def nuevo_registro():
    conn = sqlite3.connect("gimnasio.anaymore.db")
    nombre=input("Ingrese su nombre")
    apellido=input("Ingrese su apellido")
    edad=int(input("Ingrese su edad"))
    mesdecomienzo=input("¿En qué mes empieza el gimnasio?")
    conn.execute('''insert into nuevo_registro(nombre,apellido,edad,mesdecomienzo) values ('%s','%s','%s','%s')'''%(nombre, apellido, edad, mesdecomienzo))
    conn.commit()
    conn.close()

def modificar():
    conn.sqlite3.connect('gimnasio.anaymore.db')
    nombre=input("Ingrese su nombre")
    apellido=input("Ingrese su apellido")
    sql='update gimnasio_anaymore.db set nombre=Carlos where apellido=Lujan'
    conn.execute(sql,(nombre,apellido))
    conn.commit()
    conn.close()


def eliminar():
    conn.execute("DELETE FROM usuario WHERE apellido=Ortiz")
    conn.commit()
    conn.close()

def mostrar():
    cursor = conn.execute("SELECT * FROM usuario")
    filas = cursor.fetchall()
    print(filas[1]) # muestra el regitro seleccionado, arranca desde [0]
    print("----------------------------------------------------------------")
    for fila in filas:
        print (fila)
        conn.commit()
        conn.close()