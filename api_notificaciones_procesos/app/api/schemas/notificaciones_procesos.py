def notificaciones_procesosEntity(item) -> dict():
    try:
        return {
           
        }
    except Exception as e:
        return (str(e),item)

def notificaciones_procesossEntity(entity) -> list():
    return [notificaciones_procesosEntity(item) for item in entity]
