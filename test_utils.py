from utils import prologify


gemini_response = """```prolog
parent(john, mary).
parent(john, tom).
parent(mary, ann).
parent(mary, lily).
parent(tom, sam).

grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
aunt(X, Y) :- sibling(X, Z), parent(Z, Y).
uncle(X, Y) :- sibling(X, Z), parent(Z, Y).
cousin(X, Y) :- parent(A, X), parent(B, Y), sibling(A, B).

?- sibling(X, tom).
```"""

print(prologify(gemini_response))