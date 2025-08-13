from conexionBD import conectar
import hashlib

def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar_usuario(nombre, apellido, email, contrasena):
    conn = conectar()
    if not conn: 
        return None
    try:
        cur = conn.cursor()
        sql = "INSERT INTO usuarios (nombre, apellidos, email, password) VALUES (%s, %s, %s, %s)"
        cur.execute(sql, (nombre, apellido, email, hash_password(contrasena)))
        conn.commit()
        return cur.lastrowid
    except Exception as e:
        print(f"[Usuarios] Error al registrar: {e}")
        conn.rollback()
        return None
    finally:
        cur.close(); conn.close()

def autenticar_usuario(email, contrasena):
    conn = conectar()
    if not conn:
        return None
    try:
        cur = conn.cursor(dictionary=True)
        sql = "SELECT id, nombre, apellidos FROM usuarios WHERE email=%s AND password=%s"
        cur.execute(sql, (email, hash_password(contrasena)))
        return cur.fetchone()
    except Exception as e:
        print(f"[Usuarios] Error al autenticar: {e}")
        return None
    finally:
        cur.close(); conn.close()
