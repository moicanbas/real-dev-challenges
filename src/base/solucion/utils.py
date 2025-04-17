import csv
import os

ARCHIVO_RESERVAS = 'reservas.csv'

def crear_reserva(nombre, fecha, hora, servicio):
    if not validar_formato_fecha(fecha) or not validar_formato_hora(hora):
        return "❌ Formato de fecha u hora inválido."

    if existe_reserva(nombre, fecha, hora):
        return "⚠️ Ya existe una reserva para ese cliente en ese horario."

    modo_apertura = 'a' if os.path.exists(ARCHIVO_RESERVAS) else 'w'

    with open(ARCHIVO_RESERVAS, mode=modo_apertura, newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([nombre, fecha, hora, servicio])

    return "✅ Reserva registrada con éxito."


def obtener_reservas():
    if not os.path.exists(ARCHIVO_RESERVAS):
        return []

    with open(ARCHIVO_RESERVAS, mode='r', newline='') as archivo:
        reader = csv.reader(archivo)
        return list(reader)


def buscar_reservas_por_fecha(fecha):
    reservas = obtener_reservas()
    return [reserva for reserva in reservas if reserva[1] == fecha]


def cancelar_reserva(nombre, fecha):
    reservas = obtener_reservas()
    nuevas_reservas = [r for r in reservas if not (r[0] == nombre and r[1] == fecha)]

    if len(reservas) == len(nuevas_reservas):
        return "⚠️ No se encontró la reserva para cancelar."

    with open(ARCHIVO_RESERVAS, mode='w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerows(nuevas_reservas)

    return "✅ Reserva cancelada exitosamente."


def validar_formato_fecha(fecha):
    if len(fecha) != 10 or fecha[2] != '/' or fecha[5] != '/':
        return False
    return True


def validar_formato_hora(hora):
    if len(hora) != 5 or hora[2] != ':':
        return False
    return True


def existe_reserva(nombre, fecha, hora):
    reservas = obtener_reservas()
    for reserva in reservas:
        if reserva[0] == nombre and reserva[1] == fecha and reserva[2] == hora:
            return True
    return False
