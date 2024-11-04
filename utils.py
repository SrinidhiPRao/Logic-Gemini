import sys

def prologify(gemini_response: str) -> dict[str, str]:
    """
    Retrieves the knowledge base and query code from gemini response.
    
    Args:
        gemini_response (str): The raw gemini response.

    Returns:
        dict: Retrieve using result["knowledge_base"] and result["queries"] respectively.
    """

    try:
        kb_plus_queries = gemini_response.split('?-')
        knowledge_base = kb_plus_queries[0][10:]
        queries = kb_plus_queries[1]

        return {
        "knowledge_base": knowledge_base,
        "queries": queries
        }
    except IndexError:
        print(f"Gemini output: {kb_plus_queries}")
        sys.exit("Incorrect Prolog code sent by Gemini API.")

    
