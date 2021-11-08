from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.exceptions import LengthRequired
from Registro import Registro

app = Flask(__name__)
CORS(app)
usuarios = []
admin=[]
publicaciones=[]
admin.append(Registro("admin","ebeee@gaa","admin","M","admin"))
usuarios.append(Registro("home","ebeee@gaa","123","M","home"))
usuarios.append(Registro("home","ebeee@gaa","123","M","home1"))
usuarios.append(Registro("home","ebeee@gaa","123","M","home2"))


#mostrar usuarios
@app.route('/Obtener', methods=['GET'])
def mostrar():
    global usuarios
    respuesta =[]
    for u in admin:
        respuesta.append(u.Mostrar())
        
    for u in usuarios:
        respuesta.append(u.Mostrar())

    return(jsonify(respuesta))
    
@app.route('/eliminar/<string:username>', methods=['DELETE'])
def Eliminar(username):
    global usuarios  
    verificacion=0
    for a in range(len(usuarios)):
        if  usuarios[a].Mostrar_usuario() == username:
            del usuarios[a]
            verificacion=1

    if verificacion==1:        
        return(jsonify({"mensaje" : "usuario eliminado"}))
    else:
        return(jsonify({"mensaje" : "usuario no encontrado"}))     

@app.route('/modificar/<string:username>', methods=['PUT'])
def Modificar(username):
    global usuarios
    for u in usuarios:
        if u.Mostrar_usuario() == username:
            nombre=request.json["nombre"]
            contrasenia=request.json["password"]
            correo=request.json["email"]
            genero=request.json["genero"]
            usrname=request.json["username"]
            u.Modificar(nombre,contrasenia,correo,genero,usrname)

    return(jsonify({"mensaje" : "usuario modificado"}))       

@app.route('/iniciar/', methods=['POST'])
def Iniciar():
    global usuarios
    verificacion=0
    username=request.json["username"]
    password=request.json["password"]
    for u in admin:
        if (u.Mostrar_pas()== password and u.Mostrar_usuario()==username):
            verificacion=3

    for u in usuarios:
        if (u.Mostrar_pas()== password and u.Mostrar_usuario()==username):
            verificacion=1
        else:
            verifiacion=2
            
    if verificacion==1:
        return(jsonify({'message' : "022"})) 
    elif verificacion==2:
        return(jsonify({'message': "023"}))
    elif verificacion==3:
        return(jsonify({'message': "024"}))         

@app.route('/registrar/', methods=['POST'])
def Registrar():
    global usuarios
    verificacion=0
    nombre=request.json["nombre"]
    contrasenia=request.json["passwordn"]
    correo=request.json["email"]
    genero=request.json["genero"]
    usname=request.json["usernamen"]
    for u in usuarios:
        if u.Mostrar_usuario()==usname:
            verificacion=1
            
        else:
            verificacion=2
             
    if verificacion==1:
        return(jsonify({'message' : "020"})) 

    elif verificacion==2:
        usuarios.append(Registro(nombre,correo,contrasenia,genero,usname))
        return(jsonify({"message" : "025"}))  

    

if __name__=="__main__":
    app.run(threaded=True, debug=True, port=5000)

