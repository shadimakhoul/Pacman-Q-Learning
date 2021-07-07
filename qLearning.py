import numpy as np
import random
from IPython.display import clear_output
from time import sleep
import pacman as pc
import ui


def step(action, map1):
    done = False
    reward = 0
    next_x, next_y = pc.next_position(map1, action)
    s = pc.move_ghosts(map1)
    if pc.is_a_ghost(map1, next_x, next_y):
        reward -= 10
        done = True
        pc.move_pacman(map1, next_x, next_y)
        print("Agent has been eaten")

    elif pc.is_a_wall(map1, next_x, next_y):
        reward = -2
        print("Is a Wall")
    elif pc.is_a_pill(map1, next_x, next_y):
        reward += 5
        pc.move_pacman(map1, next_x, next_y)
        print("pill")
        remaining_pills = pc.total_pills(map1)
        if remaining_pills == 0:
            done = True
            print("Agent suddenly wins")

    else:
        reward -= 1
        pc.move_pacman(map1, next_x, next_y)
        print("Move")

    return map1, reward, done


def check_state(map9, maps):
    for i in range(len(maps)):
        if map9 == maps[i]:
            return i, True
        else:
            continue
    n = len(maps)
    return n, False


def print_frame(frames):
    for i, frame in enumerate(frames):
        clear_output(wait=True)
        # print(frame['frame'].getvalue())
        # print(f"Timestep: {i + 1}")
        print(f"State: {frame['state']}")
        print(f"Action: {frame['action']}")
        print(f"Reward: {frame['reward']}")
        sleep(.1)


def qlearning(map1, alpha, gamma, epsilon, q_table, maps=[], frame=[], epoch=0, penalties=0, reward=0, i=0):
    action = 0
    frame = []
    done = False
    state, check = check_state(map1, maps)
    state = int(state)
    if check == False:
        q_table.append([0, 0, 0, 0])
        m = map1.copy()
        maps.append(m)

    while not done:
        frame.append({
            "frame": ui.ui_print(map1),
            "state": state,
            "reward": reward,
            "action": action
        })
        if random.uniform(0, 1) < epsilon:
            action = random.uniform(0, 4)
        else:
            action = np.argmax(q_table[state])
        action = int(action)
        next_state, reward, done = step(action, map1)
        map1 = next_state
        new_state, check = check_state(map1, maps)
        new_state = int(new_state)

        if check == False:
            q_table.append([0, 0, 0, 0])
            m = map1.copy()
            maps.append(m)

        old_value = q_table[state][action]
        next_max = np.max(q_table[new_state])
        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        q_table[state][action] = new_value
        if reward == -10:
            penalties += 1
        state = new_state
        epoch += 1
        print("state: ", state)
        print("Reward: ", reward)
        print("Action: ", action)
        print("Penalties: ", penalties)
        print("This is the Iteration number " + str(i))
    return q_table, frame, maps, epoch, penalties, reward


def model(map2, iteration, alpha, gamma, epsilon, q_table=[]):
    frame = []
    maps = []
    epoch = 0
    penalties = 0
    reward = 0
    for i in range(iteration):
        map2 = pc.reset()
        q_table, frame, maps, epoch, penalties, reward = qlearning(map2, alpha, gamma, epsilon, q_table, maps, frame,
                                                                   epoch, penalties, reward, i)
    print(penalties)
    print(epoch)
    print(q_table)
    return q_table
    # print_frame(frame)


map1 = pc.reset()
table = []
table = model(map1, 100, 0.1, 0.6, 0.2, table)