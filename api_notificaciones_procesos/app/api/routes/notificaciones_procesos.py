import fastapi
from app.api.schemas.notificaciones_procesos import notificaciones_procesossEntity, notificaciones_procesosEntity
from app.api.models.notificaciones_procesos import Notificaciones_procesos
from app.api.config.db import conn
from app.api.utils.acces_security import get_current_username
from fastapi import APIRouter, Depends, HTTPException, Request, Response
from bson import ObjectId
from app.api.utils.jsonreturn import *
        
notificaciones_procesos = APIRouter()

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

@notificaciones_procesos.post('/notificaciones_procesos/', tags=['notificaciones_procesos'])
def post_notificaciones_procesos(notificaciones_procesos:Notificaciones_procesos):
    return post(notificaciones_procesos,conn.notificaciones_procesos.notificaciones_procesos)

@notificaciones_procesos.get('/notificaciones_procesos/{notificaciones_procesos_id}/', tags=['notificaciones_procesos'])
def get_notificaciones_procesos(notificaciones_procesos_id:str):
    return get('_id',conn.notificaciones_procesos.notificaciones_procesos,notificaciones_procesos_id)

@notificaciones_procesos.put('/notificaciones_procesos/{notificaciones_procesos_id}/', tags=['notificaciones_procesos'])
def update_notificaciones_procesos(notificaciones_procesos_id:str, notificaciones_procesos:Notificaciones_procesos):
    return put('_id',conn.notificaciones_procesos.notificaciones_procesos,notificaciones_procesos_id,notificaciones_procesos)
    
@notificaciones_procesos.delete('/notificaciones_procesos/{notificaciones_procesos_id}/', tags=['notificaciones_procesos'])
def delete_notificaciones_procesos(notificaciones_procesos_id:str):
    return delete('_id',conn.notificaciones_procesos.notificaciones_procesos,notificaciones_procesos_id)
