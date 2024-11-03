from gemini import Gemini_Model

g = Gemini_Model()
# g.query = "Socrates is a man. All men are mortal. What is Socrates?"
print(f"Gemini's prolog response: {g.query_gemini("Socrates is a man. All men are mortal. Is Socrates mortal?")}")
# print(f"Gemini's natural language response: {g.send_results({'result': True})}")
print(f"Gemini's natural language response: {g.send_results({'result': False})}")
