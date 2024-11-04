from os import getenv
from dotenv import load_dotenv

import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

class Gemini_Model:
    def __init__(self):
        load_dotenv()
        API_Key = getenv("API_KEY")

        genai.configure(api_key=API_Key)

        # model = genai.GenerativeModel("gemini-1.5-flash")
        model = genai.GenerativeModel("gemini-1.5-pro")

        self.model = model

    def query_gemini(self, natural_language_query: str) -> str:
        """
        Queries Gemini with the user's prompt along with some pre-prompting.
        
        Args:
            natural_language_query (str): The user's query.

        Returns:
            str: Gemini's prolog response.
        """
        self.query = natural_language_query
        prompt = open("input_prompt.txt", 'r').read()
        prompt += natural_language_query
        
        response = self.model.generate_content([prompt], 
            safety_settings={
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            })

        try:
            response_text = str(response.text)
            return response_text
        except ValueError:
            print(response.prompt_feedback)
            return "Harmful response and/or query"

    def send_results(self, results: dict) -> str:
        """
        Sends the prolog output back to Gemini.

        Args:
            results (dict): The results from prolog.
        Returns:
            str: Natural language interpretation of prolog results.
        
        """

        prompt = "The user's query is " + self.query + open('output_prompt.txt', 'r').read() + "This is the result" + str(results) 
        response = self.model.generate_content([prompt],
            safety_settings={
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            })

        try:
            response_text = str(response.text)
            return response_text
        except ValueError:
            print(response.prompt_feedback)
            return "Harmful response and/or query."

