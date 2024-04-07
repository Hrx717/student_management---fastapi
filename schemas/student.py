def studentEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "age": int(item["age"]),
        "address": item["address"]
    }

def students(entity) -> list:
    return [studentEntity(item) for item in entity]