import fastapi
import re
from app.api.utils.oauth import AuthHandler
from passlib.context import CryptContext
from fastapi.encoders import jsonable_encoder
from app.api.schemas.usuarios_procesos import usuarios_procesossEntity, usuarios_procesosEntity
from app.api.models.usuarios_procesos import Usuario
from app.api.config.db import conn
from app.api.utils.acces_security import get_current_username
from fastapi import APIRouter, Depends, HTTPException, Request, Response
from bson import ObjectId
from app.api.utils.jsonreturn import *
        
usuarios_procesos = APIRouter()
auth_handler = AuthHandler()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#Metodos
def post(object,db):
    try:
        object = object.dict()
        object_id  = db.insert_one(object).inserted_id
        object = db.find_one({'_id':object_id})
        object = dict(object)
        object['_id'] = str(object['_id'])
        data_object['message'] = object
        return data_object
    except Exception as e:  
        error['message'] = str(e)
        return error

def get(key,db,id):
    try:
        if(key=='_id'):
            object = db.find_one({f'{key}':ObjectId(id)})
        else:
            object = db.find_one({f'{key}':id})
        if(object!=None):
            object = dict(object)
            object['_id'] = str(object['_id'])
            data_object['message'] = object
            return data_object
        data_object_does_not_exist['message'] = 'the object does not exist'
        return data_object_does_not_exist
    except Exception as e:
        error['message'] = str(e)
        return error

def put(key,db,id,data):
    try:
        if(key=='_id'):
            object = db.find_one({f'{key}':ObjectId(id)})
        else:
            object = db.find_one({f'{key}':id})
        if(object!=None):
            data = dict(data)
            print(object)
            if(key=='_id'):
                db.update_one({f'{key}':ObjectId(id)},{'$set':data})
                object = db.find_one({f'{key}':ObjectId(id)})
            else:
                db.update_one({f'{key}':id},{'$set':data})
                object = db.find_one({f'{key}':id})        
            object['_id'] = str(object['_id'])
            data_object['message'] = object 
            return data_object
        data_object_does_not_exist['message'] = 'Object does not exist'
        return data_object_does_not_exist
    except Exception as e:
        error['message'] = str(e)
        return error

def delete(key,db,id):
    try:
        if(key=='_id'):
            object = db.find_one({f'{key}':ObjectId(id)})
        else:
            object = db.find_one({f'{key}':id})
        if(object!=None):
            if(key=='_id'):
                db.delete_one({f'{key}':ObjectId(id)})
            else:
                db.delete_one({f'{key}':id})
            data_object['message'] = 'The Object was deleted'
            return data_object
        data_object_does_not_exist['message'] = 'Object does not exist'
        return data_object_does_not_exist
    except Exception as e:
        error['message'] = str(e)
        return error

@usuarios_procesos.post('/post/', tags=['CRUD'])
def post_usuarios_procesos(usuario:Usuario):
    response = None

    try:
        if re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,12}$', usuario.password):
            existing_user = conn.rappidron.usuarios.find_one({"user": usuario.user})

            if not existing_user:
                user_dict = jsonable_encoder(usuario)
                user_dict['password'] = pwd_context.hash(user_dict['password'])

                result = conn.rappidron.usuarios.insert_one(user_dict)

                response = post(usuario, conn.rappidron.usuarios)
            else:
                error['message'] = "The user is already registered"

                response = error
        else:
            error['message'] = "The password must be 6 to 12 characters long and must have at least one uppercase letter and one number"

            response = error
    except Exception as e:
        error['message'] = str(e)

        response = error
    
    return response

@usuarios_procesos.get('/read/{usuario_id}/', tags=['CRUD'])
def get_usuarios_procesos(usuario_id:str):
    return get('_id', conn.rappidron.usuarios, usuario_id)

"""
Si los usuarios tuviesen más campos que los de login, el put tendría sentido y se realizaría sobre los datos personales.
En este caso no tiene mucho sentido hacer un update, ya que ninguno de los datos, a excepción de la contraseña (que tiene su propio endpoint),
se debería poder modificar.
"""
@usuarios_procesos.put('/update/{usuario_id}/', tags=['CRUD'])
def update_usuarios_procesos(usuario_id:str, usuario:Usuario):
    return put('_id', conn.rappidron.usuarios, usuario_id, usuario)
    
@usuarios_procesos.delete('/delete/{usuario_id}/', tags=['CRUD'])
def delete_usuarios_procesos(usuario_id:str):
    return delete('_id', conn.rappidron.usuarios, usuario_id)

@usuarios_procesos.post("/login/", tags=['Login'])
def login(user: str, password: str):
    response = None
    
    try:
        if user and password:
            user_dict = conn.rappidron.usuarios.find_one({ "user": user })

            print("user_dict:", user_dict)

            if user_dict:
                user_dict["_id"] = str(user_dict["_id"])
                hashed_password = user_dict["password"]
                
                if pwd_context.verify(password, hashed_password):
                    access_token = auth_handler.encode_token(user_dict)
                    user_dict["token"] = access_token

                    data_object['message'] = user_dict

                    response = data_object
                else:
                    error['message'] = "Contraseña incorrecta"

                    response = error
            else:
                error['message'] = "El usuario ingresado no existe"

                response = error
        else:
            data_object['message'] = "You must enter a username and a password"

            response = data_object
    except Exception as e:
        error['message'] = str(e)

        response = error

    return response

@usuarios_procesos.put('/password/{usuario_id}/', tags=['Password'])
def update_password(usuario_id: str, password:str):
    response = None

    try:
        if re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,12}$', password):
            password = pwd_context.hash(password)
            response = put('_id', conn.rappidron.usuarios, usuario_id, { "password": password })
        else:
            error['message'] = "The password must be 6 to 12 characters long and must have at least one uppercase letter and one number"

            response = error
    except Exception as e:
        error['message'] = str(e)

        response = error

    return response