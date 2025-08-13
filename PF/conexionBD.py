import mysql.connector

def conectar():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cooppel"
        )
        return conn
    except Exception as e:
        print(f"[BD] Error de conexión: {e}")
        return None

def reiniciar_tabla(nombre_tabla: str) -> bool:
    conn = conectar()
    if not conn:
        return False
    try:
        cur = conn.cursor()
        cur.execute("SET FOREIGN_KEY_CHECKS=0;")
        cur.execute(f"TRUNCATE TABLE {nombre_tabla};")
        cur.execute("SET FOREIGN_KEY_CHECKS=1;")
        conn.commit()
        return True
    except Exception as e:
        print(f"[BD] Error al reiniciar {nombre_tabla}: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()
