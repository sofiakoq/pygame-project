import pygame
import sys
from pygame.locals import *

from dots_lines import (
    screen_w,
    screen_h,
    FPS,
    BACKGROUND_COLOR,
    Point,
    Line,
    generate_points
)


class Game:
    def __init__(self, num_points):
        self.screen = pygame.display.set_mode((screen_w, screen_h))
        self.clock = pygame.time.Clock()
        self.points = generate_points(num_points)
        self.lines = []
        self.selected_point = None
        self.hovered_point = None

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEMOTION:
                self.hovered_point = None
                for point in self.points:
                    if point.is_hovered(event.pos):
                        self.hovered_point = point
                        break

            if event.type == MOUSEBUTTONDOWN:
                if self.hovered_point:
                    if self.selected_point:
                        if self.selected_point != self.hovered_point:
                            self.selected_point.connected_to = self.hovered_point
                            self.hovered_point.connected_to = self.selected_point
                            self.lines.append(Line(self.selected_point, self.hovered_point))
                            self.selected_point = None
                    else:
                        self.selected_point = self.hovered_point

    def update(self):
        pass

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)

        for line in self.lines:
            line.draw(self.screen)

        for point in self.points:
            point.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(FPS)
    