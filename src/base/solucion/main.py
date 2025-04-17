# # Bienvenida
# print("Bienvenido al sistema de reservas de Juancho Barber's Shop 🧔✂️")

# # Entrada de datos
# nombre_cliente = input("Ingresa tu nombre: ")
# fecha = input("Ingresa la fecha de tu reserva (DD/MM/AAAA): ")
# hora = input("Ingresa la hora de tu reserva (HH:MM): ")

# print("Servicios disponibles: corte, barba, ambos")
# servicio = input("Ingresa el servicio que deseas: ")

# # Mostrar los datos ingresados
# print("\n✅ ¡Reserva registrada con éxito!")
# print("Resumen de tu reserva:")
# print("Nombre:", nombre_cliente)
# print("Fecha:", fecha)
# print("Hora:", hora)
# print("Servicio:", servicio)

# # Datos en variables (aún no guardamos en archivos)
# # Se pueden reutilizar más adelante en otra parte del código o imprimirse de nuevo

# Sprint 2
# Lista vacía para guardar reservas
# reservas = []

# Menú principal
# while True:
#     print("\n=== Juancho Barber's Shop ===")
#     print("1. Registrar nueva reserva")
#     print("2. Ver todas las reservas")
#     print("3. Salir")
    
#     opcion = input("Selecciona una opción (1-3): ")

#     if opcion == "1":
#         # Solicitar datos al usuario
#         nombre = input("Nombre del cliente: ").strip()
#         fecha = input("Fecha (DD/MM/AAAA): ").strip()
#         hora = input("Hora (HH:MM): ").strip()
#         servicio = input("Servicio (corte, barba, ambos): ").strip().lower()
        
#         # Validaciones básicas
#         if servicio not in ["corte", "barba", "ambos"]:
#             print("❌ Servicio no válido. Intenta nuevamente.")
#             continue

#         # Verificar si ya hay una reserva igual
#         existe = False
#         for r in reservas:
#             if r["nombre"] == nombre and r["fecha"] == fecha and r["hora"] == hora:
#                 existe = True
#                 break
        
#         if existe:
#             print("⚠️ Ya existe una reserva para ese cliente en ese horario.")
#         else:
#             reservas.append({
#                 "nombre": nombre,
#                 "fecha": fecha,
#                 "hora": hora,
#                 "servicio": servicio
#             })
#             print("✅ Reserva registrada con éxito.")

#     elif opcion == "2":
#         if len(reservas) == 0:
#             print("No hay reservas registradas aún.")
#         else:
#             print("\n📅 Reservas registradas:")
#             for r in reservas:
#                 print(f"- {r['fecha']} {r['hora']} | {r['nombre']} | {r['servicio']}")

#     elif opcion == "3":
#         print("Gracias por usar el sistema. ¡Hasta pronto!")
#         break

#     else:
#         print("❌ Opción inválida. Intenta nuevamente.")


# Sprint 3: Usamos funciones y guardamos datos en un archivo CSV
# def mostrar_menu():
#     print("\n=== Juancho Barber’s Shop ===")
#     print("1. Registrar nueva reserva")
#     print("2. Ver todas las reservas")
#     print("3. Salir")

# def registrar_reserva():
#     nombre = input("Nombre del cliente: ")
#     fecha = input("Fecha (DD/MM/AAAA): ")
#     hora = input("Hora (HH:MM): ")
#     servicio = input("Servicio (corte, barba, ambos): ")

#     linea = f"{nombre},{fecha},{hora},{servicio}\n"

#     with open("reservas.csv", "a") as archivo:
#         archivo.write(linea)

#     print("✅ Reserva guardada.")

# def ver_reservas():
#     print("\n📅 Reservas registradas:")
#     try:
#         with open("reservas.csv", "r") as archivo:
#             for linea in archivo:
#                 datos = linea.strip().split(",")
#                 if len(datos) == 4:
#                     print(f"- Cliente: {datos[0]}, Fecha: {datos[1]}, Hora: {datos[2]}, Servicio: {datos[3]}")
#     except FileNotFoundError:
#         print("No hay reservas registradas todavía.")

# # Ciclo principal (bucle while)
# def iniciar():
#     while True:
#         mostrar_menu()
#         opcion = input("Elige una opción (1-3): ")

#         if opcion == "1":
#             registrar_reserva()
#         elif opcion == "2":
#             ver_reservas()
#         elif opcion == "3":
#             print("👋 Hasta la próxima!")
#             break
#         else:
#             print("Opción inválida. Intenta de nuevo.")

# # Iniciamos el programa
# iniciar()

# Bonus Sprint
from utils import crear_reserva, cancelar_reserva, obtener_reservas, buscar_reservas_por_fecha

def mostrar_menu():
    while True:
        print("\n📅 Menú de Reservas - Juancho Barber's")
        print("1. Crear reserva")
        print("2. Ver todas las reservas")
        print("3. Buscar reservas por fecha")
        print("4. Cancelar una reserva")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Nombre del cliente: ")
            fecha = input("Fecha (DD/MM/AAAA): ")
            hora = input("Hora (HH:MM): ")
            servicio = input("Servicio (corte, barba, ambos): ")
            resultado = crear_reserva(nombre, fecha, hora, servicio)
            print(resultado)

        elif opcion == '2':
            reservas = obtener_reservas()
            if reservas:
                print('Cliente | Fecha y hora | Servicio')
                for r in reservas:
                    print(f"{r[0]} - {r[1]} {r[2]} - {r[3]}")
            else:
                print("⚠️ No se han creado reservas aún.")

        elif opcion == '3':
            fecha = input("Fecha a buscar (DD/MM/AAAA): ")
            resultados = buscar_reservas_por_fecha(fecha)
            if resultados:
                print('Cliente | Hora | Servicio')
                for r in resultados:
                    print(f"{r[0]} - {r[2]} - {r[3]}")
            else:
                print("❌ No hay reservas para esa fecha.")

        elif opcion == '4':
            nombre = input("Nombre del cliente: ")
            fecha = input("Fecha de la reserva: ")
            resultado = cancelar_reserva(nombre, fecha)
            print(resultado)

        elif opcion == '5':
            print("👋 ¡Gracias por usar el sistema de reservas!")
            break

        else:
            print("❗ Opción no válida. Intenta de nuevo.")


# Ejecutamos el menú
mostrar_menu()
