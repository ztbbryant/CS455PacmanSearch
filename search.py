# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
	
    """
    "*** YOUR CODE HERE ***"

    from game import Directions
    closedSet = set()
    stack = util.Stack()
    startState = problem.getStartState()
    
	#Define a tuple that has state, directions, and path cost to that point
    info = (startState,[], 0)
    state = info[0]
    direction = info[1]
    cost = info[2]

  #Push the tuple into the stack
    stack.push(info)

		#While the stack is not empty, keep running
    while not stack.isEmpty():
		node = stack.pop()

		#Check if the start state is the goal
		if problem.isGoalState(node[0]):
			return node[1]
	
		#Check if node is in the closed set
		if node[0] not in closedSet:
			closedSet.add(node[0])

			#Find successors and add them to the stack
			for successor in problem.getSuccessors(node[0]): 
				path = node[1]
				path = path + [successor[1]]
				stack.push((successor[0], path, cost))
			
def breadthFirstSearch(problem):
	"""Search the shallowest nodes in the search tree first."""
	"*** YOUR CODE HERE ***"
	
	from game import Directions
	closedSet = set()
	Queue = util.Queue()
	startState = problem.getStartState()
	
	#Define a tuple that has state, directions, and path cost to that point
	info = (startState,[], 0)
	state = info[0]
	direction = info[1]
	cost = info[2]
    
	#Push the tuple into the queue
	Queue.push(info)
	while not Queue.isEmpty():
		node = Queue.pop()

		#Check if the start state is the goal
		if problem.isGoalState(node[0]):
			return node[1]
	
		#Check if node is in closed set, if not add it
		if node[0] not in closedSet:
			closedSet.add(node[0])

			#Find successors for the node and add to queue
			for successor in problem.getSuccessors(node[0]): 
				path = node[1]
				path = path + [successor[1]]
				Queue.push((successor[0], path, cost))
	
def uniformCostSearch(problem):
	"""Search the node of least total cost first."""
	"*** YOUR CODE HERE ***"
	from game import Directions
	closedSet = set()
	Queue = util.PriorityQueue()
	startState = problem.getStartState()
	
	#Define a tuple that has state, directions, and path cost to that point
	info = (startState,[], 0)
	state = info[0]
	direction = info[1]
	cost = info[2]
    
	Queue.push(info, cost)
	while not Queue.isEmpty():
		node = Queue.pop()
	
		if problem.isGoalState(node[0]):
			return node[1]
	
		if node[0] not in closedSet:
			closedSet.add(node[0])
			cost = node[2]

			for successor in problem.getSuccessors(node[0]):
				path = node[1]
				path = path + [successor[1]]
				cost += successor[2]
				Queue.push((successor[0], path, cost), cost)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
	"""Search the node that has the lowest combined cost and heuristic first."""
	"*** YOUR CODE HERE ***"
	from game import Directions
	closedSet = set()
	Queue = util.PriorityQueue()
	startState = problem.getStartState()
	
	#Define a tuple that has state, directions, and path cost to that point
	info = (startState,[], 0)
	state = info[0]
	direction = info[1]
	cost = info[2]
	heurVal = heuristic(state,problem)
	cost += heurVal
    
	Queue.push(info, cost)
	while not Queue.isEmpty():
		node = Queue.pop()
	
		if problem.isGoalState(node[0]):
			return node[1]
	
		if node[0] not in closedSet:
			closedSet.add(node[0])
			cost = node[2]

			for successor in problem.getSuccessors(node[0]):
				path = node[1]
				path = path + [successor[1]]
				cost += successor[2]
				heurVal = heuristic(successor[0],problem)
				cost += heurVal
				Queue.push((successor[0], path, cost), cost)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
