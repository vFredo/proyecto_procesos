from fastapi import FastAPI
from app.api.routes.inventario_procesos import inventario_procesos
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    openapi_url='/api/v1/inventario_procesos/openapi.json',
    docs_url='/api/v1/inventario_procesos/docs',
    title='',
    description='',
    version='0.0.1',
    terms_of_service='',
    contact={
        'name': '',
        'url': '',
        'email': '',
    },
    license_info={
        'name': '',
        'url': '',
    },
)

origins = ['*']
app.add_middleware(
 CORSMiddleware,
 allow_origins=origins,
 allow_credentials=True,
 allow_methods=['*'],
 allow_headers=['*'],
)

@app.on_event('startup')
async def startup():
    print('startup')

@app.on_event('shutdown')
async def shutdown():
    print('shutdown')

app.include_router(inventario_procesos, prefix='/api/v1/inventario_procesos')
