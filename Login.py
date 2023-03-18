def login():
    # Pide al usuario que introduzca su nombre de usuario y contraseña
    username = input("Introduce tu nombre de usuario: ")
    password = input("Introduce tu contraseña: ")

    # Aquí podrías hacer una consulta a una base de datos o leer un archivo con los datos de usuario y contraseña
    # En este ejemplo, simplemente se usan valores predefinidos para hacer la comprobación
    if username == "usuario" and password == "contraseña":
        print("Inicio de sesión exitoso")
        return True
    else:
        print("Nombre de usuario o contraseña incorrectos")
        return False




