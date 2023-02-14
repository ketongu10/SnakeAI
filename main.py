import random

from SnakeAI.Memory.Memory import *
from SnakeAI.World.Screen import *
from SnakeAI.World.World import *


def print_hi(name):
    print(f'Hi, {name}')


WORLD = World()
MEMORY = Memory()
SCREEN = Screen()
if __name__ == '__main__':
    WORLD.gen_random_apple(True)
    while WORLD.update_turn():
        SCREEN.setScreeenFromWorld(WORLD)
        MEMORY.set_from_screen(SCREEN)
        MEMORY.time_shift()
        WORLD.move_snake(MEMORY.get_action())
    print(f"Snake has eaten {WORLD.eaten_apples} apples")
