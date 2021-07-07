from IPython.display import clear_output
from time import sleep

ui_wall = [
    "......",
    "......",
    "......",
    "......"
]

ui_ghost = [
    " .-.  ",
    "| OO| ",
    "|   | ",
    "'^^^' "
]

ui_pacman = [
    " .--. ",
    "/ _.-'",
    "\\  '-.",
    " '--' "
]

ui_empty = [
    "      ",
    "      ",
    "      ",
    "      "
]

ui_pill = [
    "      ",
    " .-.  ",
    " '-'  ",
    "      "
]


def ui_print(map):

    for row in map:
        for piece in range(4):
            for column in row:
                if column == 'G':
                    print(ui_ghost[piece], end='')
                if column == 'P':
                    print(ui_pill[piece], end='')
                if column == '@':
                    print(ui_pacman[piece], end='')
                if column == '.':
                    print(ui_empty[piece], end='')
                if column == '-' or column == '|':
                    print(ui_wall[piece], end='')

            print("")
    clear_output(wait=True)
    sleep(.1)

def ui_key():
    k = input()
    k = int(k)
    return k


def ui_msg_lost():
    print("Pacman died!")


def ui_msg_win():
    print("You won the game!")


