class Registro:
    def __init__(self, nombre,correo,contrasenia,genero,usname):
        self.correo = correo
        self.contrasenia = contrasenia
        self.nombre = nombre
        self.genero = genero
        self.usname = usname

    def Mostrar (self):
        return{
            "correo" : self.correo,
            "contrasenia" : self.contrasenia,
            "nombre": self.nombre,
            "genero" : self.genero,
            "Usname" : self.usname
        }    

    def Mostrar_usuario(self):
        return(self.usname)

    def ModificarDatosUsuario(self, nombre,correo,contrasenia,genero,usname):
        self.correo = correo
        self.contrasenia = contrasenia
        self.nombre = nombre
        self.genero = genero
        self.usname = usname

    def Mostrar_pas(self):
        return(self.contrasenia)    

