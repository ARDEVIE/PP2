import pygame
from datetime import datetime
import math

RES = WIDTH, HEIGHT = 1500, 800
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2
RADIUS = H_HEIGHT - 50

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

font = pygame.font.SysFont('Verdana', 60)
bg = pygame.image.load('clock.png').convert()
bg_rect = bg.get_rect(center=(H_WIDTH, H_HEIGHT))

radius_list = {
    'sec': RADIUS - 10, 
    'min': RADIUS - 55, 
    'hour': RADIUS - 100
}

clock60 = dict(zip(range(60), range(0, 360, 6)))

def get_clock_pos(angle, length):
    """Вычисляет конечную точку стрелки"""
    x = H_WIDTH + length * math.cos(math.radians(angle) - math.pi / 2)
    y = H_HEIGHT + length * math.sin(math.radians(angle) - math.pi / 2)
    return x, y

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    surface.blit(bg, bg_rect)
    t = datetime.now()


    sec_angle = t.second * 6
    min_angle = t.minute * 6 + t.second * 0.1
    hour_angle = (t.hour % 12) * 30 + t.minute * 0.5


    min_hand = pygame.image.load('min_hand.png')
    sec_hand = pygame.image.load('sec_hand.png')


    min_hand = pygame.transform.rotate(min_hand, -min_angle)
    sec_hand = pygame.transform.rotate(sec_hand, -sec_angle)


    min_rect = min_hand.get_rect(center=(H_WIDTH, H_HEIGHT))
    sec_rect = sec_hand.get_rect(center=(H_WIDTH, H_HEIGHT))


    surface.blit(min_hand, min_rect)
    surface.blit(sec_hand, sec_rect)


    time_render = font.render(f'{t:%H:%M:%S}', True, pygame.Color('white'), pygame.Color('black'))
    surface.blit(time_render, (50, 50))

    pygame.display.flip()
    clock.tick(60)
