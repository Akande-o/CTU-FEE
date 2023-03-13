import kuimaze
import numpy as np
import sys
import os
import gym
from itertools import permutations
# MAP = 'maps/normal/normal3.bmp'
MAP = 'maps/easy/easy2.bmp'
MAP = os.path.join(os.path.dirname(os.path.abspath(__file__)), MAP)
# PROBS = [0.8, 0.1, 0.1, 0]
PROBS = [1, 0, 0, 0]
GRAD = (0, 0)
SKIP = False
VERBOSITY = 2

def wait_n_or_s():

    def wait_key():
        """
        returns key pressed ... works only in terminal! NOT in IDE!
        """
        result = None
        if os.name == 'nt':
            import msvcrt
            # https://cw.felk.cvut.cz/forum/thread-3766-post-14959.html#pid14959
            result = chr(msvcrt.getch()[0])
        else:
            import termios
            fd = sys.stdin.fileno()

            oldterm = termios.tcgetattr(fd)
            newattr = termios.tcgetattr(fd)
            newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
            termios.tcsetattr(fd, termios.TCSANOW, newattr)
            try:
                result = sys.stdin.read(1)
            except IOError:
                pass
            finally:
                termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        return result

    '''
    press n - next, s - skip to end ... write into terminal
    '''
    global SKIP
    x = SKIP
    while not x:
        key = wait_key()
        x = key == 'n'
        if key == 's':
            SKIP = True
            break

def get_visualisation(table):
    ret = []
    for i in range(len(table[0])):
        for j in range(len(table)):
            ret.append({'x': j, 'y': i, 'value': [table[j][i][0], table[j][i][1], table[j][i][2], table[j][i][3]]})
    return ret

def learn_policy(env):
    """ This function implements the q-learning method for reinforcement learning
    and returns a dictionary with states as keys and actions as values
    Parameters:
    env - The HardMaze environment whic we are to learn the best policy for
    Returns:
    action_dict - The dictionary output with states as keys and actions as values
    """
    ###    getting the parameters for the q_table    ###
    x_dims = env.observation_space.spaces[0].n  # no. of rows
    y_dims = env.observation_space.spaces[1].n  # no. of columns
    maze_size = tuple((x_dims, y_dims))
    num_actions = env.action_space.n     # no. of actions
    q_table = np.zeros([maze_size[0], maze_size[1], num_actions], dtype=float)
    action_dict = {}
    MAX_T = 1000  # max trials (for one episode)
    # iterating through the total number of trials 
    for i in range(MAX_T):
        obv = env.reset()   # initialising the state
        state = obv[0:2]
        total_reward = 0   # initialising the reward
        is_done = False
        # iterating through the environment till we reach a terminal node
        while not is_done:
            action = np.argmax(q_table[state[0]][state[1]])  # starting with random action
            obv, reward, is_done, _ = env.step(action)  # getting the next state, reward and terminality
            next_state = obv[0:2]
            next_max = np.max(q_table[next_state[0]][next_state[1]]) # getting the maximum q-value of the state
            # print(next_max)
            new_value = next_max +reward   # updating the q-value

            q_table[state[0]][state[1]][action] = new_value   # updating the q-table
            state = next_state   # going on to the next_state
    # genarating the dictionary with state keys and action values
    for i in range(x_dims):
        for j in range(y_dims):
            if (i, j) not in action_dict:
                action_dict[(i,j)] = np.argmax(q_table[i][j])
    return action_dict
    


if __name__ == "__main__":
    # Initialize the maze environment
    env = kuimaze.HardMaze(map_image=MAP, probs=PROBS, grad=GRAD)

    if VERBOSITY > 0:
        print('====================')
        print('works only in terminal! NOT in IDE!')
        print('press n - next')
        print('press s - skip to end')
        print('====================')
    
    '''
    Define constants:
    '''
    # Maze size
    x_dims = env.observation_space.spaces[0].n
    y_dims = env.observation_space.spaces[1].n
    maze_size = tuple((x_dims, y_dims))
    # print(maze_size)
    # Number of discrete actions
    num_actions = env.action_space.n
    # print(num_actions)
    # Q-table:
    q_table = np.zeros([maze_size[0], maze_size[1], num_actions], dtype=float)
    # if VERBOSITY > 0:
    #     env.visualise(get_visualisation(q_table))
    #     env.render()
    print(learn_policy(env))
    # print(q_table)

    # if VERBOSITY > 0:
    #     SKIP = False
    #     env.visualise(get_visualisation(q_table))
    #     env.render()
    #     wait_n_or_s()

    #     env.save_path()
    #     env.save_eps()