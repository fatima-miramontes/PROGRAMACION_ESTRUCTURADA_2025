agenda_contactos = {
    "RUBEN": ["6181234567", "ruben@example.com"] 
}

import mysql.connector
from mysql.connector import Error
def conectar():
    try:
        conexion = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password = "",
            database = "bd_agenda"
        )
        return conexion
    except Error as e :
        print(f"El error que se presento es: {e}")
        return None

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\tOprima cualquier tecla para continuar...\n\t")

def menu_principal(): 
    print("\n\t\t 💾..::: Sistema de Gestión de Agenda de Contactos :::..💾 \n\n\t\t1️⃣  Agregar contacto\n\t\t2️⃣  Mostrar contactos\n\t\t3️⃣  Buscar contacto\n\t\t4️⃣  Modificar contacto\n\t\t5️⃣  Eliminar contacto\n\t\t6️⃣  SALIR")
    opcion = input("\n\t\t👉 Elige una opción (1-6): ")
    return opcion

def agregar_contacto(agenda_contactos):
    conexionBD = conectar()
    if conexionBD != None:
        borrarPantalla()
        print("\n\t\t📥 ..::AGREGAR CONTACTO::..📥 ")
        
        nombre = input("\n\tNombre: ").upper().strip()
        
        # Verificar si el contacto ya existe
        if nombre in agenda_contactos:
            print("\n\t❌ El contacto ya existe.")
        else:
            telefono = input("\tTeléfono: ").strip()
            email = input("\tEmail: ").lower().strip()
            
            # Agregar al diccionario (estructura exacta que pide el profesor)
            agenda_contactos[nombre] = [telefono, email]
            print("\n\t✅ Contacto agregado con éxito.")
            
            # Opcional: Guardar en base de datos (si lo requieres)
            if conectar():
                try:
                    cursor = conexionBD.cursor()
                    sql = "INSERT INTO agenda (Nombre, Telefono, Gmail) VALUES (%s, %s, %s)"
                    cursor.execute(sql, (nombre, telefono, email))
                    conexionBD.commit()
                except Error as e:
                    print(f"\t❌ Error al guardar en BD: {e}")
        
        esperarTecla()
        return agenda_contactos



def mostrar_contactos(agenda_contactos):
    conexionBD = conectar()
    if conexionBD is None:
        print("\n\t❌ Error al conectar a la base de datos")
        esperarTecla()
        return

    borrarPantalla()
    print("\n\t\t\U0001F4DD ..::LISTA DE CONTACTOS::.. \U0001F4DD ")
    
    try:
        cursor = conexionBD.cursor()
        
        # 1. Obtener contactos de la base de datos
        cursor.execute("SELECT Nombre, Telefono, Gmail FROM agenda")
        contactos_bd = cursor.fetchall()
        
        # 2. Actualizar el diccionario en memoria
        agenda_contactos.clear()  # Limpiar datos antiguos
        for nombre, telefono, gmail in contactos_bd:
            agenda_contactos[nombre] = [telefono, gmail]
        
        # 3. Mostrar los contactos
        if not agenda_contactos:
            print("\n\t\u274C No hay contactos registrados.")
        else:
            print("-"*60)
            print(f"{'Nombre':>15}   {'Número':>15}   {'Email':>15}")
            print("-"*60)
            
            for nombre, datos in agenda_contactos.items():
                print(f"{nombre:>15}   {datos[0]:>15}   {datos[1]:>15}")
            
            print("-"*60)
            
    except Error as e:
        print(f"\n\t❌ Error al consultar la BD: {e}")
    finally:
        if conexionBD.is_connected():
            cursor.close()
            conexionBD.close()
    
    esperarTecla()
#imprimir print(f"{i} agenda {agenda[0]:>15}")
            
def buscar_contactos(agenda_contactos):
    conexionBD = conectar()
    if conexionBD != None:
        borrarPantalla()
        print("\n\t\t\U0001F50D ..::BUSCAR CONTACTO::.. 🔍")
        nombre = input("\n\tNombre a buscar: ").upper().strip()
        if nombre in agenda_contactos:
            print(f"\n\t🔹 {nombre}:")
            print(f"\t   Teléfono: {agenda_contactos[nombre][0]}")
            print(f"\t   Email: {agenda_contactos[nombre][1]}")
            esperarTecla()
        else:
            print("\n\t❌ Contacto no encontrado.")
            esperarTecla()

def modificar_contacto(agenda_contactos):
    conexionBD = conectar()
    if conexionBD is None:
        print("\n\t❌ Error al conectar a la base de datos")
        esperarTecla()
        return agenda_contactos

    borrarPantalla()
    print("\n\t\t✏️ ..::MODIFICAR CONTACTO::..✏️")
    nombre_original = input("\n\tNombre del contacto a modificar: ").upper().strip()

    if nombre_original not in agenda_contactos:
        print("\n\t❌ El contacto no existe")
        esperarTecla()
        conexionBD.close()
        return agenda_contactos

    print("\n\t\t📥 ..::MODIFICACIÓN DE DATOS::..📥 ")
    nuevo_nombre = input("\n\tIngrese el nuevo nombre: ").upper().strip()
    telefono = input("\tTeléfono: ").strip()
    email = input("\tEmail: ").upper().strip()

    try:
        cursor = conexionBD.cursor()
        
        # Sentencia SQL para actualizar el contacto
        sql = """UPDATE agenda 
                 SET Nombre = %s, Telefono = %s, Gmail = %s 
                 WHERE Nombre = %s"""
        
        cursor.execute(sql, (nuevo_nombre, telefono, email, nombre_original))
        conexionBD.commit()
        
        # Actualizar el diccionario local
        del agenda_contactos[nombre_original]  # Eliminar el nombre antiguo
        agenda_contactos[nuevo_nombre] = [telefono, email]
        
        print("\n\t✅ Contacto modificado con éxito")
        print("LA OPERACIÓN SE REALIZÓ CON ÉXITO")
        
    except Error as e:
        print(f"\n\t❌ Error al modificar en BD: {e}")
    finally:
        if conexionBD.is_connected():
            cursor.close()
            conexionBD.close()

    esperarTecla()
    return agenda_contactos


def eliminar_contacto(agenda_contactos):
    conexionBD = conectar()
    if conexionBD != None:
        borrarPantalla()
        print("\n\t\t🗑️ ..::ELIMINAR CONTACTO::..🗑️")
    if not agenda_contactos:
        print("\u26A0NO hya contactos en la Agenda\u26A0")
    else:
        nombre = input("\n\tNombre del contacto a eliminar: ").upper().strip()
        if nombre in agenda_contactos:
            print("\U0001F4C2Valores actuales")
            print(f"nombre: {nombre}\nTelefono: {agenda_contactos[nombre][0]}\n{agenda_contactos[nombre][1]}")
            resp=input("\U0001F4DBDeseas eliminar los valores? (si/no)\U0001F4DB").lower().strip()
            if resp=="si":
                agenda_contactos.pop(nombre)
                print("\u2705Operación realizada con exito\u2705")
        else:
            print("\n\t❌ Contacto no encontrado.")
            esperarTecla()

    cursor = conexionBD.cursor()
    sql = "delete from agenda where agenda . Nombre = %s"
    valor = nombre
    cursor.execute = (sql,valor )
    conexionBD.commit()
    return agenda_contactos


def main():
    conexionBD = conectar()
    if conexionBD != None:
        opcion = True
        agenda_contactos = {}  

        while opcion:
            borrarPantalla()
            opcion = menu_principal()
            
            if opcion == "1":
                agregar_contacto(agenda_contactos)
                
            elif opcion == "2":
                mostrar_contactos(agenda_contactos)
                
            elif opcion == "3":
                buscar_contactos(agenda_contactos)
                
            elif opcion == "4":
                modificar_contacto(agenda_contactos)
                
            elif opcion == "5":
                eliminar_contacto(agenda_contactos)
                esperarTecla()
            elif opcion == "6":
                opcion = False
                borrarPantalla()
                print("\n\t🚪 Terminaste la ejecución del SW 🚪")
            else:
                print("\n\t❌ Opción inválida.Vuelva a intentarlo")
                esperarTecla()