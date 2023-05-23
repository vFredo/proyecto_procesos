def usuarios_procesosEntity(item) -> dict():
    try:
        data = {}
        data["id"] = str(item["_id"])
        for i in list(item):
            if(str(i)!="_id"):
                data[str(i)] = (item[str(i)])
        return data
    except Exception as e:
        return (str(e),item)

def usuarios_procesossEntity(entity) -> list():
    return [usuarios_procesosEntity(item) for item in entity]
