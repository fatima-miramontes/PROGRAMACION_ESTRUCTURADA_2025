"""# proyecto-1-
# -Crear-un-proyecto que permita Gestionar (Administrar) peliculas, colocar un-menu-de-opciones para agregar, eliminar, modificar-y-consultar-peliculas..
# Notas:
# 1.--Utilizar funciones y mandar llamar desde otro archivo
# 2.--Utilizar listas para almacenar el nombre y 3 calificaciones de los alumnos

"""

import calificaciones

def main():
    opcion = True
    datos=[]

    while opcion:
        calificaciones.borrarPantalla()
        opcion = calificaciones.menu_principal()
        match opcion:
            case "1":
                calificaciones.agregar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.calcular_promedios()
                calificaciones.esperarTecla()
            case "4":
                opcion = False
                calificaciones.borrarPantalla()
                print("\n\tTerminaste la ejecucion del SW")
            case "5":
                calificaciones.buscar(datos)
                calificaciones.esperarTecla
            case _:
                opcion = True
                input("\n\tOpción inválida, vuelva a intentarlo.... por favor")
                
if __name__ == "__main__":
    main ()