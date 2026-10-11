import random
import sys
import pygame

pygame.init()

WIDTH, HEIGHT = 900, 650
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NeonRush - Prototipo")
clock = pygame.time.Clock()

BLACK = (9, 12, 24)
ROAD = (24, 28, 43)
WHITE = (240, 245, 255)
CYAN = (40, 230, 255)
BLUE = (40, 100, 255)
RED = (255, 65, 90)
ORANGE = (255, 165, 55)
GREEN = (60, 240, 150)
PURPLE = (160, 80, 255)
GRAY = (100, 110, 135)

font = pygame.font.Font(None, 28)
big_font = pygame.font.Font(None, 58)

ROAD_LEFT = 180
ROAD_RIGHT = 720
ROAD_WIDTH = ROAD_RIGHT - ROAD_LEFT
LANE_WIDTH = ROAD_WIDTH //3

ruuning = True
game_over = False
score = 0
spawn_timer = 0
enemy_bullet_timer = 0
road_offset = 0
station = None
station_timer = 0

def draw_text(text, x, y, color=WHITE, font_obj=font):
    image = font_obj.render(str(text), True, color)
    screen.blit(image, (x, y))

