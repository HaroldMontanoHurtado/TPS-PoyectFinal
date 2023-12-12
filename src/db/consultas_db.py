from .connection import conectarBD
from tkinter import messagebox
# Si intento ejecutar consultas_db.py, me sale error
'''
|     0      |    1      |    2      |    3      |     4      |     5      |    6      |
|     id     |   nombre  | f_inicio  |   f_fin   |   serial   | ### proyectos ###
|     id     |   nombre  |    rol    |  serial   | ### usuarios ###
|     id     |   nombre  |descripcion| prioridad |   estado   |fecha_limite|id_asignado| ### pruebas ###
|     id     |   nombre  |descripcion| severidad |   estado   |id_asignado | id_prueba | ### errores ###
'''

def select_row(id, tabla):
    conexion = conectarBD()
    
    listar_fila = []
    query = f"""SELECT * FROM public.{tabla} WHERE id=\'{id}\'"""
    try:
        conexion.cursor.execute(query)
        listar_fila = conexion.cursor.fetchall()
        conexion.cerrar()
    except Exception as ex:
        messagebox.showerror('ERROR EN LA CONSULTA', f'{ex}.')

    return listar_fila

def select_table(tabla):
    conexion = conectarBD()
    
    listar_tabla = []
    query = f"""SELECT * FROM public.{tabla}"""
    try:
        conexion.cursor.execute(query)
        listar_tabla = conexion.cursor.fetchall()
        conexion.cerrar()
    except Exception as ex:
        messagebox.showerror('ERROR EN LA CONSULTA', f'{ex}.')

    return listar_tabla

def custom_consulta(query):
    conexion = conectarBD()
    
    listar_fila = []
    
    try:
        conexion.cursor.execute(query)
        listar_fila = conexion.cursor.fetchall()
        conexion.cerrar()
    except Exception as ex:
        messagebox.showerror('ERROR EN LA CONSULTA', f'{ex}.')

    return listar_fila

def agregar(tabla, objeto):
    conexion = conectarBD()
    quary=''
    
    if not(None in objeto) and not('' in objeto):
        print(type(objeto[0]), objeto[0])
        if tabla == 'P':
            quary = f"""
            INSERT INTO public.proyectos(id, nombre, f_inicio)
            VALUES (1, '{objeto[0]}', (CURRENT_DATE));
            UPDATE public.proyectos SET id = 'P' || LPAD(serial::text, 5, '0');
            """
        elif tabla == 'U':
            quary = f"""
            INSERT INTO public.usuarios(id, nombre, rol)
            VALUES (1, '{objeto[0]}', '{objeto[1]}');
            UPDATE public.usuarios SET id = 'U' || LPAD(serial::text, 5, '0');
            """
        elif tabla == 'C':
            quary = f"""
            INSERT INTO public.pruebas(
            id, nombre, descripcion, prioridad, estado, fecha_limite, id_asignado)
            VALUES (1, '{objeto[0]}', '{objeto[1]}', '{objeto[2]}', '{objeto[3]}', '{objeto[4]}', '{objeto[5]}');
            UPDATE public.pruebas SET id = 'C' || LPAD(serial::text, 5, '0');
            """
        elif tabla == 'E':
            quary = f"""
            INSERT INTO public.errores(
            id, nombre, descripcion, severidad, estado, id_asignado, id_prueba)
            VALUES (1, '{objeto[0]}', '{objeto[1]}', '{objeto[2]}',
            '{objeto[3]}', '{objeto[4]}', '{objeto[5]}', '{objeto[6]}');
            UPDATE public.errores SET id = 'E' || LPAD(serial::text, 5, '0');
            """
        elif tabla == 'A':
            quary = f"""
            INSERT INTO public.asignados(id, id_proy, id_user)
            VALUES (1, '{objeto[0]}', '{objeto[1]}');
            UPDATE public.asignados SET id = 'A' || LPAD(serial::text, 5, '0');
            """
    
    try:
        conexion.cursor.execute(quary)
        conexion.cerrar()
        print('ejecutó agregar()')
    except Exception as ex:
        titulo = 'ERROR EN AGREGAR'
        mensaje = f'{ex}.'
        messagebox.showerror(titulo, mensaje)  

def editar(tabla, id, cambios):
    conexion = conectarBD()
    
    if tabla=='proyectos':
        quary = f"""
        UPDATE public.proyectos
        SET nombre='{cambios[0]}' WHERE id='{id}';
        """
    elif tabla=='usuarios':
        quary = f"""
        UPDATE public.usuarios
        SET nombre='{cambios[0]}', rol='{cambios[1]}' WHERE id='{id}';
        """
    elif tabla=='pruebas':
        quary = f"""
        UPDATE public.pruebas
        SET nombre='{cambios[0]}', descripcion='{cambios[1]}', prioridad='{cambios[2]}',
        estado='{cambios[3]}', fecha_limite='{cambios[4]}', id_asignado='{cambios[5]}'
        WHERE id='{id}';
        """
    elif tabla=='errores':
        quary = f"""
        UPDATE public.errores
        SET nombre='{cambios[0]}', descripcion='{cambios[1]}', severidad='{cambios[2]}',
        estado='{cambios[3]}', id_asignado='{cambios[4]}', id_prueba='{cambios[5]}'
        WHERE id='{id}';
        """
    
    try:
        conexion.cursor.execute(quary)
        conexion.cerrar()
    except Exception as ex:
        titulo = 'ERROR AL EDITAR'
        mensaje = f'{ex}.'
        messagebox.showerror(titulo,mensaje)

def contar_total_tabla(tabla):
    conexion = conectarBD()
    
    tamaño_tabla = []
    quary = f"""SELECT count(*) FROM public.{tabla}"""
    
    try:
        conexion.cursor.execute(quary)
        tamaño_tabla = conexion.cursor.fetchall()
        conexion.cerrar()
    except Exception as ex:
        messagebox.showerror('ERROR EN CONTEO', f'{ex}.')
    
    return tamaño_tabla[0][0]

def aplanar_lst(lista):
    return [elemento for sublista in lista for elemento in sublista]

