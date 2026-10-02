# Question (Lab P1): If you swapped the problem file, did the planner need to change, Why or why not?

For my toy problem file, I made into a scenario of the steps necessary to be prepared to take a test. As I ran the toy problem file in main.py using the unmodified bfs search in planner.py, I concluded that I didn't need to change anything in planner.py. This is because the bfs search in planner.py only relies on a generic state, a goal condition, a funtion that lists all the available actions, and a function to apply the actions. Furthermore, this shows that bfs search is not tied to a particular domain like the heritage restoration or the toy problem. Instead the algorithm solely explores the state space using the abstract fields.

# Question (Lab P2): What did test_no_solution_returns_none catch that you didn't expect?

In my case for the test_no_solution_returns_none function did actually return none when running by bfs_search to show that there is an unreachable goal rather than an infinite loop to search for possible paths.

# Question (Lab P3): What did you see in the hidden-trap experiment, and why?

During the hidden-trap experiment, when adjusting the variables to use set, the restoration plan generated different plans each itteration and wasn't as consistent as before. This is because Python can iterate over a set in a different order as the strings are hashed randomly.

# Question (Lab P3): Your Lab 2 oracle was correct when you wrote it. What does its failure here tell you about tests over time?

The failure of the oracle here told me that Lab 2 was only checking for prerequisites nad completeness which made it approve a plan that was valid under the old requirements. However, the old oracle was not familiar with the new implementation of the tranche-cost rule showing that the tests are only valid at the time they were created. This means that tests decay over time and as new implementations are made, the tests should be updated as well.
