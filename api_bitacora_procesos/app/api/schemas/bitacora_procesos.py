def bitacora_procesosEntity(item) -> dict():
    try:
        return {
           
        }
    except Exception as e:
        return (str(e),item)

def bitacora_procesossEntity(entity) -> list():
    return [bitacora_procesosEntity(item) for item in entity]
