import fastapi
from app.api.schemas.bitacora_procesos import bitacora_procesossEntity, bitacora_procesosEntity
from app.api.models.bitacora_procesos import Bitacora_procesos
from app.api.config.db import conn
from app.api.utils.acces_security import get_current_username
from fastapi import APIRouter, Depends, HTTPException, Request, Response
from bson import ObjectId
from app.api.utils.jsonreturn import *
        
bitacora_procesos = APIRouter()

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

@bitacora_procesos.post('/bitacora_procesos/', tags=['bitacora_procesos'])
def post_bitacora_procesos(bitacora_procesos:Bitacora_procesos):
    return post(bitacora_procesos,conn.bitacora_procesos.bitacora_procesos)

@bitacora_procesos.get('/bitacora_procesos/{bitacora_procesos_id}/', tags=['bitacora_procesos'])
def get_bitacora_procesos(bitacora_procesos_id:str):
    return get('_id',conn.bitacora_procesos.bitacora_procesos,bitacora_procesos_id)

@bitacora_procesos.put('/bitacora_procesos/{bitacora_procesos_id}/', tags=['bitacora_procesos'])
def update_bitacora_procesos(bitacora_procesos_id:str, bitacora_procesos:Bitacora_procesos):
    return put('_id',conn.bitacora_procesos.bitacora_procesos,bitacora_procesos_id,bitacora_procesos)
    
@bitacora_procesos.delete('/bitacora_procesos/{bitacora_procesos_id}/', tags=['bitacora_procesos'])
def delete_bitacora_procesos(bitacora_procesos_id:str):
    return delete('_id',conn.bitacora_procesos.bitacora_procesos,bitacora_procesos_id)
