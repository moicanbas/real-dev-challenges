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
