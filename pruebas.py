from Registro import Registro
usuarios = []
usuarios.append(Registro("carlos","casd@gasde.com","asdae","M","veaaaas"))
def prueba():
    global usuarios
    for u in usuarios:
        print(u.dump())
    