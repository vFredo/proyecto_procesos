def solicitudes_procesosEntity(item) -> dict():
    try:
        return {
           
        }
    except Exception as e:
        return (str(e),item)

def solicitudes_procesossEntity(entity) -> list():
    return [solicitudes_procesosEntity(item) for item in entity]
