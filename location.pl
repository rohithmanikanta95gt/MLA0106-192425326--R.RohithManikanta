% --- Facts: Location(city, state) ---
location(chennai, tamilnadu).
location(mumbai, maharashtra).
location(delhi, delhi).
location(bangalore, karnataka).

% --- Facts: Stays(person, city) ---
stays(john, chennai).
stays(sita, mumbai).
stays(ravi, delhi).
stays(arun, bangalore).

% --- Rule: Display person, city, state ---
display_details(Person, City, State) :-
    stays(Person, City),
    location(City, State).

% --- Rule: Given person, find the state ---
state_of_person(Person, State) :-
    stays(Person, City),
    location(City, State).
