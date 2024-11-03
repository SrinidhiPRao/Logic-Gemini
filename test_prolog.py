from prolog import create_knowledge_base, query_knowledge_base


kb = """parent(john, mary).
parent(john, tom).
parent(mary, ann).
parent(mary, lily).
parent(tom, sam).

grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
aunt(X, Y) :- sibling(X, Z), parent(Z, Y).
uncle(X, Y) :- sibling(X, Z), parent(Z, Y).
cousin(X, Y) :- parent(A, X), parent(B, Y), sibling(A, B)."""

query1 = """sibling(X, tom).
"""
query2 = """aunt(tom, lily).
"""

create_knowledge_base(kb)

print(query_knowledge_base(query2))
