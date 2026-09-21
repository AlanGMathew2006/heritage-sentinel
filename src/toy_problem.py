ACTIONS = {
    "write_notes": {"requires": set(), "cost": 3},
    "practice_problems": {"requires": {"write_notes"}, "cost": 2},
    "review": {"requires": set(), "cost": 1},
    "take_test": {"requires": {"review"}, "cost": 2},
}

GOAL = frozenset(ACTIONS.keys())
START = frozenset()

def available_actions(state):
    """Actions whose prerequisites are satisfied and not already done."""
    return [a for a, info in ACTIONS.items()
            if a not in state and info["requires"].issubset(state)]

def apply_action(state, action):
    return state | {action}