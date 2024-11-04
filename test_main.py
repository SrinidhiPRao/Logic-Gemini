from gemini import Gemini_Model
from prolog import create_knowledge_base, query_knowledge_base
from utils import prologify

# gemini_response = """```prolog
# parent(john, mary).
# parent(john, tom).
# parent(mary, ann).
# parent(mary, lily).
# parent(tom, sam).

# grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
# sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
# aunt(X, Y) :- sibling(X, Z), parent(Z, Y).
# uncle(X, Y) :- sibling(X, Z), parent(Z, Y).
# cousin(X, Y) :- parent(A, X), parent(B, Y), sibling(A, B).

# ?- sibling(X, tom).
# ```"""

natural_language_query = "Socrates is a man. All men are mortal. What is Socrates?"

# natural_language_query = "Hello, how are you?"

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