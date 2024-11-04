behind(anu, bala).
behind(bala, cory).
behind(donald, anu).

behind_recursive(X, Y) :- behind(X, Y).
behind_recursive(X, Y) :- behind(X, Z), behind_recursive(Z, Y).

