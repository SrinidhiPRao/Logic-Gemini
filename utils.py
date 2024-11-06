import sys
import json
from re import *

def prologify(gemini_response: str) -> dict[str, str]:
    """
    Retrieves the knowledge base and query code from gemini response.
    
    Args:
        gemini_response (str): The raw gemini response.

    Returns:
        dict: Retrieve using result["knowledge_base"] and result["queries"] respectively.
    """
    kb_plus_queries = gemini_response.split('?-')
    try:
        knowledge_base = kb_plus_queries[0][10:]
        queries = kb_plus_queries[1][:-3]
    except IndexError:
        queries = ''
        knowledge_base = kb_plus_queries[0][10:-3]

    return {
    "knowledge_base": knowledge_base,
    "queries": queries
    }
# def json_to_prolog(json_data: dict) -> str:
#     prolog_code = []

#     # Convert facts to Prolog syntax
#     for fact in json_data.get("facts", []):
#         subject = fact["subject"]
#         predicate = fact["predicate"]
#         object_ = fact["object"]
#         prolog_code.append(f"{predicate}({subject}, {object_}).")

#     # Convert rules to Prolog syntax
#     for rule in json_data.get("rules", []):
#         head = rule["head"]
#         body_conditions = ", ".join(rule["body"])
#         prolog_code.append(f"{head} :- {body_conditions}.")

#     knowledge_base = "\n".join(prolog_code)

#     query = json_data.get("query")
        
#     # Join the list into a single string of Prolog code
#     return {
#             "knowledge_base": knowledge_base,
#             "queries": query
#         }

# import json

# def gemini_response_to_prolog(response: str) -> str:
#     """
#     Convert a JSON response string from Gemini into Prolog code.
    
#     Parameters:
#         response (str): The JSON response string from Gemini.
        
#     Returns:
#         str: Prolog code generated from the JSON data.
#     """
#     # Parse the Gemini response string into JSON

#     try:
#         response = response.strip('/n')
#         json_data = json.loads(response[8:-4])
#     except json.JSONDecodeError:
#         print(f"response: {response[8:-3]}")
#         raise ValueError("Invalid JSON response from Gemini")

#     # Generate Prolog code
#     return json_to_prolog(json_data)
