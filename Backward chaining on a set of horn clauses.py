# ✅ Backward Chaining in AI using Horn Clauses (Fixed Version)

knowledge_base = {
    "vertebrate": ["mammal"],              # vertebrate(A) ⇐ mammal(A)
    "animal": ["vertebrate"],              # animal(A) ⇐ vertebrate(A)
    "bird": ["vertebrate", "flying"]       # bird(A) ⇐ vertebrate(A) ∧ flying(A)
}

facts = {"vertebrate(duck)", "flying(duck)", "mammal(cat)"}
visited = set()  # to prevent infinite recursion


def backward_chain(goal):
    # Prevent infinite loops
    if goal in visited:
        print(f"(Already visited {goal}, skipping to avoid loop.)")
        return False
    visited.add(goal)

    # Base case: if goal is a fact
    if goal in facts:
        print(f"{goal} is TRUE (fact)")
        return True

    # Extract predicate and argument
    predicate, arg = goal.split("(")
    arg = arg[:-1]  # remove closing parenthesis

    # Check for rules that conclude this predicate
    for conclusion, premises in knowledge_base.items():
        if conclusion == predicate:
            print(f"\nTo prove {goal}, need to prove: {premises}")
            all_true = True
            for premise in premises:
                new_goal = f"{premise}({arg})"
                if not backward_chain(new_goal):
                    all_true = False
            if all_true:
                print(f"✅ {goal} is TRUE (derived)")
                return True

    print(f"❌ {goal} cannot be proven (no matching fact or rule)")
    return False


# Run the backward chaining system
print("\n--- Backward Chaining on Horn Clauses ---\n")
backward_chain("bird(duck)")
print()
visited.clear()  # reset visited before next goal
backward_chain("animal(cat)")
