import tkinter as tk  
from tkinter import messagebox  

class AgendaPersonal:  
    def __init__(self, root):  
        self.root = root  
        self.root.title("Agenda Personal")  
        
        self.initial_frame = tk.Frame(self.root )  
        self.initial_frame.pack(fill=tk.BOTH, expand=True)  
        
        self.create_initial_widgets()  
        
        self.contactos = []  

    def create_initial_widgets(self):  
        label = tk.Label(self.initial_frame, text="¿Desea iniciar o salir del programa?",   
                         font=("BODONI MT Black", 14) )  
        label.pack(pady=120, padx=70)  

        start_button = tk.Button(self.initial_frame, text="Inicializar", command=self.open_main_window,   
                                 font=("Castellar", 14),  fg="black")  
        start_button.pack(side=tk.LEFT, pady=20, padx=70)  

        exit_button = tk.Button(self.initial_frame, text="Salir", command=self.root.quit,   
                                font=("Castellar", 14), fg="black")  
        exit_button.pack(side=tk.LEFT, pady=20, padx=30)  

    def open_main_window(self):  
        """Abre la ventana principal de la agenda."""  
        self.initial_frame.pack_forget()  
        
        self.main_frame = tk.Frame(self.root)  
        self.main_frame.pack(pady=20)  
        
        label_nombre = tk.Label(self.main_frame, text="Nombre:")  
        label_nombre.pack(padx=10, pady=5)  
        self.entrada_nombre = tk.Entry(self.main_frame, width=50)  
        self.entrada_nombre.pack(padx=10, pady=5)  

        label_telefono = tk.Label(self.main_frame, text="Teléfono:")  
        label_telefono.pack(padx=10, pady=5)  
        self.entrada_telefono = tk.Entry(self.main_frame, width=50)  
        self.entrada_telefono.pack(padx=10, pady=5)  

       
        boton_agregar = tk.Button(self.main_frame, text="Agregar Contacto", command=self.agregar_contacto)  
        boton_agregar.pack(pady=10)  

        boton_buscar = tk.Button(self.main_frame, text="Buscar Contacto", command=self.buscar_contacto)  
        boton_buscar.pack(pady=10)  

        boton_editar = tk.Button(self.main_frame, text="Editar Contacto", command=self.editar_contacto)  
        boton_editar.pack(pady=10)  

        boton_eliminar = tk.Button(self.main_frame, text="Eliminar Contacto", command=self.eliminar_contacto)  
        boton_eliminar.pack(pady=10)  

    def agregar_contacto(self):  
        nombre = self.entrada_nombre.get()  
        telefono = self.entrada_telefono.get()  
        
        if nombre and telefono:  
            self.contactos.append({'nombre': nombre, 'telefono': telefono})  
            self.entrada_nombre.delete(0, tk.END)  
            self.entrada_telefono.delete(0, tk.END)  
            messagebox.showinfo("Éxito", "Contacto agregado correctamente.")  
        else:  
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")  

    def buscar_contacto(self):  
        nombre = self.entrada_nombre.get()  
        encontrado = False  
        
        for contacto in self.contactos:  
            if contacto['nombre'].lower() == nombre.lower():  
                self.entrada_telefono.delete(0, tk.END)  
                self.entrada_telefono.insert(0, contacto['telefono'])  
                encontrado = True  
                break  
        
        if not encontrado:  
            messagebox.showwarning("No encontrado", "Contacto no encontrado.")  

    def editar_contacto(self):  
        nombre = self.entrada_nombre.get()  
        telefono = self.entrada_telefono.get()  
        encontrado = False  
        
        for contacto in self.contactos:  
            if contacto['nombre'].lower() == nombre.lower():  
                contacto['telefono'] = telefono  
                messagebox.showinfo("Éxito", "Contacto editado correctamente.")  
                encontrado = True  
                break  
        
        if not encontrado:  
            messagebox.showwarning("No encontrado", "Contacto no encontrado.")  

    def eliminar_contacto(self):  
        nombre = self.entrada_nombre.get()  
        encontrado = False  
        
        for contacto in self.contactos:  
            if contacto['nombre'].lower() == nombre.lower():  
                self.contactos.remove(contacto)  
                self.entrada_telefono.delete(0, tk.END)  
                messagebox.showinfo("Éxito", "Contacto eliminado correctamente.")  
                encontrado = True  
                break  
        
        if not encontrado:  
            messagebox.showwarning("No encontrado", "Contacto no encontrado.")  

if __name__ == "__main__":  
    root = tk.Tk()  
    app = AgendaPersonal(root)  
    root.mainloop() 
