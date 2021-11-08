from flask import Flask, jsonify, request, json
from flask_cors import CORS
from werkzeug.exceptions import LengthRequired
from Registro import Registro

app = Flask(__name__)
CORS(app)
usuarios = []
admin=[]
publicaciones=[]
admin.append(Registro("Darwin Arevalo","admin@ipc1.com","admin","M","admin@ipc1"))
usuarios.append(Registro("home-1","eee@gaa","123contrasenia","f","home"))
usuarios.append(Registro("home-2","be@gaa.com","12carreraa","M","home1"))
usuarios.append(Registro("home-3","ebe@gaa.com","123322nuevo","f","home2"))


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

@app.route('/Obtener/<string:username>', methods=['GET'])
def obtenerUsuario(username):
    global usuarios
    respuesta =[]
    for u in admin:
        if(u.Mostrar_usuario() == username):
            respuesta.append(u.Mostrar())
            break
    for u in usuarios:
        if(u.Mostrar_usuario() == username):
            respuesta.append(u.Mostrar())
            break

    return(jsonify(respuesta))
    
@app.route('/eliminar/<string:username>', methods=['DELETE'])
def Eliminar(username):
    global usuarios  
    verificacion=0
    for a in range(len(usuarios)):
        
        if  usuarios[a].Mostrar_usuario() == username:
            del usuarios[a]
            verificacion=1
            break

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
            for i in usuarios:
                if i.Mostrar_usuario()==usrname:
                    return(jsonify({"mensaje" : "usuario ya registrado con ese username"}))

            u.ModificarDatosUsuario(nombre,correo,contrasenia,genero,usrname)
            return(jsonify({"mensaje" : "usuario modificado"}))
            

    return(jsonify({"mensaje" : "usuario no modificado"}))


@app.route('/iniciar/', methods=['POST'])
def Iniciar():
    global usuarios

    username=request.json["username"]
    password=request.json["password"]
    for u in admin:
        if (u.Mostrar_pas()== password and u.Mostrar_usuario()==username):
            return(jsonify({'message': "024"}))  

    for u in usuarios:
        if (u.Mostrar_pas()== password and u.Mostrar_usuario()==username):
            return(jsonify({'message' : "022"}))

    return(jsonify({'message': "023"}))
               

@app.route('/registrar/', methods=['POST'])
def Registrar():
    global usuarios
    cont=0
    num="1234567890"
    nombre=request.json["nombre"]
    contrasenia=request.json["passwordn"]
    correo=request.json["email"]
    genero=request.json["genero"]
    usname=request.json["usernamen"]
    if len(contrasenia)<8:
        return(jsonify({'message' : "02"}))    
    for caracter in contrasenia:
        for caracter1 in num:
            if caracter==caracter1:
                cont=+1
    if cont==0:
             return(jsonify({'message' : "01"}))  

    for u in usuarios:
        if u.Mostrar_usuario()==usname:
            return(jsonify({'message' : "020"})) 
            
    usuarios.append(Registro(nombre,correo,contrasenia,genero,usname))
    return(jsonify({"message" : "025"}))  

@app.route('/load-users',methods=['POST'] )
def LoadUsers():
    if request.method=='POST':
        params=json.load(request.files['document'])

        for usuarios in params:
            print(usuarios['name'])

        return (jsonify({"status" : "200"}))    

if __name__=="__main__":
    app.run(threaded=True, debug=True, port=5000)

