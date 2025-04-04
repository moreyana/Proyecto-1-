# Diccionario de estudiantes inicial
estudiantes = {
    "Juan Pérez": {"edad": 17, "materias": ["Matemáticas", "Física"]},
    "Ana Gómez": {"edad": 16, "materias": ["Química", "Historia"]},
    "Pedro López": {"edad": 18, "materias": ["Biología", "Inglés"]}
}

# Función para agregar un nuevo estudiante
def agregar_estudiante(nombre, edad, materias):
    estudiantes[nombre] = {"edad": edad, "materias": materias}
    print(f"Estudiante {nombre} agregado exitosamente.")

# Función para mostrar la lista de estudiantes
def mostrar_estudiantes():
    if estudiantes:
        for nombre, datos in estudiantes.items():
            print(f"Nombre: {nombre}, Edad: {datos['edad']}, Materias: {', '.join(datos['materias'])}")
    else:
        print("No hay estudiantes registrados.")

# Función para eliminar un estudiante
def eliminar_estudiante(nombre):
    if nombre in estudiantes:
        del estudiantes[nombre]
        print(f"Estudiante {nombre} eliminado.")
    else:
        print(f"No se encuentra al estudiante {nombre}.")

# Función para buscar un estudiante por nombre
def buscar_estudiante(nombre):
    if nombre in estudiantes:
        datos = estudiantes[nombre]
        print(f"Nombre: {nombre}, Edad: {datos['edad']}, Materias: {', '.join(datos['materias'])}")
    else:
        print(f"No se encuentra al estudiante {nombre}.")

# Función para verificar si una palabra clave está en el nombre de algún estudiante
def verificar_palabra_en_nombre(palabra):
    encontrados = [nombre for nombre in estudiantes if palabra.lower() in nombre.lower()]
    if encontrados:
        print("Estudiantes que contienen la palabra clave en su nombre:")
        for nombre in encontrados:
            print(f"- {nombre}")
    else:
        print(f"No se encontró la palabra clave '{palabra}' en los nombres de los estudiantes.")

# Función principal para manejar el menú con match
def menu():
    while True:
        print(" Menu de opciones:")
        print("1. Agregar un estudiante")
        print("2. Mostrar lista de estudiantes")
        print("3. Eliminar un estudiante")
        print("4. Buscar un estudiante")
        print("5. Verificar palabra en nombre")
        print("6. Salir")
        opcion = input("Seleccione una opción (1-6): ").strip()

        match opcion:
            case "1":
                nombre = input("Ingrese el nombre del estudiante: ").strip()
                edad = int(input("Ingrese la edad del estudiante: ").strip())
                materias = input("Ingrese las materias aprobadas (separadas por coma): ").strip().split(",")
                materias = [materia.strip() for materia in materias]  # Limpiar espacios
                agregar_estudiante(nombre, edad, materias)
            case "2":
                mostrar_estudiantes()
            case "3":
                nombre = input("Ingrese el nombre del estudiante a eliminar: ").strip()
                eliminar_estudiante(nombre)
            case "4":
                nombre = input("Ingrese el nombre del estudiante a buscar: ").strip()
                buscar_estudiante(nombre)
            case "5":
                palabra = input("Ingrese la palabra clave a buscar en los nombres: ").strip()
                verificar_palabra_en_nombre(palabra)
            case "6":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Por favor, elija una opción entre 1 y 6.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
