class Usuario:
    def __init__(self,correo,contra):
        self.correo = correo
        self.contra = contra

    def dump (self):
        return{
            "correo" : self.correo,
            "contra" : self.contra
        }