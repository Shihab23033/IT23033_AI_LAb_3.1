%1.Relationship

male(Rakib).
male(Kabir).
male(jamal).
male(Alif).

female(Sumaiya).
female(salma).
female(nasrin).
female(mitu).

father(Rakib, jamal).
mother(Sumaiya, jamal).

father(Rakib, nasrin).
mother(Sumaiya, nasrin).

father(jamal, Alif).
mother(nasrin, mitu).

father(Kabir, mitu).
mother(salma, mitu).

parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).

sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).


%2.Like-Dislike:

likes(Rakib, tea).
likes(Rakib, football).
likes(Kabir, coffee).

dislikes(Rakib, smoking).
dislikes(Kabir, tea).

friend(X, Y) :-
    likes(X, Z),
    likes(Y, Z),
    X \= Y.

