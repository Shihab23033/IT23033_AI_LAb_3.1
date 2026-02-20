%1.Relationship

male(rahim).
male(karim).
male(jamal).
male(arif).

female(amina).
female(salma).
female(nasrin).
female(mitu).

father(rahim, jamal).
mother(amina, jamal).

father(rahim, nasrin).
mother(amina, nasrin).

father(jamal, arif).
mother(nasrin, mitu).

father(karim, mitu).
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

likes(rahim, tea).
likes(rahim, football).
likes(karim, coffee).

dislikes(rahim, smoking).
dislikes(karim, tea).

friend(X, Y) :-
    likes(X, Z),
    likes(Y, Z),
    X \= Y.

