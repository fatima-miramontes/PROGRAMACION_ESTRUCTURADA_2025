#AGENDA DE CONTACTOS
#AGENDA DE CONTACTOS
import os

def borrarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("\n\tOprima cualquier tecla para continuar...\n\t")

def menu_principal():
    print("==== AGENDA DE CONTACTOS ====")
    print("1. 📥 Agregar contacto 📥")
    print("2. 📤 Mostrar todos los contactos 📤")
    print("3. 🔍 Buscar contacto por nombre 🔍")
    print("4. ✏️ Modificar contacto ✏️")
    print("5. ❌ Eliminar contacto ❌")
    print("6. 🚪Salir🚪")
    return input("📌 Selecciona una opción: 📌")

def agregar_contacto(contactos):
    borrarPantalla()
    print("\n\t\t..::: Agregar Contacto :::..\n") 
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    email = input("Email: ").strip()
    contacto = {"nombre": nombre, "telefono": telefono, "email": email}
    contactos.append(contacto)
    print("✅ Contacto agregado correctamente. ✅")
    esperarTecla()

def mostrar_contactos(contactos):
    borrarPantalla()
    print("\n\t\t..::: Mostrar Contactos :::..\n") 
    if contactos:
        print(f"{'Nombre':<20}{'Teléfono':<15}{'Email':<25}")
        print("-" * 60)
        for c in contactos:
            print(f"{c['nombre']:<20}{c['telefono']:<15}{c['email']:<25}")
        print("-" * 60)
        print(f"Son {len(contactos)} contactos")
    else: 
        print("No hay contactos en la agenda.")
    esperarTecla()

def buscar_contacto(contactos):
    borrarPantalla()
    print("\n\t\t..::: Buscar Contacto :::..\n") 
    nombre = input("Ingrese el nombre a buscar: ").strip().lower()
    encontrados = [c for c in contactos if c['nombre'].lower() == nombre]
    if encontrados:
        print(f"{'Nombre':<20}{'Teléfono':<15}{'Email':<25}")
        print("-" * 60)
        for c in encontrados:
            print(f"{c['nombre']:<20}{c['telefono']:<15}{c['email']:<25}")
        print("-" * 60)
    else:
        print("No se encontró el contacto.")
    esperarTecla()

def modificar_contacto(contactos):
    borrarPantalla()
    print("\n\t\t..::: Modificar Contacto :::..\n")
    nombre = input("Ingrese el nombre del contacto a modificar: ").strip().lower()
    encontrados = [i for i, c in enumerate(contactos) if c['nombre'].lower() == nombre]
    if encontrados:
        for idx in encontrados:
            c = contactos[idx]
            print(f"{idx+1}. {c['nombre']:<20}{c['telefono']:<15}{c['email']:<25}")
        seleccion = input("Ingrese el número del contacto a modificar (o ENTER para cancelar): ")
        if seleccion.isdigit():
            seleccion = int(seleccion) - 1
            if seleccion in encontrados:
                print("Deje en blanco si no desea modificar un campo.")
                nuevo_nombre = input("Nuevo nombre: ").strip()
                nuevo_telefono = input("Nuevo teléfono: ").strip()
                nuevo_email = input("Nuevo email: ").strip()
                if nuevo_nombre:
                    contactos[seleccion]['nombre'] = nuevo_nombre
                if nuevo_telefono:
                    contactos[seleccion]['telefono'] = nuevo_telefono
                if nuevo_email:
                    contactos[seleccion]['email'] = nuevo_email
                print("Contacto modificado correctamente.")
            else:
                print("Selección inválida.")
        else:
            print("Modificación cancelada.")
    else:
        print("No se encontró el contacto.")
    esperarTecla()

def eliminar_contacto(contactos):
    borrarPantalla()
    print("\n\t\t..::: Eliminar Contacto :::..\n")
    nombre = input("Ingrese el nombre del contacto a eliminar: ").strip().lower()
    encontrados = [i for i, c in enumerate(contactos) if c['nombre'].lower() == nombre]
    if encontrados:
        for idx in encontrados:
            c = contactos[idx]
            print(f"{idx+1}. {c['nombre']:<20}{c['telefono']:<15}{c['email']:<25}")
        seleccion = input("Ingrese el número del contacto a eliminar (o ENTER para cancelar): ")
        if seleccion.isdigit():
            seleccion = int(seleccion) - 1
            if seleccion in encontrados:
                eliminado = contactos.pop(seleccion)
                print(f"Contacto '{eliminado['nombre']}' eliminado correctamente.")
            else:
                print("Selección inválida.")
        else:
            print("Eliminación cancelada.")
    else:
        print("No se encontró el contacto.")
    esperarTecla()
