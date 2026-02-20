addition(A, B, Result) :- Result is A + B.
subtraction(A, B, Result) :- Result is A - B.
multiplication(A, B, Result) :- Result is A * B.
division(A, B, Result) :- Result is A / B.
int_division(A, B, Result) :- Result is A // B.
modulus(A, B, Result) :- Result is A mod B.
exponentiation(A, B, Result) :- Result is A ** B.
absolute(A, Result) :- Result is abs(A).
square_root(A, Result) :- Result is sqrt(A).
to_float(A, Result) :- Result is float(A).
round_number(A, Result) :- Result is round(A).
truncate_number(A, Result) :- Result is truncate(A).
fractional_part(A, Result) :- Result is float_fractional_part(A).
integer_part(A, Result) :- Result is float_integer_part(A).
minimum(A, B, Result) :- Result is min(A, B).
maximum(A, B, Result) :- Result is max(A, B).
pi_value(Result) :- Result is pi.
