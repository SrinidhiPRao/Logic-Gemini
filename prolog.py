from pyswip import Prolog

def create_knowledge_base(knowledge: str) -> None:
    with open("db.pl", "w") as db:
        db.write(knowledge)
    
# currently works for a single query only
def query_knowledge_base(queries: str) -> dict:
    Prolog.consult("db.pl")
    # return list(Prolog.query(queries))
    prolog_result = next(Prolog.query(queries))

    if prolog_result == {}:
        return {"result": True}
    elif prolog_result == None:
        return {"result": False}
    else:
        return prolog_result
