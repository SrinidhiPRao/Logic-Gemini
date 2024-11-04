from gemini import Gemini_Model

g = Gemini_Model()

query1 = "Socrates is a man. All men are mortal. Is Socrates mortal?"
query2 = "Anu, bala and cory are walking behind one another.  Donald joins the line behind anu.  who is behind donald "

print(f"Gemini's prolog response: {g.query_gemini(query1)}")
# print(f"Gemini's prolog response: {g.query_gemini(query2)}")

# print(f"Gemini's natural language response: {g.send_results({'result': True})}")
# print(f"Gemini's natural language response: {g.send_results({'result': False})}")

