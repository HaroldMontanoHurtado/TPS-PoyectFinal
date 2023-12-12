from customtkinter import *
from tkinter import simpledialog, ttk
from tkcalendar import DateEntry, Calendar
from CTkMessagebox import CTkMessagebox
from db.consultas_db import *
# Pero cuando ejecuto gui.py, me ejecuta las funciones en consultas_db.py sin problemas
ventana_act=0
proyecto_act=''

class Window(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # variables creadas para centrar la ventana al iniciar el programa
        self.wtotal = self.winfo_screenwidth()
        self.htotal = self.winfo_screenheight()
        self.wventana = 1120
        self.hventana = 630
        self.pwidth = round(self.wtotal/2-self.wventana/2)
        self.pheight = round(self.htotal/2-self.hventana/2)
        self.geometry(
            str(self.wventana)+"x"+str(self.hventana)+
            "+"+str(self.pwidth)+"+"+str(self.pheight-50))
        self.title('Sistema de gestion de pruebas de software')
        self.resizable(0,0)
        ####### componentes agregados #######
        global ventana_act
        if ventana_act==1:
            self.states_frame()
        elif ventana_act==2:
            self.poly_frame()
            self.test_items_exclusive()
        elif ventana_act==3:
            self.poly_frame()
            self.gestor_items_error()
        else:
            self.home_frame()

    ##### HOME FRAME #####

    def home_frame(self):
        self.home_optionMenus()
        self.home_labels()
        self.home_buttons()

    def home_buttons(self):
        # Se crean como globas para hacer alternar el estado del boton
        bt_create_proj = CTkButton(
            master=self, text="Crear\nProtecto", command=self.crear_proyecto,
            width=250, height=120, font=('Calisto MT', 30))
        bt_create_proj.place(x=290, y=260)

        bt_bt_manage = CTkButton(
            master=self, text="Gestionar\nProyecto", command=self.cambia_a_StateFrame,
            width=250, height=120, font=('Calisto MT', 30))
        bt_bt_manage.place(x=580, y=260)

    def home_labels(self):
        label = CTkLabel(
            master=self, text="Sistema de Gestión\nde Pruebas de Software", fg_color="transparent",
            #width=80, height=30, 
            font=('Calisto MT', 50))
        label.place(x=320,y=100)

    def home_optionMenus(self):
        proyectos = aplanar_lst(custom_consulta("""Select nombre from proyectos"""))
        
        optionmenu = CTkOptionMenu(
            master=self, values=proyectos, #command=optionmenu_callback,
            width=540, height=60, font=('Calisto MT', 30))
        optionmenu.set("\tSeleccionar Proyectos")
        optionmenu.place(x=290, y=420)

    ##### STATES FRAME #####
    def states_frame(self):
        self.states_buttons()
        self.states_labels()
        self.states_optionMenus()
        self.states_table()

    def states_labels(self):
        label = CTkLabel(
            master=self, text="Estados de Pruebas", fg_color="transparent",
            font=('Calisto MT', 50))
        label.place(x=390,y=10)

    def states_buttons(self):
        # Se crean como globas para hacer alternar el estado del boton
        bt_agregar = CTkButton(
            master=self, text="Agregar", command=self.cambia_a_TestFrame,
            width=240, height=80, font=('Calisto MT', 30))
        bt_agregar.place(x=40, y=90)

        bt_editar = CTkButton(
            master=self, text="Editar", command=self.cambia_a_GestorFrame,
            width=240, height=80, #border_width=0, state='normal',
            font=('Calisto MT', 30))
        bt_editar.place(x=300, y=90)

        bt_regresar = CTkButton(
            master=self, text="Volver al Menú", command=self.cambia_a_home,
            width=240, height=80, font=('Calisto MT', 30))
        bt_regresar.place(x=840, y=90)

    def states_optionMenus(self):
        
        optionmenu = CTkOptionMenu(
            master=self, values=[
                "Gestionar Usuarios", "Casos de Pruebas", "Gestionar Errores"], 
            #command=optionmenu_callback,
            command=self.probando123,
            width=260, height=80, font=('Calisto MT', 30))
        optionmenu.set("Opcion a\ngestionar")
        optionmenu.place(x=560, y=90)

    def states_table(self):
        table = ttk.Treeview(
            master=self, columns=('estado','prioridad','designado','prueba'), show='headings')
        table.heading('estado', text='Estado')
        table.heading('prioridad', text='Prioridad')
        table.heading('designado', text='Designado a')
        table.heading('prueba', text='Titulo de prueba')
        table.place(x=40,y=190,width=1040,height=400)
        # example
        table.insert(parent='',index=0,values=('En curso','Alta','Harold','Prueba de aceptación'))
        table.insert(parent='',index=0,values=('Detenido','Baja','Ana','Prueba de usabilidad'))
        table.insert(parent='',index=0,values=('Listo','Mediana','Juan','Prueba unitaria'))
        table.bind('<<TreeviewSelect>>', lambda event: print(table.selection()))

    ##### POLY FRAME #####
    
    def poly_frame(self):
        self.tests_buttons()
        self.tests_labels()
        self.tests_optionMenus()
        self.tests_entries()

    def tests_buttons(self):
        
        bt_volver = CTkButton(
            master=self, text="Volver", command=self.cambia_a_StateFrame,
            width=240, height=80, border_width=0, state='normal',
            font=('Calisto MT', 30))
        bt_volver.place(x=60, y=60)

        bt_inicio = CTkButton(
            master=self, text="Volver al Menú", command=self.cambia_a_home,
            width=240, height=80, border_width=0, state='normal',
            font=('Calisto MT', 30))
        bt_inicio.place(x=820, y=60)

    def tests_labels(self):
        
        titulo = CTkLabel(
            master=self, text="Titulo", fg_color="transparent",
            font=('Calisto MT', 30), width=200, height=70)
        titulo.place(x=50, y=180)
        
        descripcion = CTkLabel(
            master=self, text="Descripción", fg_color="transparent",
            font=('Calisto MT', 30), width=200, height=70)
        descripcion.place(x=10, y=280)

    def tests_optionMenus(self):
        
        test_state = CTkOptionMenu(
            master=self, values=["tipo1", "tipo2", "tipo3"], #command=optionmenu_callback,
            width=400, height=70, font=('Calisto MT', 30))
        test_state.set("Estado")
        test_state.place(x=660, y=280)
        
        test_asignar = CTkOptionMenu(
            master=self, values=["tipo1", "tipo2", "tipo3"], #command=optionmenu_callback,
            width=400, height=70, font=('Calisto MT', 30))
        test_asignar.set("Asignar a")
        test_asignar.place(x=660, y=380)

    def tests_entries(self):
        titulo = CTkEntry(
            master=self, textvariable='',
            width=420, height=70,
            font=('Calisto MT', 25))
        titulo.place(x=200, y=180)
        
        descripcion = CTkEntry(
            master=self, textvariable='',
            width=420, height=270,
            font=('Calisto MT', 25))
        descripcion.place(x=200, y=280)

    def test_items_exclusive(self):
        label = CTkLabel(
            master=self, text="Diseñar Pruebas", fg_color="transparent",
            font=('Calisto MT', 50))
        label.place(x=390,y=70)
        
        test_priority = CTkOptionMenu(
            master=self, values=["Baja", "Media", "Alta"], #command=optionmenu_callback,
            width=400, height=70, font=('Calisto MT', 30))
        test_priority.set("Seleccionar prioridad")
        test_priority.place(x=660, y=180)
        
        def obtener_fecha():
            print(cal.get_date())
        
        bt_fecha = CTkButton(
            master=self, text="Elegir fecha", command=obtener_fecha,
            width=280, height=80, border_width=0, state='normal',
            font=('Calisto MT', 30))
        bt_fecha.place(x=660, y=480)
        
        cal = DateEntry(self)
        cal.place(x=960, y=500)

    def gestor_items_error(self):
        label = CTkLabel(
            master=self, text="Gestión de Errores", fg_color="transparent",
            font=('Calisto MT', 50))
        label.place(x=360,y=70)
        
        gestor_severity = CTkOptionMenu(
            master=self, values=["Baja", "Media", "Alta", "Crítica"], #command=optionmenu_callback,
            width=400, height=70, font=('Calisto MT', 30))
        gestor_severity.set("Seleccionar severidad")
        gestor_severity.place(x=660, y=180)
        
        gestor_prueba = CTkOptionMenu(
            master=self, values=["Unitaria", "Integración", "Rendimiento"], #command=optionmenu_callback,
            width=400, height=70, font=('Calisto MT', 30))
        gestor_prueba.set("Caso de prueba")
        gestor_prueba.place(x=660, y=480)

    ###### FUNCTIONS ######
    def cambia_a_home(self):
        global ventana_act
        ventana_act=0
        self.destroy()
        iniit()

    def cambia_a_StateFrame(self):
        global ventana_act
        ventana_act=1
        print(f'ahora es: {ventana_act}')
        self.destroy()
        iniit()

    def cambia_a_TestFrame(self):
        global ventana_act
        ventana_act=2
        self.destroy()
        iniit()

    def cambia_a_GestorFrame(self):
        global ventana_act
        ventana_act=3
        self.destroy()
        iniit()

    def crear_proyecto(self):
        proyecto=[]
        respuesta = simpledialog.askstring(' ', "Ingresa el nombre del proyecto:")
        proyecto.append(respuesta)
        
        agregar('P', proyecto)


    def probando123(self):
        print('Llamado de prueba')

def iniit():
    if __name__=="__main__":
        window = Window()
        window.mainloop()

iniit()

