import customtkinter as Ctk
from CTkMessagebox import CTkMessagebox



Ctk.set_appearance_mode("dark")
Ctk.set_default_color_theme("dark-blue")

# Tamaño del programa
root = Ctk.CTk()
root.geometry("500x350")

root.title ("Login")

# Función de login
def login():
    username = entry1.get()
    password = entry2.get()
    if username == "admin" and password == "admin":
        CTkMessagebox(title="Inicio de sesión exitoso", message=f"Bienvenido, {username}!", icon="check")
    else:
        CTkMessagebox(title="Error", message="Nombre de usuario o contraseña incorrectos", icon="cancel")

# Marco principal
frame = Ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# Título
label = Ctk.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
label.pack(pady=12, padx=10)

# Barra de ingreso de datos
entry1 = Ctk.CTkEntry(master=frame, placeholder_text='Username')
entry1.pack(pady=12, padx=10)
entry2 = Ctk.CTkEntry(master=frame, placeholder_text='Password', show="*")
entry2.pack(pady=12, padx=10)

# Botón con texto
button = Ctk.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

# Botón con tilde
checkbox = Ctk.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)




root.mainloop()
