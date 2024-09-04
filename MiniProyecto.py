import tkinter as tk  
from tkinter import messagebox  

class AgendaPersonal:  
    def __init__(self, root):  
        self.root = root  
        self.root.title("Agenda Personal")  
        self.root.geometry("400x400")  
        self.root.config(bg="#87CEEB")  

        self.initial_frame = tk.Frame(self.root, bg="#87CEEB")  
        self.initial_frame.pack(fill=tk.BOTH, expand=True)  

        self.create_initial_widget()  

        self.contactos = []  

    def create_initial_widget(self):  
        label = tk.Label(self.initial_frame, text="¿Desea iniciar o salir del programa?",  
                         font=("Arial", 14, "bold"), bg="#87CEEB", fg="#333")  
        label.pack(pady=30)  

        button_frame = tk.Frame(self.initial_frame, bg="#87CEEB")  
        button_frame.pack(pady=20)  

        start_button = tk.Button(button_frame, text="Inicializar", command=self.open_main_window,  
                                 font=("Arial", 14), fg="#fff", bg="#007BFF", relief="raised")  
        start_button.pack(side=tk.LEFT, padx=20, pady=10)  

        exit_button = tk.Button(button_frame, text="Salir", command=self.root.quit,  
                                font=("Arial", 14), fg="#fff", bg="#0056b3", relief="raised")  
        exit_button.pack(side=tk.LEFT, padx=20, pady=10)  

    def open_main_window(self):  
        self.initial_frame.pack_forget()  

    
        self.main_frame = tk.Frame(self.root, bg="#FFA500", width=300, height=300)  
        self.main_frame.pack(pady=20, padx=20)  
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')  

        label_nombre = tk.Label(self.main_frame, text="Nombre:", font=("Arial", 12), bg="#ffffff", fg="#333")  
        label_nombre.pack(padx=10, pady=5)  

        self.entrada_nombre = tk.Entry(self.main_frame, width=30, font=("Arial", 12), bg="#f0f0f0", fg="#333")  
        self.entrada_nombre.pack(padx=10, pady=5)  

        label_telefono = tk.Label(self.main_frame, text="Teléfono:", font=("Arial", 12), bg="#ffffff", fg="#333")  
        label_telefono.pack(padx=10, pady=5)  

        self.entrada_telefono = tk.Entry(self.main_frame, width=30, font=("Arial", 12), bg="#f0f0f0", fg="#333")  
        self.entrada_telefono.pack(padx=10, pady=5)  

        boton_agregar = tk.Button(self.main_frame, text="Agregar Contacto", command=self.agregar_contacto,  
                                   font=("Arial", 12), fg="#fff", bg="#28a745", relief="raised")  
        boton_agregar.pack(pady=10)  

        boton_buscar = tk.Button(self.main_frame, text="Buscar Contacto", command=self.buscar_contacto,  
                                 font=("Arial", 12), fg="#fff", bg="#17a2b8", relief="raised")  
        boton_buscar.pack(pady=10)  

        boton_editar = tk.Button(self.main_frame, text="Editar Contacto", command=self.editar_contacto,  
                                 font=("Arial", 12), fg="#fff", bg="#007BFF", relief="raised")  
        boton_editar.pack(pady=10)  

        boton_eliminar = tk.Button(self.main_frame, text="Eliminar Contacto", command=self.eliminar_contacto,  
                                   font=("Arial", 12), fg="#fff", bg="#0056b3", relief="raised")  
        boton_eliminar.pack(pady=10)  

        for button in [boton_agregar, boton_buscar, boton_editar, boton_eliminar]:  
            button.bind("<Enter>", lambda e: button.config(bg="#0056b3"))    
            button.bind("<Leave>", lambda e: button.config(bg="#28a745" if button == boton_agregar else "#17a2b8" if button == boton_buscar else "#007BFF" if button == boton_editar else "#0056b3"))  

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
                encontrado = True  
                messagebox.showinfo("Éxito", "Contacto editado correctamente.")  
                break  
        if not encontrado:  
            messagebox.showwarning("No encontrado", "Contacto no encontrado.")  

    def eliminar_contacto(self):  
        nombre = self.entrada_nombre.get()  
        encontrado = False  
        for i, contacto in enumerate(self.contactos):  
            if contacto['nombre'].lower() == nombre.lower():  
                del self.contactos[i]  
                encontrado = True  
                messagebox.showinfo("Éxito", "Contacto eliminado correctamente.")  
                break  
        if not encontrado:  
            messagebox.showwarning("No encontrado", "Contacto no encontrado.")  

if __name__ == "__main__":  
    root = tk.Tk()  
    app = AgendaPersonal(root)  
    root.mainloop()
               
           
