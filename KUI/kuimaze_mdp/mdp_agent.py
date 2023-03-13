import collections
import kuimaze
import random
import os
import time
import sys

state = collections.namedtuple('State', ['x', 'y', 'reward'])  # initialising the format and parameters of non-terminal states

def find_policy_via_value_iteration(problem, discount_factor, epsilon):
    """The function returns the different actions of each non-terminal state by calculating the value for some
    number of iterations. The actions are determined each time and would continue iterating until the maximum error
    is less than the provided error margin
    Parameters:
    problem - the state environment for which we try to find the best policy (actions)
    discount_factor - a real number between 0 and 1 used to scale down the value
    epsilon- the provided error margin for which we use to implement a stopping condition once the error is lower
    Returns:
    action_dict- a dictionary with the tuple coordinates as keys and the best actions as values
    """
     ### INITIALISING REQUIRED PARAMETERS   ###
    x_dims = problem.observation_space.spaces[0].n  # the number of rows in the state environment
    y_dims = problem.observation_space.spaces[1].n  # the number of columns in the state environment
    states = problem.get_all_states()    # a list of all possible states within the environment
    action_dict = {}     # initialising the dictionary with the best policy (set of actions for each state)
    values = [ [0]*y_dims for i in range(x_dims)]  # initialising the value matrix
    errors = [0]*len(states)     # initialising the list of errors
    error = epsilon * 2      # initialising the maximum error
    ###  VALUE ITERATION  ###
    # Implementing the stopping condition of maximum error of all states being less than the error margin provided
    while error > epsilon:
        for i in range(len(states)):  # iterating through all possible states
            state = states[i]
            if problem.is_terminal_state(state):  # the condition that the current state is a terminal state
                action_dict[(state.x, state.y)] = None   # terminal states yield no action
                errors[i] = 0             # terminal states yield no error since the values are constant
                values[state.x][state.y] = state.reward  # terminal state has constant value
            else:             # the condition that the current state is a non-terimnal state
                actions = list(problem.get_actions(state))   # getting a list of all possible actions
                max_action = None            # initialising the best action for the current iteration
                max_value = - 10**9          # initialising the best value for this iteration
                for action in actions:       # iterating through all possible actions
                    value = state.reward     # initialise the value for the specific action
                    # Calculating the value of the current state based on the probability distribution
                    for next_state, prob in problem.get_next_states_and_probs(state, action):
                        value += discount_factor*prob*values[next_state.x][next_state.y]
                    if value > max_value:   # the condition that the current value is greater than the current maximum value 
                        max_value = value  # updating the value for this iteration
                        max_action = action  # updating the action for this iteration
                errors[i] = abs(max_value - values[state.x][state.y])   # calculating the error for this current state and iteration
                values[state.x][state.y] = max_value  # updating the value for this current state
                action_dict[(state.x, state.y)] = max_action  # updating the best action for the current state
        error = max(errors)   # the maximum error
    return action_dict


def find_policy_via_policy_iteration(problem, discount_factor):
    """The function returns the different actions of each non-terminal state by calculating the value for some
    number of iterations. The actions are determined each time and would continue iterating until we see that there
    is no change between the previous and current best action for all non-terminal states within the state environment
    Parameters:
    problem - the state environment for which we try to find the best policy (actions)
    epsilon- the provided error margin for which we use to implement a stopping condition once the error is lower
    Returns:
    action_dict- a dictionary with the tuple coordinates as keys and the best actions as values
    """
    x_dims = problem.observation_space.spaces[0].n    # the number of rows in the state environment
    y_dims = problem.observation_space.spaces[1].n    # the number of columns in the state environment
    states = problem.get_all_states()              # a list of all possible states within the environment
    action_dict = {}                    # initialising the dictionary with the best policy (set of actions for each state)
    values = [ [0]*y_dims for i in range(x_dims)]   # initialising the value matrix
    errors = [0]*len(states)   # initialising the array which tells us if there are any changes between the previous and current best action
    # Implementing the policy iteration to stop if there are no changes between the current and previous policy
    while min(errors) == 0:
        ###    POLICY EVALUATION   ####
        for state in states:   # iterating through all possible states within the state environment
            if problem.is_terminal_state(state):  # the condition of the state being a terminal state
                values[state.x][state.y] = state.reward  #  the value remains the same for terminal states
                continue
            if (state.x, state.y) not in action_dict:  # if it is the first iteration
                actions = list(problem.get_actions(state))
                action_dict[(state.x, state.y)] = actions[0] # set the current action to a random action
            action = action_dict[(state.x, state.y)]   # getting the previously calculated best action
            value = state.reward    # initialising the current value based on the action
            # Calculating the value of the current state based on the probability distribution
            for next_state, prob in problem.get_next_states_and_probs(state, action):
                value += discount_factor*prob*values[next_state.x][next_state.y]  
            values[state.x][state.y] = value   # updating the value of this specific non-terminal state

        ###   POLICY REFINEMENT    ###
        for i in range(len(states)): # iterating through all possible states
            state = states[i]
            if problem.is_terminal_state(state):   # the condition that it is a terminal state
                action_dict[(state.x, state.y)] = None  # terminal states don't warrant any action
                errors[i] = 1            # since they don't have any actions, there is no change to them
                values[state.x][state.y] = state.reward   # the value for terminal states don't change
            else:             # when it is a non-terminal state
                actions = list(problem.get_actions(state))   #  a list of all possible actions
                max_action = action_dict[(state.x, state.y)]   # getting the previously calculated best action
                max_value = values[state.x][state.y]  # getting the previously calculated best value
                for action in actions:     # iterating through all possible actions
                    value = state.reward    # initialising the value for this specific action
                    # Calculating the value of the current action based on the probability distribution
                    for next_state, prob in problem.get_next_states_and_probs(state, action):
                        value += discount_factor*prob*values[next_state.x][next_state.y]
                    if value > max_value: # the condition that the current value is greater than the current maximum value 
                        max_value = value # updating the current maximum value for this iteration
                        max_action = action # updating the current best action for this state for this iteration
                errors[i] = int(action_dict[(state.x, state.y)]==max_action)  # checking if the current and previous best calculated actions are the same
                action_dict[(state.x, state.y)] = max_action  # updating the action for this state
                values[state.x][state.y] = max_value   # updating the value for this state
    return action_dict            
def get_visualisation_values(dictvalues):
    if dictvalues is None:
        return None
    ret = []
    for key, value in dictvalues.items():
        # ret.append({'x': key[0], 'y': key[1], 'value': [value, value, value, value]})
        ret.append({'x': key[0], 'y': key[1], 'value': value})
    return ret

MAP = 'maps/easy/easy1.bmp'
MAP = os.path.join(os.path.dirname(os.path.abspath(__file__)), MAP)
PROBS = [0.4, 0.3, 0.3, 0]
GRAD = (0, 0)
SKIP = False
SAVE_EPS = False
GRID_WORLD4 = [[[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 0, 0]],
               [[255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255]],
               [[0, 0, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
               [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]]]

GRID_WORLD3 = [[[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 0, 0]],
               [[255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 0, 0]],
               [[0, 0, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]]]

REWARD_NORMAL_STATE = -0.04
REWARD_GOAL_STATE = 1
REWARD_DANGEROUS_STATE = -1

GRID_WORLD3_REWARDS = [[REWARD_NORMAL_STATE, REWARD_NORMAL_STATE, REWARD_NORMAL_STATE, REWARD_GOAL_STATE],
                       [REWARD_NORMAL_STATE, 0, REWARD_NORMAL_STATE, REWARD_DANGEROUS_STATE],
                       [REWARD_NORMAL_STATE, REWARD_NORMAL_STATE, REWARD_NORMAL_STATE, REWARD_NORMAL_STATE]]
if __name__ == "__main__":
    # Initialize the maze environment
    env = kuimaze.MDPMaze(map_image=GRID_WORLD3, probs=PROBS, grad=GRAD, node_rewards=GRID_WORLD3_REWARDS)
    # env = kuimaze.MDPMaze(map_image=GRID_WORLD3, probs=PROBS, grad=GRAD, node_rewards=None)
    # env = kuimaze.MDPMaze(map_image=MAP, probs=PROBS, grad=GRAD, node_rewards=None)
    # env.reset()
    policy = find_policy_via_value_iteration(env, 0.8, 0.0000001)
    # print(policy)
    # env.visualise(get_visualisation_values(policy))
    # env.render()
    # time.sleep(10)
    policy = find_policy_via_policy_iteration(env, 0.8)
    print(policy)
    env.visualise(get_visualisation_values(policy))
    env.render()
    time.sleep(10)