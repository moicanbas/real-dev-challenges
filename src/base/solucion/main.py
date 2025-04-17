# Lista vacía para guardar reservas
reservas = []

# Menú principal
while True:
    print("\n=== Juancho Barber's Shop ===")
    print("1. Registrar nueva reserva")
    print("2. Ver todas las reservas")
    print("3. Salir")
    
    opcion = input("Selecciona una opción (1-3): ")

    if opcion == "1":
        # Solicitar datos al usuario
        nombre = input("Nombre del cliente: ").strip()
        fecha = input("Fecha (DD/MM/AAAA): ").strip()
        hora = input("Hora (HH:MM): ").strip()
        servicio = input("Servicio (corte, barba, ambos): ").strip().lower()
        
        # Validaciones básicas
        if servicio not in ["corte", "barba", "ambos"]:
            print("❌ Servicio no válido. Intenta nuevamente.")
            continue

        # Verificar si ya hay una reserva igual
        existe = False
        for r in reservas:
            if r["nombre"] == nombre and r["fecha"] == fecha and r["hora"] == hora:
                existe = True
                break
        
        if existe:
            print("⚠️ Ya existe una reserva para ese cliente en ese horario.")
        else:
            reservas.append({
                "nombre": nombre,
                "fecha": fecha,
                "hora": hora,
                "servicio": servicio
            })
            print("✅ Reserva registrada con éxito.")

    elif opcion == "2":
        if len(reservas) == 0:
            print("No hay reservas registradas aún.")
        else:
            print("\n📅 Reservas registradas:")
            for r in reservas:
                print(f"- {r['fecha']} {r['hora']} | {r['nombre']} | {r['servicio']}")

    elif opcion == "3":
        print("Gracias por usar el sistema. ¡Hasta pronto!")
        break

    else:
        print("❌ Opción inválida. Intenta nuevamente.")
