from game import start_screen, lose_screen, final_screen
from dots_lines import create_level
import pygame
import sys
from constants import screen, WHITE, BLACK, WIDTH, font, BLUE, RED

pygame.init()

def main():
    level_count = 0
    start_screen()
    running = True
    while running:
        level = create_level()
        level_running = True
        while level_running:
            screen.fill(WHITE)
            level.draw()

            text = font.render(f"Уровень: {level_count}", True, BLACK)
            screen.blit(text, (10, 10))

            skip_button = pygame.Rect(WIDTH - 200, 10, 180, 40)
            pygame.draw.rect(screen, BLUE, skip_button)
            text = font.render("Пропустить", True, WHITE)
            screen.blit(text, (WIDTH - 190, 20))

            restart_button = pygame.Rect(WIDTH - 200, 60, 180, 40)
            pygame.draw.rect(screen, RED, restart_button)
            text = font.render("Заново", True, WHITE)
            screen.blit(text, (WIDTH - 190, 70))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if skip_button.collidepoint(pos):
                        level_running = False  
                    elif restart_button.collidepoint(pos):
                        for point in level.points:
                            point.connected_to = None
                        level.connections.clear()
                    else:
                        for point in level.points:
                            if point.is_clicked(pos):
                                if level.selected_point is None:
                                    level.selected_point = point
                                else:
                                    point1 = level.selected_point
                                    point2 = point
                                    if point1 != point2 and point1.connected_to is None and point2.connected_to is None:
                                        point1.connected_to = point2
                                        point2.connected_to = point1
                                        level.connections.append((point1, point2))
                                        if level.check_intersections():
                                            lose_screen()
                                            level_count = 0  
                                            level = create_level()  
                                    level.selected_point = None

            if level.check_win() and not level.check_intersections():
                level_running = False
                level_count += 1  

            pygame.display.flip()

        if level_count >= 5: 
            final_screen(level_count)
            running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
