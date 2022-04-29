class Usuario:
    def __init__(self, nombre, permiso) -> None:
        self.nombre = nombre
        self.permiso = permiso


nombreUsuario = input("Ingrese el nombre del usuario")
permisoUsuario = input("Ingrese el nivel de Permiso")

nuevoUsuario = Usuario(nombreUsuario, permisoUsuario)

if nuevoUsuario.permiso == "3":
    print("3: Agregar Vehiculo")