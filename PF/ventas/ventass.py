from conexionBD import conectar

def registrar_venta(usuario_id, productos_vendidos):
    conn = conectar()
    if not conn: return False
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO ventas (fecha, total, usuario_id) VALUES (NOW(), 0, %s)", (usuario_id,))
        venta_id = cur.lastrowid
        total = 0
        for item in productos_vendidos:
            cur.execute("""                INSERT INTO detalle_venta (venta_id, producto_id, cantidad, precio_unitario)
                VALUES (%s, %s, %s, %s)
            """, (venta_id, item['id'], item['cantidad'], item['precio']))
            cur.execute("UPDATE productos SET stock = stock - %s WHERE id=%s", (item['cantidad'], item['id']))
            total += item['cantidad'] * item['precio']
        cur.execute("UPDATE ventas SET total=%s WHERE id=%s", (total, venta_id))
        conn.commit()
        return True
    except Exception as e:
        print(f"[Ventas] Error al registrar: {e}")
        conn.rollback()
        return False
    finally:
        cur.close(); conn.close()
