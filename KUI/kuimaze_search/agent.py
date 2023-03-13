from queue import PriorityQueue
import kuimaze
import os
import time
class Agent(kuimaze.BaseAgent):
    '''
    Simple example of agent class that inherits kuimaze.BaseAgent class 
    '''
    def __init__(self, environment):
        self.environment = environment
    
    def heuristics(self, current, goal):
        '''
        Simple method which returns a measure of the distance from the current position the end point
        Parameters:
        current - the current position where the agent is located
        goal - the end point or destination position
        Returns:
        Euclidean distance between these two positions
        '''
        x1, y1 = current    # the x and y coordinates of the current position
        x2, y2 = goal       # the x and y coordinates of the destination position
        return abs(x2-x1) + abs(y2-y1)
    
    def find_path(self):
        '''
        This method returns the optimal path or one of the optimal paths within the environment
        '''
        ###    INITIALIZING OF PARAMETERS    ###
        path = []     # initializing of path
        frontier = PriorityQueue()   # initializing of priority queue which represents the open positions in the (heuristics, position) form
        parents = {}    # initializing dictionary which maps to parent position which would help get the path
        costs = {}      # initializing dictionary which maps to cost from the the start position to the current position based on current path
        explored = set()  # initializing the set of closed positions within the environment
        observation = self.environment.reset() # must be called first, it is necessary for maze initialization
        goal = observation[1][0:2]  # The destination position
        position = observation[0][0:2] # The start position
        frontier.put((0,position))    # inputting the start position into the queue
        explored.add(position)        # adding the start positions the explored positions
        costs[position] = 0          # initializing the cost of start to start which is 0
        parents[position] = None     # initializing the parent of the start position to None

        # Search through the enviroment while there are still open nodes
        while not frontier.empty():
            curr_pos = frontier.get()[1]  # getting the current node
            # Once we've reached our destination we break
            if curr_pos == goal:
                break
            # We go through the children position of the current position
            next_nodes = self.environment.expand(curr_pos)
            for (next_pos, weight) in next_nodes:
                new_cost = costs[curr_pos] + weight   # the current cost
                # We check to see if we need to update the costs and parents dictionaries 
                if next_pos not in explored or new_cost < costs[next_pos]:
                    costs[next_pos] = new_cost  # update to costs dictionary
                    parents[next_pos] = curr_pos  # update to parents dictionary
                    # Adding of this child position such that it is ordered to give us the closest optimal position
                    frontier.put((new_cost + self.heuristics(next_pos, goal), next_pos))     
                    explored.add(next_pos)  # update to the explored positions
                
        # Now that we have the reached the goal we try to find an optimal path
        node = goal  # we start from the destination position
        # if there are no optimal paths
        if node not in parents:
            return None
        # We are checking for each parent from the destination position to the start position
        while parents[node] is not None:
            path.append(node)
            node = parents[node]
        path.append(position)
        path.reverse()   # We reverse so we go from start to destination and not vice versa
        if len(path):    
            return path
        

if __name__ == '__main__':

    MAP = 'maps/easy/easy3.bmp'
    MAP = os.path.join(os.path.dirname(os.path.abspath(__file__)), MAP)
    GRAD = (0, 0)
    SAVE_PATH = False
    SAVE_EPS = False

    env = kuimaze.InfEasyMaze(map_image=MAP, grad=GRAD)       # For using random map set: map_image=None
    agent = Agent(env) 

    path = agent.find_path() 
    print(path)
    env.set_path(path)          # set path it should go from the init state to the goal state
    if SAVE_PATH:
        env.save_path()         # save path of agent to current directory
    if SAVE_EPS:
        env.save_eps()          # save rendered image to eps
    env.render(mode='human')
    time.sleep(2)              




