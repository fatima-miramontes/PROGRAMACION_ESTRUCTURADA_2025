#Proyecto final 
#Crear un proyecto que permita gestionar (administrar) productos de cooppel, colocar un menú de opciones para agregar, mostrar, modificar, checar el precio, eliminar. 
# Notas:
# 1.- Utilizar funciones y mandar a llamar desde otro archivo.
# 2.- Utilizar listas para almacenar el nombre y el precio.
# 3.- Utilizar el concepto de manejo de excepciones.


import cooppel

def main():
    opcion = True
    productos = []

    while opcion:
        cooppel.borrarPantalla()
        opcion = cooppel.menu_principal()
        
        match opcion:
            case "1":
                cooppel.agregar_producto(productos)
                cooppel.esperarTecla()
            case "2":
                cooppel.mostrar_productos(productos)
                cooppel.esperarTecla()
            case "3":
                cooppel.modificar_producto(productos)
                cooppel.esperarTecla()
            case "4":
                cooppel.checar_precio(productos)
                cooppel.esperarTecla()
            case "5":
                cooppel.eliminar_producto(productos)
                cooppel.esperarTecla()
            case "6":
                opcion = False
                cooppel.borrarPantalla()
                print("✅Terminaste la ejecución del SW✅")
            case _:
                print("❌Opción inválida❌")
                cooppel.esperarTecla()

if __name__ == "__main__":
    main()
