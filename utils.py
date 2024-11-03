
def prologify(gemini_response: str) -> dict[str, str]:
    """
    Retrieves the knowledge base and query code from gemini response.
    
    Args:
        gemini_response (str): The raw gemini response.

    Returns:
        dict: Retrieve using result["knowledge_base"] and result["queries"] respectively.
    """
    kb_plus_queries = gemini_response.split('?-')
    knowledge_base = kb_plus_queries[0][10:]
    # knowledge_base = kb_plus_queries[0]
    queries = kb_plus_queries[1]

    return {
        "knowledge_base": knowledge_base,
        "queries": queries
    }
