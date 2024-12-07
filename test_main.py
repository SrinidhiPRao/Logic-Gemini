from gemini import Gemini_Model
from prolog import create_knowledge_base, query_knowledge_base
from utils import prologify

# natural_language_query = "Socrates is a man. All men are mortal. What is Socrates?"
# natural_language_query = "A is standing ahead of B, B is standing ahead of C. D joins the queue behind A. Who is behind D?"
natural_language_query = "I am a 4 digit number. My rightmost digit is not divisible by 2. The sum of my digits is 20, and all my digits are in strictly decreasing order from left to right. One of my digits is 4 times one of my other digits, and the difference between my 2 middle digits is more than 3. What number am I?"

g = Gemini_Model()
gemini_response = g.query_gemini(natural_language_query)


print(f"Gemini's response was: {gemini_response}")
print('*'*140)

util_result = prologify(gemini_response)

print(f"The utils result was: {util_result}")
print('*' * 140)

create_knowledge_base(util_result["knowledge_base"])
prolog_result = query_knowledge_base(util_result["queries"])

print(f"The prolog result was: {prolog_result}")
print('*' * 140)

natural_language_result = g.send_results(prolog_result)
print(f"The natural language result is: {natural_language_result}")
print("*" * 140)