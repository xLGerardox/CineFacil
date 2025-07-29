funciones = {
    "1": {"pelicula": "Matrix", "hora": "18:00", "precio": 45},
    "2": {"pelicula": "Inception", "hora": "20:30", "precio": 50},
    "3": {"pelicula": "Interstellar", "hora": "22:00", "precio": 55}
}

reservas = []

def cancelar_reserva(nombre_cliente):
    for r in reservas:
        if r["cliente"] == nombre_cliente:
            reservas.remove(r)
            print("Reserva cancelada:", r)
            return
    print("No se encontró una reserva para ese nombre.")

while True:
    print("Opciones: 1-Reservar | 2-Cancelar | 3-Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre del cliente: ")
        print("Funciones disponibles:")
        for clave, datos in funciones.items():
            print(clave, "-", datos["pelicula"], "-", datos["hora"], "-", "Q" + str(datos["precio"]))
        seleccion = input("Seleccione una función por número: ")
        boletos = int(input("Cantidad de boletos: "))
        total = funciones[seleccion]["precio"] * boletos

        reserva = {
            "cliente": nombre,
            "pelicula": funciones[seleccion]["pelicula"],
            "hora": funciones[seleccion]["hora"],
            "boletos": boletos,
            "total": total
        }

        reservas.append(reserva)

        print("Resumen de reserva:")
        print("Cliente:", nombre)
        print("Película:", funciones[seleccion]["pelicula"])
        print("Hora:", funciones[seleccion]["hora"])
        print("Boletos:", boletos)
        print("Total a pagar: Q", total)

    elif opcion == "2":
        nombre_cancelar = input("Nombre del cliente para cancelar: ")
        cancelar_reserva(nombre_cancelar)

    elif opcion == "3":
        break

ver_todas = input("¿Mostrar todas las reservas hechas? (s/n): ")
if ver_todas.lower() == "s":
    for r in reservas:
        print(r)

# linea de prueba