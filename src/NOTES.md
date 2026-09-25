# Question: If you swapped the problem file, did the planner need to change, Why or why not?

For my toy problem file, I made into a scenario of the steps necessary to be prepared to take a test. As I ran the toy problem file in main.py using the unmodified bfs search in planner.py, I concluded that I didn't need to change anything in planner.py. This is because the bfs search in planner.py only relies on a generic state, a goal condition, a funtion that lists all the available actions, and a function to apply the actions. Furthermore, this shows that bfs search is not tied to a particular domain like the heritage restoration or the toy problem. Instead the algorithm solely explores the state space using the abstract fields.

# Question: What did test_no_solution_returns_none catch that you didn't expect?

In my case for the test_no_solution_returns_none function did actually return none when running by bfs_search to show that there is an unreachable goal rather than an infinite loop to search for possible paths.
