% c_to_f(C, F): convert Celsius C to Fahrenheit F
c_to_f(C, F) :-
    F is C * 9 / 5 + 32.

% below_freezing_c(C): true if C is below 0°C
below_freezing_c(C) :-
    C < 0.

% below_freezing_f(F): true if F is below 32°F
below_freezing_f(F) :-
    F < 32.
