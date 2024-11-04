from pyswip import Prolog
from pyswip.prolog import PrologError
from sys import exit

def create_knowledge_base(knowledge: str) -> None:
    with open("db.pl", "w") as db:
        db.write(knowledge)
    
# currently works for a single query only
def query_knowledge_base(queries: str) -> dict:
    Prolog.consult("db.pl")
    # return list(Prolog.query(queries))

    try:
        prolog_result = next(Prolog.query(queries))
        if prolog_result == {}:
            return {"result": True}
        else:
            return prolog_result
    except PrologError:
        exit("Gemini response has faulty logic or prolog engine has failed.")
    except StopIteration:
        return {"result": False}
    
