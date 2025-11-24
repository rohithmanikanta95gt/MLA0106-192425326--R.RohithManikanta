% sum_up_to_n(N, Sum): Sum = 1 + 2 + ... + N

% Base case
sum_up_to_n(1, 1).

% Recursive case: N > 1
sum_up_to_n(N, Sum) :-
    N > 1,
    N1 is N - 1,
    sum_up_to_n(N1, Partial),
    Sum is Partial + N.
