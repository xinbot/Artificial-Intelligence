# Fall 2012 6.034 Lab 2: Search
#
# Your answers for the true and false questions will be in the following form.  
# Your answers will look like one of the two below:
#ANSWER1 = True
#ANSWER1 = False

# 1: True or false - Hill Climbing search is guaranteed to find a solution
#    if there is a solution
ANSWER1 = False

# 2: True or false - Best-first search will give an optimal search result
#    (shortest path length).
#    (If you don't know what we mean by best-first search, refer to
#     http://courses.csail.mit.edu/6.034f/ai3/ch4.pdf (page 13 of the pdf).)
ANSWER2 = False

# 3: True or false - Best-first search and hill climbing make use of
#    heuristic values of nodes.
ANSWER3 = True

# 4: True or false - A* uses an extended-nodes set.
ANSWER4 = True

# 5: True or false - Breadth first search is guaranteed to return a path
#    with the shortest number of nodes.
ANSWER5 = True

# 6: True or false - The regular branch and bound uses heuristic values
#    to speed up the search for an optimal path.
ANSWER6 = False

# Import the Graph data structure from 'search.py'
# Refer to search.py for documentation
from search import Graph

## Optional Warm-up: BFS and DFS
# If you implement these, the offline tester will test them.
# If you don't, it won't.
# The online tester will not test them.
def bfs(graph, start, goal):
    if start == goal:
        return [start]
    else:
        # Form a one-element queue consisting of a zero-length path that contains
        # only the root node.
        queue = []
        queue.append([start])
        # Avoid extending the same node multiple times.
        extended = set()
        extended.add(start)
        # Until the first path in the queue terminates at the goal node or the queue is empty
        while len(queue) > 0:
            # Remove the first path from the queue
            path = queue.pop(0)
            # The terminal node
            node = path.pop()
            # Extending the first path to all the neighbors of the terminal node
            for neighbour in graph.get_connected_nodes(node):
                # Reject all new paths with loops
                if neighbour not in extended:
                    if neighbour == goal:
                        # The goal node is found
                        return path + [node, neighbour]
                    else:
                        extended.add(neighbour)
                        # Add new paths, if any, to the back of the queue
                        queue.append(path + [node, neighbour])
        return []

## Once you have completed the breadth-first search,
## this part should be very simple to complete.
def dfs(graph, start, goal):
    if start == goal:
        return [start]
    else:
        # Form a one-element queue consisting of a zero-length path that contains
        # only the root node.
        queue = []
        queue.append([start])
        # Avoid extending the same node multiple times.
        extended = set()
        extended.add(start)
        # Until the first path in the queue terminates at the goal node or the queue is empty
        while len(queue) > 0:
            # Remove the first path from the queue
            path = queue.pop(0)
            # The terminal node
            node = path.pop()
            # Extending the first path to all the neighbors of the terminal node
            for neighbour in graph.get_connected_nodes(node):
                # Reject all new paths with loops
                if neighbour not in extended:
                    if neighbour == goal:
                        # The goal node is found
                        return path + [node, neighbour]
                    else:
                        extended.add(neighbour)
                        # Add new paths, if any, to the front of the queue
                        queue.insert(0,  path + [node, neighbour])
        return []

## Now we're going to add some heuristics into the search.  
## Remember that hill-climbing is a modified version of depth-first search.
## Search direction should be towards lower heuristic values to the goal.
def hill_climbing(graph, start, goal):
    raise NotImplementedError

## Now we're going to implement beam search, a variation on BFS
## that caps the amount of memory used to store paths.  Remember,
## we maintain only k candidate paths of length n in our agenda at any time.
## The k top candidates are to be determined using the 
## graph get_heuristic function, with lower values being better values.
def beam_search(graph, start, goal, beam_width):
    raise NotImplementedError

## Now we're going to try optimal search.  The previous searches haven't
## used edge distances in the calculation.

## This function takes in a graph and a list of node names, and returns
## the sum of edge lengths along the path -- the total distance in the path.
def path_length(graph, node_names):
    raise NotImplementedError


def branch_and_bound(graph, start, goal):
    raise NotImplementedError

def a_star(graph, start, goal):
    raise NotImplementedError


## It's useful to determine if a graph has a consistent and admissible
## heuristic.  You've seen graphs with heuristics that are
## admissible, but not consistent.  Have you seen any graphs that are
## consistent, but not admissible?

def is_admissible(graph, goal):
    raise NotImplementedError

def is_consistent(graph, goal):
    raise NotImplementedError

HOW_MANY_HOURS_THIS_PSET_TOOK = '24'
WHAT_I_FOUND_INTERESTING = 'Optimal Searching'
WHAT_I_FOUND_BORING = 'Debugging'
