from dummy_frontend import user_input
from gemini import Gemini_Model
from utils import prologify
from prolog import create_knowledge_base, query_knowledge_base


def main():
    gemini_model = Gemini_Model()
    prompt = user_input()
    
    gemini_response = gemini_model.query_gemini(prompt)
    
    prolog_input = prologify(gemini_response)
    
    create_knowledge_base(prolog_input["knowledge_base"])
    prolog_output = query_knowledge_base(prolog_input["queries"])

    natural_language_output = gemini_model.send_results(prolog_output)

    print(natural_language_output)


if __name__ == "__main__":
    main()
