from gemini import Gemini_Model

g = Gemini_Model()
# g.query = "Socrates is a man. All men are mortal. What is Socrates?"
g.query_gemini("Socrates is a man. All men are mortal. What is Socrates?")
print(g.send_results({'result': True}))
