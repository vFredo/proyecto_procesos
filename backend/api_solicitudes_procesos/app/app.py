from fastapi import FastAPI
from app.api.routes.solicitudes_procesos import solicitudes_procesos
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    openapi_url='/api/v1/solicitudes/openapi.json',
    docs_url='/api/v1/solicitudes/docs',
    title='API Solicitudes',
    description='Esta API realiza la función de administrar las solicitudes de domicilios. Básicamente, un CRUD.',
    version='0.0.1',
    terms_of_service='',
    contact={
        'name': 'Ingeniería de Sistemas y Computación',
        'url': 'www.javerianacali.edu.co',
        'email': 'estudiantesisc@javerianacali.edu.co',
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

app.include_router(solicitudes_procesos, prefix='/api/v1/solicitudes')
