def inventario_procesosEntity(item) -> dict():
    try:
        return {
           
        }
    except Exception as e:
        return (str(e),item)

def inventario_procesossEntity(entity) -> list():
    return [inventario_procesosEntity(item) for item in entity]
