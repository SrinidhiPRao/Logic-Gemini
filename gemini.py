from os import getenv
from dotenv import load_dotenv
import google.generativeai as genai

class Gemini_Model:
    def __init__(self):
        load_dotenv()
        API_Key = getenv("API_KEY")

        genai.configure(api_key=API_Key)

        model = genai.GenerativeModel("gemini-1.5-flash")
        
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
        prompt = "Convert the following question into Prolog facts and rules, and generate a Prolog-compatible query. Only give the code, do not give any explanation."
        prompt += natural_language_query
        
        response = self.model.generate_content(prompt)
        response_text = response.text
        return response_text

    def send_results(self, results: dict) -> str:
        """
        Sends the prolog output back to Gemini.

        Args:
            results (dict): The results from prolog.
        Returns:
            str: Natural language interpretation of prolog results.
        
        """
        prompt = str(results) + ".This is the solution to "+ self.query +". Write this out in natural language."
        response = self.model.generate_content(prompt)
        response_text = str(response.text)
        return response_text

