import sys
import pygame

from game import Game


def main():
    pygame.init()
    game = Game(num_points=4)
    game.run()


if __name__ == "__main__":
    main()