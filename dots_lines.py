import pygame
import random

pygame.init()
from constants import screen, BLACK, WIDTH, BLUE, RED, HEIGHT
from game import distance

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.display.set_caption("Головоломка 'Соедини точки'")
font = pygame.font.Font(None, 36)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.connected_to = None
        self.selected = False

    def draw(self):
        color = RED if self.selected else BLACK
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)

    def is_clicked(self, pos):
        return (self.x - self.radius <= pos[0] <= self.x + self.radius) and \
               (self.y - self.radius <= pos[1] <= self.y + self.radius)

class Level:
    def __init__(self, points):
        self.points = points
        self.connections = []
        self.selected_point = None  

    def draw(self):
        for point in self.points:
            point.draw()
        for connection in self.connections:
            pygame.draw.line(screen, BLACK, (connection[0].x, connection[0].y), (connection[1].x, connection[1].y), 2)
        if self.selected_point:
            mouse_pos = pygame.mouse.get_pos()
            pygame.draw.line(screen, BLUE, (self.selected_point.x, self.selected_point.y), mouse_pos, 2)

    def check_win(self):
        for point in self.points:
            if point.connected_to is None:
                return False
        return True

    def check_intersections(self):
        for i in range(len(self.connections)):
            for j in range(i + 1, len(self.connections)):
                if do_lines_intersect(self.connections[i], self.connections[j]):
                    return True
        return False

def do_lines_intersect(line1, line2):
    def ccw(A, B, C):
        return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)
    
    A, B = line1[0], line1[1]
    C, D = line2[0], line2[1]
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

def create_level():
    num_points = random.randint(4, 8)  
    if num_points % 2 != 0:
        num_points += 1
    
    points = []
    min_distance = 30  
    margin_x = 250  
    margin_y = 80  
    
    while len(points) < num_points:
        x = random.randint(margin_x, WIDTH - margin_x)
        y = random.randint(margin_y, HEIGHT - margin_y)
        
        new_point = Point(x, y)
        
        valid_position = all(distance(p, new_point) > min_distance for p in points)
        
        button_skip = pygame.Rect(WIDTH - 200, 10, 180, 40)
        button_restart = pygame.Rect(WIDTH - 200, 60, 180, 40)
        label_rect = pygame.Rect(10, 10, 150, 40)
        
        if valid_position and not button_skip.collidepoint(x, y) and not button_restart.collidepoint(x, y) and not label_rect.collidepoint(x, y):
            points.append(new_point)
            
    return Level(points)
