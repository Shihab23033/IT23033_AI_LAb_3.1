move(1, Source, Target, _) :-
    write('Move disk 1 from '), write(Source), write(' to '), writeln(Target).

move(N, Source, Target, Auxiliary) :-
    N > 1,
    M is N - 1,
    move(M, Source, Auxiliary, Target),
    write('Move disk '), write(N), write(' from '), write(Source), write(' to '), writeln(Target),
    move(M, Auxiliary, Target, Source).
