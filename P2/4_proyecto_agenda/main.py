

#Crear un proyecto que permita gestionar (administrar) una agenda, colocar un menú de opciones para agregar contacto, mostrar todos los contactos, buscar contacto por nombre y salir.
# Notas:
# 1.- Utilizar funciones y mandar a llamar desde otro archivo.
# 2.- Utilizar listas para almacenar el nombre todo lo de mas.

# Proyecto: Agenda de contactos
# Proyecto: Agenda de contactos

# Programa principal
#Crear un proyecto que permita gestionar (administrar) una agenda, colocar un menú de opciones para agregar contacto, mostrar todos los contactos, buscar contacto por nombre y salir.
# Notas:
# 1.- Utilizar funciones y mandar a llamar desde otro archivo.
# 2.- Utilizar listas para almacenar el nombre todo lo de mas.

# Proyecto: Agenda de contactos

from agenda import (
    borrarPantalla,
    menu_principal,
    agregar_contacto,
    mostrar_contactos,
    buscar_contacto,
    modificar_contacto,
    eliminar_contacto,
    esperarTecla
)

def main():
    contactos = []
    while True:
        borrarPantalla()
        opcion = menu_principal()
        if opcion == "1":
            agregar_contacto(contactos)
        elif opcion == "2":
            mostrar_contactos(contactos)
        elif opcion == "3":
            buscar_contacto(contactos)
        elif opcion == "4":
            modificar_contacto(contactos)
        elif opcion == "5":
            eliminar_contacto(contactos)
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")
            esperarTecla()

if __name__ == "__main__":
    main()