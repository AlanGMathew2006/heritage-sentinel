# restoration_csp.py — problem definition only.
from restoration_graph import ACTIONS      # reuse the Lab 1 data

VARIABLES = list(ACTIONS.keys())           # a list, not a set. Remember this.
DOMAINS = {a: list(range(1, len(VARIABLES) + 1)) for a in VARIABLES}

def build_constraints(actions=ACTIONS, tranche_cap=4):
    constraints = []

    # 1. all-different
    for i, a in enumerate(VARIABLES):
        for b in VARIABLES[i + 1:]:
            constraints.append(((a, b), lambda x, y: x != y))

    # 2. TODO: prerequisites. For each action and each action it requires,
    #    add a constraint on the pair (required, action) saying the
    #    required action's slot is smaller.
    for action, info in actions.items():
        for prereq in info["requires"]:
            constraints.append(((prereq, action), lambda x, y: x < y))

    # 3. TODO: tranche rule. One constraint over ALL variables: the summed
    #    cost of every action whose slot is <= 2 must be <= tranche_cap.
    #    Hint: scope = tuple(VARIABLES); the check function receives one
    #    slot per variable, in that same order.
    constraints.append((tuple(VARIABLES),
                        lambda *slots: sum(actions[a]["cost"] for a, s in zip(VARIABLES, slots) if s <= 2) <= tranche_cap))
    return constraints