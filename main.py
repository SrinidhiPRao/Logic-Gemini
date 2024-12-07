from gemini import Gemini_Model
from utils import prologify
from prolog import create_knowledge_base, query_knowledge_base


def main(prompt: str) -> str:
    gemini_model = Gemini_Model()
    
    
    gemini_response = gemini_model.query_gemini(prompt)
    
    prolog_input = prologify(gemini_response)
    
    create_knowledge_base(prolog_input["knowledge_base"])
    prolog_output = query_knowledge_base(prolog_input["queries"])

    natural_language_output = gemini_model.send_results(prolog_output)

    return natural_language_output



if __name__ == "__main__":
    print(main(input("Enter query: ")))
