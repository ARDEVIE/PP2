import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
done = False
is_blue = True
x = 50
y = 50

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3 if y > 25 else 0
        if pressed[pygame.K_DOWN]: y += 3 if y < 375 else 0
        if pressed[pygame.K_LEFT]: x -= 3 if x > 25 else 0
        if pressed[pygame.K_RIGHT]: x += 3 if x < 375 else 0
        
        screen.fill((255, 255, 255))
        if is_blue: color = ("red")
        else: color = ("red")
        
        pygame.draw.circle(screen, color, (x, y), 25)
        
        pygame.display.flip()
        clock.tick(60)