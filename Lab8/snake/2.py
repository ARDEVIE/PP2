import pygame
from pygame.math import Vector2

import random 



class Snake:
    def __init__(self):
        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)]
    # self.body: 
    # Список из объектов Vector2, определяющих сегменты тела змейки. 
    # Змейка начинает игру с тремя сегментами на определённых позициях.
    
        self.eated = False
    # self.eated: 
    # Булево значение, указывающее, съела ли змейка еду. 
    # При значении True змейка должна увеличиться в размере.
    
        self.isDead = False
    # self.isDead: 
    # Булево значение, указывающее, жива ли змейка. 
    # Если True, игра заканчивается.

    def drawingSnake(self):
    # Проходит по каждому сегменту тела змейки и рисует его на экране в виде прямоугольника зелёного цвета.
        for block in self.body:
            body_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (0 , 128 ,0), body_rect)

    def snakeMoving(self):
        if self.eated == True:
    # Если змейка съела еду (self.eated == True), к телу добавляется новый сегмент в начале, эмулируя рост.
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + direction)
            self.body = body_copy[:]
            self.eated = False
        else:
    # Если змейка не съела еду, она просто двигается вперёд, теряя последний сегмент тела и добавляя новый в направлении движения.
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + direction)
            self.body = body_copy[:]
    # Направление движения определяется внешней переменной direction, которая не описана в данном фрагменте кода.

class Fruit:
    def __init__(self):
        self.randomize()
    # __init__: Конструктор класса вызывает метод randomize, который задаёт случайную позицию фрукта на игровом поле.
    
    def drawingFruit(self):
    # drawingFruit: Метод рисует фрукт на экране. Он создаёт прямоугольник (pygame.Rect) на основе позиции фрукта, а затем отображает изображение фрукта (apple) в этом прямоугольнике.
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        screen.blit(apple, fruit_rect)

    def randomize(self):
    # randomize: 
    # Метод задаёт случайные координаты x и y для фрукта в пределах игрового поля, 
    # исключая крайние границы, и сохраняет эти координаты в атрибуте pos в виде объекта Vector2.
        self.x = random.randint(0, cell_number - 2)
        self.y = random.randint(0, cell_number - 2)
        self.pos = Vector2(self.x, self.y)

class Game:
    def __init__(self):
    # __init__: Конструктор инициализирует змейку (self.snake), фрукт (self.fruit), уровень (self.level) и скорость змейки (self.snake_speed).
        self.snake = Snake()
        self.fruit = Fruit()
        self.level = 1
        self.snake_speed = 10

    def update(self):
    # update: Метод обновляет состояние игры, двигая змейку и проверяя на столкновения с фруктом через checkCollision.
        self.snake.snakeMoving()
        self.checkCollision()

    def drawElements(self):
    # drawElements: Метод отвечает за отрисовку всех элементов игры: змейки и фрукта, а также отображение счёта.
        self.snake.drawingSnake()
        self.fruit.drawingFruit()
        self.scoreDrawing()
    
    def checkCollision(self):
    # checkCollision: 
    # Проверяет, съела ли змейка фрукт. Если голова змейки (self.snake.body[0]) находится на той же позиции, что и фрукт, 
    # змейка увеличивается (self.snake.eated = True), фрукт перемещается на новую позицию, 
    # и вызывается метод levelAdding для возможного увеличения уровня.
        if(self.fruit.pos == self.snake.body[0]):
            self.snake.eated = True
            self.fruit.randomize()
            self.levelAdding()

    def gameOver(self):
    # gameOver: 
    # Проверяет условия проигрыша, такие как столкновение змейки с границами поля или с самой собой. 
    # Возвращает True, если игра должна закончиться.
        #бьется на границы
        if self.snake.body[0].x >= 19:
            return True
        if self.snake.body[0].x <= 0:
            return True
        if self.snake.body[0].y >= 19:
            return True
        if self.snake.body[0].y <= 0:
            return True
        
        #бьется об саму себя
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                return True
        return False
    
    def levelAdding(self):
    # levelAdding: Увеличивает уровень и скорость змейки, если длина тела змейки (за вычетом начальной длины) кратна 3.
        if(len(self.snake.body) - 3) % 3 == 0:
            self.level += 1
            self.snake_speed += 1
    
    def scoreDrawing(self):
    # scoreDrawing: 
    # Отображает текущий счёт и уровень игры на экране. 
    # Использует pygame.font для создания текста счёта и уровня и отображает эти значения на экране.
        score_text = "Score: " + str(len(self.snake.body) - 3)
        score_surface = font.render(score_text, True, (56, 74, 12))
        score_rect = score_surface.get_rect(center = (cell_size * cell_number - 120, 40))
        screen.blit(score_surface, score_rect)

        level_text = "Level: " + str(self.level)
        level_surface = font.render(level_text, True, (56, 74, 12))
        level_rect = level_surface.get_rect(center = (cell_size * cell_number - 120, 70))
        screen.blit(level_surface, level_rect)



pygame.init()
clock = pygame.time.Clock()
cell_size = 40
cell_number = 20
direction = Vector2(1, 0)
# cell_size, cell_number, direction: 
# Определяют размер ячейки, количество ячеек и начальное направление движения змейки соответственно.
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
done = False

apple = pygame.image.load('apple.png').convert_alpha()
apple = pygame.transform.scale(apple, (35, 35))

font = pygame.font.Font('font.ttf', 25)


game = Game()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if direction.x != -1:
                direction = Vector2(1, 0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if direction.x != 1:
                direction = Vector2(-1, 0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if direction.y != 1:
                direction = Vector2(0, -1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if direction.y != -1:
                direction = Vector2(0, 1)

    if(game.gameOver() == True):
        done = True
    
        
    screen.fill((0, 0, 0))
    game.drawElements()
    game.update()
    pygame.display.flip()
    clock.tick(game.snake_speed)

pygame.quit()