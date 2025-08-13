from funciones import *
from usuarios import usuarioss
from productos import productoss
from ventas import ventass
from conexionBD import reiniciar_tabla 
import getpass

def main():
    usuario_actual = None 
    
    while True:
        if not usuario_actual:
            opcion = menu_principal()
            
            if opcion == "1":
                borrar_pantalla()
                print("\n" + "=" * 50)
                print(" INICIO DE SESIÓN")
                print("=" * 50)
                email = input("Email: ").strip()
                contrasena = getpass.getpass("Contraseña: ").strip()

                usuario_actual = usuarioss.autenticar_usuario(email, contrasena)
                if usuario_actual:
                    print(f"\nBienvenido {usuario_actual['nombre']}!")
                    esperar_tecla()
                else:
                    print("\n❌ Credenciales incorrectas")
                    esperar_tecla()

            elif opcion == "2":  # Registro
                borrar_pantalla()
                print("\n" + "=" * 50)
                print(" REGISTRO DE USUARIO")
                print("=" * 50)
                nombre = input("Nombre: ").strip().title()
                apellido = input("Apellido: ").strip().title()
                email = input("email: ").strip().lower()
                contrasena = getpass.getpass("Contraseña: ").strip()
                registrar = usuarioss.registrar_usuario(nombre, apellido, email, contrasena)
                if registrar:
                    print("\n✅ Usuario registrado exitosamente!")
                else:
                    print("\n❌ Error al registrar usuario")
                esperar_tecla()

            elif opcion == "3":  # Salir
                print("\n¡Hasta pronto! 🍻")
                break
                
            else:
                print("\n❌ Opción inválida")
                esperar_tecla()

        else:  # Menú principal para usuarios autenticados
            opcion = menu_inventario()
            
            if opcion == "1":  # Realizar venta
                borrar_pantalla()
                print("\n" + "=" * 50)
                print(" REGISTRAR VENTA")
                print("=" * 50)
                productos = productoss.listar()
                print("\nPRODUCTOS DISPONIBLES:")
                print(f"{'ID':<5}{'Nombre':<20}{'Precio':<10}{'Stock':<10}")
                print("-" * 45)
                for p in productos:
                    print(f"{p['id']:<5}{p['nombre'][:18]:<20}{formatear_precio(p['precio']):<10}{p['stock']:<10}")
                
                productos_seleccionados = []
                while True:
                    try:
                        print("\n" + "-" * 50)
                        id_producto = int(input("ID del producto (presiona 0 para finalizar con la compra): "))
                        if id_producto == 0:
                            break
                            
                        producto = next((p for p in productos if p['id'] == id_producto), None)
                        if not producto:
                            print("❌ ID no válido")
                            continue
                            
                        cantidad = int(input(f"Ingresa la cantidad de {producto['nombre']} que deseas comprar ({producto['stock']} en disponibilidad): "))
                        if cantidad <= 0:
                            print("❌ La cantidad debe ser mayor que 0")
                            continue

                        if cantidad > producto['stock']:
                            print(f"❌ Stock insuficiente... (Disponible: {producto['stock']})")
                            continue
                        producto['stock'] -= cantidad    
                        productos_seleccionados.append({
                            'id': producto['id'],
                            'cantidad': cantidad,
                            'precio': producto['precio']})
                        print(f"✅ Añadido: {cantidad} x {producto['nombre']}")

                    except ValueError:
                        print("❌ Ingresa un valor numérico")
                        continue
                
                if productos_seleccionados:
                    if ventass.registrar_venta(usuario_actual['id'], productos_seleccionados):
                        print("\n✅ Venta registrada!")
                        print("\nRESUMEN DE VENTA:")
                        print("-" * 30)
                        total = 0
                        for item in productos_seleccionados:
                            subtotal = item['cantidad'] * item['precio']
                            prod_nombre = next(p['nombre'] for p in productos if p['id'] == item['id'])
                            print(f"{item['cantidad']} x {prod_nombre}")
                            print(f"  {formatear_precio(item['precio'])} c/u = {formatear_precio(subtotal)}")
                            total += subtotal
                        print("-" * 30)
                        print(f"TOTAL: {formatear_precio(total)}")
                    else:
                        print("\n❌ Error al registrar venta")
                else:
                    print("\n⚠️ No se seleccionaron productos")
                esperar_tecla()
                            
            elif opcion == "2":  # Registrar producto
                borrar_pantalla()
                print("\n" + "=" * 50)
                print(" REGISTRO DE PRODUCTO")
                print("=" * 50)
                codigo = input("Código de barras: ").strip()
                nombre = input("Nombre del producto: ").strip().title()
                categoria = input("Categoría: ").strip().title()
                precio = float(input("Precio unitario: $"))
                stock = int(input("Stock inicial: "))
                crearp = productoss.crear(codigo, nombre, categoria, precio, stock, usuario_actual['id'])
                if crearp:
                    print("\n✅ Producto registrado exitosamente!")
                else:
                    print("\n❌ Error al registrar producto")
                esperar_tecla()

            elif opcion == "3":  # Listar productos
                borrar_pantalla()
                print("\n" + "=" * 90)
                print(" INVENTARIO DE PRODUCTOS")
                print("=" * 90)
                print(f"{'Código':<15}{'Nombre':<20}{'Categoría':<15}{'Precio':>15}{'Stock':>10}")
                print("-" * 90)
                lista = productoss.listar()
                
                if lista:
                    for p in lista:
                        precio_fmt = formatear_precio(p['precio'])
                        print(f"{p['codigo']:<15}{p['nombre'][:18]:<20}{p['categoria']:<15}{precio_fmt:>15}{p['stock']:>10}")
                else:
                    print("No hay productos registrados")
                print("=" * 90)
                esperar_tecla()
                
            elif opcion == "4":  # Buscar producto
                borrar_pantalla()
                print("\n" + "=" * 50)
                print(" BUSCAR PRODUCTO")
                print("=" * 50)
                codigo = input("Ingrese código de barras: ").strip()
                producto = productoss.buscar(codigo)
                if producto:
                    print("\n" + "-" * 50)
                    print(f"Código: {producto['codigo']}")
                    print(f"Nombre: {producto['nombre']}")
                    print(f"Categoría: {producto['categoria']}")
                    print(f"Precio: {formatear_precio(producto['precio'])}")
                    print(f"Stock: {producto['stock']} unidades")
                else:
                    print("\n❌ Producto no encontrado")
                esperar_tecla()
            
            elif opcion == "5":  # Actualizar stock
                borrar_pantalla()
                print("\n" + "=" * 50)
                print(" ACTUALIZAR STOCK")
                print("=" * 50)
                codigo = input("Código de barras: ").strip()
                nuevo_stock = int(input("Nuevo stock: "))
                actualizar = productoss.actualizar_stock(codigo, nuevo_stock)
                if actualizar:
                    print("\n✅ Stock actualizado correctamente!")
                else:
                    print("\n❌ Error al actualizar stock")
                esperar_tecla()

            elif opcion == "6":  # Menú de administración de tablas
                while True:
                    opcion_admin = menu_admin()
                    
                    if opcion_admin == "1":
                        print("\nReiniciando tabla productos...")
                        ok = reiniciar_tabla("detalle_venta") and reiniciar_tabla("ventas") and reiniciar_tabla("productos")
                        print("\n✅ Tabla(s) reiniciada(s)" if ok else "\n❌ Error al reiniciar")
                        esperar_tecla()
                        
                    elif opcion_admin == "2":
                        print("\nReiniciando tabla ventas...")
                        ok = reiniciar_tabla("detalle_venta") and reiniciar_tabla("ventas")
                        print("\n✅ Tabla(s) reiniciada(s)" if ok else "\n❌ Error al reiniciar")
                        esperar_tecla()

                    elif opcion_admin == "3":
                        print("\nReiniciando tabla detalle_venta...")
                        ok = reiniciar_tabla("detalle_venta")
                        print("\n✅ Tabla reiniciada" if ok else "\n❌ Error al reiniciar")
                        esperar_tecla()
                        
                    elif opcion_admin == "4":
                        print("\nReiniciando tabla usuarios...")
                        ok = reiniciar_tabla("usuarios")
                        print("\n✅ Tabla reiniciada" if ok else "\n❌ Error al reiniciar")
                        esperar_tecla()

                    elif opcion_admin == "5":
                        borrar_pantalla()
                        print("\n" + "=" * 50)
                        print(" EXPORTAR DATOS")
                        print("=" * 50)
                        print("1. Exportar Usuarios")
                        print("2. Exportar Productos")
                        print("3. Exportar Ventas")
                        print("4. Exportar Detalle de Ventas")
                        print("5. Volver")
                        sub_op = input("\nSeleccione tabla a exportar: ")
                        mapas = {"1":"usuarios","2":"productos","3":"ventas","4":"detalle_venta"}
                        if sub_op == "5":
                            continue
                        tabla = mapas.get(sub_op)
                        if not tabla:
                            print("\n❌ Opción inválida"); esperar_tecla(); continue
                        print("\nFormato: 1=Excel  2=PDF")
                        fmt = input("Seleccione formato: ")
                        formatos = {"1":"excel","2":"pdf"}
                        from funciones import exportar_tabla
                        archivo = exportar_tabla(tabla, formatos.get(fmt))
                        if archivo:
                            print(f"\n✅ Exportado: {archivo}")
                        else:
                            print("\n❌ Error al exportar (¿tabla vacía?)")
                        esperar_tecla()

                    elif opcion_admin == "6":
                        break
                    else:
                        print("\n❌ Opción inválida"); esperar_tecla()
            
            elif opcion == "7":
                usuario_actual = None
                print("\nSesión cerrada correctamente")
                esperar_tecla()

            else:
                print("\n❌ Opción inválida")
                esperar_tecla()

if __name__ == "__main__":
    main()
