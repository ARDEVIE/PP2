import pygame, sys

from pygame.locals import *
import random, time

# Инициализируются Pygame и параметры кадров в секунду (FPS).
pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()

# Задаются цвета, используемые в игре.
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 

# Устанавливаются размеры экрана и начальная скорость движения объектов
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 4
SCORE = 0
COINS = 0
 

# Создаются объекты шрифтов для отображения текста "Game Over" и счета.
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over!", True, WHITE)


# Загружается фоновое изображение и устанавливается размер экрана игры.
background = pygame.image.load("AnimatedStreet.png")
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)


pygame.display.set_caption("Race")


# Enemy: класс "врагов" (других автомобилей на дороге), которые движутся сверху вниз. При достижении нижней части экрана, они возвращаются вверх, увеличивая счет игрока на единицу.
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 

    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            
            
# Coin: класс монет, которые игрок может собирать для увеличения своего счета. Монеты также движутся сверху вниз и возвращаются вверх, как только достигают нижней части экрана.
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
    def move(self):
        global COINS
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            COINS += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)      
            
# Player: класс игрока, управляемого автомобиля. Игрок может двигаться влево и вправо по экрану, избегая столкновений с врагами и собирая монеты.
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                   
                   
# Создаются и добавляются в группы спрайты игрока, врагов и монет. 
# Это позволяет управлять ими как единым целым при отрисовке на экране и обработке столкновений.   
P1 = Player()
E1 = Enemy()
COIN = Coin()
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(COIN)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(COIN)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while 1:
# Обработка событий (в том числе увеличение скорости движения объектов и выход из игры).
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
            
# Отрисовка фона, счета и всех спрайтов.
    DISPLAYSURF.blit(background, (0,0))
    score1 = font_small.render(str(SCORE), True, BLACK)
    score2 = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(score1, (10,10))
    DISPLAYSURF.blit(score2, (380,10))
 
# Перемещение всех спрайтов согласно их логике.
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
 
 
# Проверка на столкновения между игроком и врагами или монетами. При столкновении с врагом игра заканчивается, при сборе монеты она исчезает и увеличивает количество монет.
    if pygame.sprite.spritecollideany(P1, enemies):
          time.sleep(0.5) 

          DISPLAYSURF.fill(BLACK)
          DISPLAYSURF.blit(game_over, (30,250))         

          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()  
    if pygame.sprite.spritecollideany(P1, coins):
            for coin in coins:
                coin.kill()
            COINS += 1
            pygame.display.update() 
    
# Если все монеты собраны, создается новая монета.
    if(len(coins) == 0):
        COIN = Coin()
        coins.add(COIN)
        all_sprites.add(COIN)     
        
# После обработки всех событий и логики, экран обновляется, и цикл повторяется.
    pygame.display.update()
    FramePerSec.tick(FPS)