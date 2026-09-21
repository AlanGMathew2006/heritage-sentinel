from restoration_graph import START, GOAL, available_actions, apply_action
from toy_problem import START as TOY_START, GOAL as TOY_GOAL, available_actions as toy_available_actions, apply_action as toy_apply_action
from planner import bfs_search

if __name__ == "__main__":
    plan = bfs_search(START, GOAL, available_actions, apply_action)
    toy_plan = bfs_search(TOY_START, TOY_GOAL, toy_available_actions, toy_apply_action)
    print("Restoration plan:", plan)
    print("Toy problem plan:", toy_plan)