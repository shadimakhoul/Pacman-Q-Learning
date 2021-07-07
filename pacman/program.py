from ui import ui_print
from pacman import play
from ui import ui_key
from ui import ui_msg_win
from ui import ui_msg_lost
from pacman import  move_ghosts
map = [
    "|--------|",
    "|...|....|",
    "|...PP...|",
    "|G...@.|.|",
    "|........|",
    "|--------|"
]
game_finished = False
while not game_finished:
    ui_print(map)
    key = ui_key()
    valid_key, pacman_alive, won = play(map, key)

    pacman_was_hit = move_ghosts(map)

    if (not pacman_alive) or (pacman_was_hit):
        ui_msg_lost()
        game_finished = True
    elif won:
        ui_msg_win()
        game_finished = True

