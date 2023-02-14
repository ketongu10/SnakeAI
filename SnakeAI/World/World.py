from random import random as rnd


class World:

    def __init__(self):
        self.apple_pos = -1
        self.poisoned_apple_pos = -1
        self.snake_pos = 100
        self.eaten_apples = 0
        self.poisoned_apple_time = 0
        self.turn = 0

    def update_turn(self):
        self.turn += 1
        if self.poisoned_apple_pos >= 0:
            self.poisoned_apple_time += 1
        if self.poisoned_apple_time > 20:
            self.gen_random_apple(True)
        if self.snake_pos < 0:
            raise Exception(f"Snake left the World on {self.turn} turn")
        if self.snake_pos == self.poisoned_apple_pos:
            print(f"Snake got dead on {self.turn} turn")
            return False
        if self.snake_pos == self.apple_pos:
            self.eaten_apples += 1
            self.gen_random_apple(False)
            return True
        return True

    def gen_random_apple(self, should):
        if rnd() < 0.5 or should:
            while self.snake_pos == self.apple_pos or self.apple_pos < 0:
                self.apple_pos = int(rnd()*50)
                self.poisoned_apple_pos = -1
                self.poisoned_apple_time = 0
            print(self.apple_pos, self.poisoned_apple_pos)
        else:
            while self.snake_pos == self.poisoned_apple_pos or self.poisoned_apple_pos < 0:
                self.poisoned_apple_pos = int(rnd()*50)
                self.apple_pos = -1
            print(self.apple_pos, self.poisoned_apple_pos)

    def move_snake(self, action):
        """action is one of {-1, 0, 1}"""
        self.snake_pos+=action