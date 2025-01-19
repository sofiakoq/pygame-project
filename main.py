import sys
import pygame
import random
from game import Game


def main():
    pygame.init()
    game = Game(num_points=random.randint(2, 15))
    game.run()


if __name__ == "__main__":
    main()
