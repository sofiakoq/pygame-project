import math
import pygame


screen_w = 800
screen_h = 600
FPS = 60
POINT_RADIUS = 15
LINE_THICKNESS = 3
FONT_SIZE = 24
BACKGROUND_COLOR = (20, 20, 20)
POINT_COLOR = (255, 255, 255)
LINE_COLOR = (200, 200, 200)
TEXT_COLOR = (255, 255, 255)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.connected_to = None

    def draw(self, surface):
        pygame.draw.circle(surface, POINT_COLOR, (int(self.x), int(self.y)), POINT_RADIUS)

    def is_hovered(self, mouse_pos):
        distance = math.sqrt((mouse_pos[0] - self.x) ** 2 + (mouse_pos[1] - self.y) ** 2)
        return distance <= POINT_RADIUS


class Line:
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, surface):
        pygame.draw.line(
            surface,
            LINE_COLOR,
            (self.point_a.x, self.point_a.y),
            (self.point_b.x, self.point_b.y),
            LINE_THICKNESS
        )


def generate_points(num_points):
    points = []
    spacing = screen_w // (num_points + 1)
    for i in range(num_points):
        x = spacing * (i + 1)
        y = screen_h // 2
        points.append(Point(x, y))
    return points