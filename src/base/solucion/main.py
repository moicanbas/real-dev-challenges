# Sprint 3: Usamos funciones y guardamos datos en un archivo CSV

def mostrar_menu():
    print("\n=== Juancho Barber’s Shop ===")
    print("1. Registrar nueva reserva")
    print("2. Ver todas las reservas")
    print("3. Salir")

def registrar_reserva():
    nombre = input("Nombre del cliente: ")
    fecha = input("Fecha (DD/MM/AAAA): ")
    hora = input("Hora (HH:MM): ")
    servicio = input("Servicio (corte, barba, ambos): ")

    linea = f"{nombre},{fecha},{hora},{servicio}\n"

    with open("reservas.csv", "a") as archivo:
        archivo.write(linea)

    print("✅ Reserva guardada.")

def ver_reservas():
    print("\n📅 Reservas registradas:")
    try:
        with open("reservas.csv", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) == 4:
                    print(f"- Cliente: {datos[0]}, Fecha: {datos[1]}, Hora: {datos[2]}, Servicio: {datos[3]}")
    except FileNotFoundError:
        print("No hay reservas registradas todavía.")

# Ciclo principal (bucle while)
def iniciar():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-3): ")

        if opcion == "1":
            registrar_reserva()
        elif opcion == "2":
            ver_reservas()
        elif opcion == "3":
            print("👋 Hasta la próxima!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Iniciamos el programa
iniciar()
