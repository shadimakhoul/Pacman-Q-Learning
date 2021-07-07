import random

map = [
    "|--------|",
    "|...|....|",
    "|.P...P..|",
    "|G...@.|.|",
    "|.P...P..|",
    "|--------|"
]


def reset():
    map1 = [
        "|--------|",
        "|...|....|",
        "|.P...P..|",
        "|G...@.|.|",
        "|.P...P..|",
        "|--------|"
    ]

    return map1


# to find Pacman on the map
def find_pacman(map):
    pacman_x = -1
    pacman_y = -1
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == '@':
                pacman_x = x
                pacman_y = y

    return pacman_x, pacman_y


# to move pacman on the map
def move_pacman(map, next_pacman_x, next_pacman_y):
    pacman_x, pacman_y = find_pacman(map)
    new_row = map[pacman_x][0:pacman_y] + "." + map[pacman_x][pacman_y + 1:]
    map[pacman_x] = new_row
    new_row2 = map[next_pacman_x][0:next_pacman_y] + "@" + map[next_pacman_x][next_pacman_y + 1:]
    map[next_pacman_x] = new_row2


# move Ghost on the map
def moveGhost(map, nextGhostx, nextGhosty):
    ghostx, ghosty = find_ghosts(map)
    new_row = map[ghostx][0:ghosty] + "." + map[ghostx][ghosty + 1:]
    map[ghostx] = new_row
    new_row2 = map[nextGhostx][0:nextGhosty] + "G" + map[nextGhostx][nextGhosty + 1:]
    map[nextGhostx] = new_row2
    return map


# play function by the user
def play(map, key):
    next_x, next_y = next_position(map, key)

    # if it is a invalid key
    # is_an_invalid_key = next_x == -1 and next_y == -1
    # if is_an_invalid_key:
    # return False, True, False

    # if it is not within borders
    if not within_borders(map, next_x, next_y):
        return False, True, False

    # if it is a wall
    if is_a_wall(map, next_x, next_y):
        return False, True, False

    is_a_ghost = map[next_x][next_y] == 'G'
    if is_a_ghost:
        return True, False, False

    move_pacman(map, next_x, next_y)

    remaining_pills = total_pills(map)
    if remaining_pills == 0:
        return True, True, True
    else:
        return True, True, False


# return if the agent hits a wall
def is_a_wall(map, next_x, next_y):
    is_a_wall = map[next_x][next_y] == '|' or map[next_x][next_y] == '-'
    return is_a_wall


# return if the agent hits a gosts
def is_a_ghost(map, next_x, next_y):
    return map[next_x][next_y] == 'G'


# return if the agent eats a pill
def is_a_pill(map, next_x, next_y):
    return map[next_x][next_y] == 'P'


def is_a_pacman(map, next_x, next_y):
    return map[next_x][next_y] == '@'


def within_borders(map, next_x, next_y):
    number_of_rows = len(map)
    x_is_valid = 0 <= next_x < number_of_rows
    number_of_columns = len(map[0])
    y_is_valid = 0 <= next_y < number_of_columns
    return x_is_valid and y_is_valid


def total_pills(map):
    total = 0
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 'P':
                total += 1
    # total[x]=y
    # else:total[x]=-1
    return total


# move the pacman a one step
def next_position(map, key):
    x, y = find_pacman(map)
    next_x = -1
    next_y = -1
    if key == 0:
        next_x = x
        next_y = y - 1
    elif key == 1:
        next_x = x
        next_y = y + 1
    elif key == 2:
        next_x = x - 1
        next_y = y
    elif key == 3:
        next_x = x + 1
        next_y = y
    return next_x, next_y


# return location of the ghosts
def find_ghosts(map):
    ghosts = []
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 'G':
                ghosts.append([x, y])

    return ghosts


def move_ghosts(map):
    all_ghosts = find_ghosts(map)
    for ghost in all_ghosts:
        ghost_x = ghost[0]
        ghost_y = ghost[1]

        possible_directions = [
            [ghost_x, ghost_y + 1],
            [ghost_x, ghost_y - 1],
            [ghost_x - 1, ghost_y],
            [ghost_x + 1, ghost_y]
        ]

        # select a random possible movement
        # and get the x,y of the movement
        random_number = random.randint(0, 3)
        next_ghost_x = possible_directions[random_number][0]
        next_ghost_y = possible_directions[random_number][1]

        # checks before actually moving it!
        if not within_borders(map, next_ghost_x, next_ghost_y):
            continue

        if is_a_wall(map, next_ghost_x, next_ghost_y):
            continue

        if is_a_ghost(map, next_ghost_x, next_ghost_y):
            continue

        if is_a_pill(map, next_ghost_x, next_ghost_y):
            continue

        if is_a_pacman(map, next_ghost_x, next_ghost_y):
            return True

        # move the ghost to the random position
        everything_to_the_left = map[ghost_x][0:ghost_y]
        everything_to_the_right = map[ghost_x][ghost_y + 1:]
        map[ghost_x] = everything_to_the_left + "." + everything_to_the_right

        # the new place has the pacman
        everything_to_the_left = map[next_ghost_x][0:next_ghost_y]
        everything_to_the_right = map[next_ghost_x][next_ghost_y + 1:]
        map[next_ghost_x] = everything_to_the_left + "G" + everything_to_the_right

    return False