# 🏆 Proyecto: Sistema de Gestión de Reservas para Barbería

## 🎯 Enunciado

Desarrolla un sistema utilizando **Python** que permita cumplir con las siguientes funcionalidades:

1. **Registrar una nueva reserva**: El sistema debe permitir ingresar los datos de una nueva reserva: nombre del cliente, fecha y hora, y servicio solicitado (corte, barba, o ambos).
2. **Ver todas las reservas**: El usuario puede consultar todas las reservas registradas hasta el momento.
3. **Consultar reservas por fecha**: El usuario puede ingresar una fecha y el sistema debe mostrar todas las reservas para ese día específico.
4. **Cancelar una reserva**: El sistema debe permitir cancelar una reserva dado el nombre del cliente y la fecha de la reserva.
5. **Exportar reservas a un archivo CSV**: El sistema debe exportar todas las reservas registradas a un archivo `reservas.csv`.

---

## 📚 Requisitos técnicos

- **Tecnología o stack sugerido**: **Python**
- **Estructura del proyecto**:
  - Usa **funciones** para dividir la lógica de cada funcionalidad.
  - **Validaciones**: Asegúrate de que la fecha y hora se ingresen en el formato correcto, y que no haya reservas duplicadas para el mismo horario.
  - **Ciclos**: Utiliza un ciclo `while` para crear un menú interactivo donde el usuario pueda elegir entre las diferentes opciones (agregar reserva, ver reservas, cancelar, etc.).
  - **Persistencia de datos**: Los datos deben guardarse en un archivo CSV llamado `reservas.csv`. Si el archivo no existe, debe ser creado automáticamente.

- **Entrada de datos**: Los datos deben ser ingresados por el usuario a través de la terminal.

---

## 📅 Fechas importantes

- **Fecha de inicio**: 15/04/2025
- **Fecha de entrega**: 12/05/2025
