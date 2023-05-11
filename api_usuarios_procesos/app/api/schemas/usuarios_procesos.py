def usuarios_procesosEntity(item) -> dict():
    try:
        return {
           
        }
    except Exception as e:
        return (str(e),item)

def usuarios_procesossEntity(entity) -> list():
    return [usuarios_procesosEntity(item) for item in entity]
