import pygame
import random
import sys
import psycopg2

# === ПОДКЛЮЧЕНИЕ К БАЗЕ ===
conn = psycopg2.connect(
    dbname='snake',
    user='postgres',
    password='12345',
    host='localhost'
)
cursor = conn.cursor()

# === ФУНКЦИЯ ДОБАВЛЕНИЯ ПОЛЬЗОВАТЕЛЯ И ЕГО СЧЕТА ===
def insert_user(user_name, score, level):
    sql = """INSERT INTO user_score (user_name, score, level)
             VALUES (%s, %s, %s)
             ON CONFLICT (user_name)
             DO UPDATE SET score = EXCLUDED.score, level = EXCLUDED.level
             RETURNING user_name;"""
    try:
        cursor.execute(sql, (user_name, score, level))
        conn.commit()
        return cursor.fetchone()[0]
    except Exception as error:
        print("Ошибка при сохранении:", error)
        return None

# === НАСТРОЙКА ЭКРАНА ===
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Змейка")

# === ЦВЕТА ===
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# === КЛАСС ЗМЕИ ===
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.player_name = None
        self.paused = False

    def get_player_name(self):
        input_box = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 25, 200, 50)
        font = pygame.font.Font(None, 32)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ''
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            done = True
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            screen.fill(BLACK)
            txt_surface = font.render(text, True, color)
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width
            screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            pygame.draw.rect(screen, color, input_box, 2)
            pygame.display.flip()

        self.player_name = text

    def move(self):
        global score, speed, level
        if not self.paused:
            head = self.body[0]
            x = (head[0] + self.direction[0]) % GRID_WIDTH
            y = (head[1] + self.direction[1]) % GRID_HEIGHT
            new_head = (x, y)
            if new_head in self.body[1:] or new_head in walls:
                snake.save_score(score, level)
                return False
            self.body.insert(0, new_head)
            if new_head == food.position:
                score += 1
                if score % 3 == 0:
                    level += 1
                    speed += 1
                food.spawn()
            else:
                self.body.pop()
        return True

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def save_score(self, score, level):
        result = insert_user(self.player_name, score, level)
        if result:
            print(f"Счет и уровень сохранены для {result}")
        else:
            print("Ошибка при сохранении данных.")

# === КЛАСС ЕДЫ ===
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.weight = 0
        self.timer = 0
        self.spawn()

    def spawn(self):
        while True:
            x = random.randint(1, GRID_WIDTH - 2)
            y = random.randint(1, GRID_HEIGHT - 2)
            if (x, y) not in snake.body and (x, y) not in walls:
                self.position = (x, y)
                self.weight = 20
                self.timer = pygame.time.get_ticks() + 3000
                break

    def update(self):
        if pygame.time.get_ticks() > self.timer:
            self.spawn()

# === СТЕНКИ УРОВНЯ ===
walls = [(0, i) for i in range(GRID_HEIGHT)] + [(GRID_WIDTH - 1, i) for i in range(GRID_HEIGHT)] + \
        [(i, 0) for i in range(GRID_WIDTH)] + [(i, GRID_HEIGHT - 1) for i in range(GRID_WIDTH)]

# === НАЧАЛО ИГРЫ ===
snake = Snake()
snake.get_player_name()
food = Food()
score = 0
level = 0
speed = 7

# === ИГРОВОЙ ЦИКЛ ===
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0, -1))
            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, 1))
            elif event.key == pygame.K_LEFT:
                snake.change_direction((-1, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction((1, 0))
            elif event.key == pygame.K_SPACE:
                snake.paused = not snake.paused
            elif event.key == pygame.K_s:
                snake.save_score(score, level)
            elif event.key == pygame.K_ESCAPE:
                running = False

    if not snake.move():
        running = False

    if not snake.paused:
        for segment in snake.body:
            pygame.draw.rect(screen, WHITE, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        x, y = food.position
        pygame.draw.rect(screen, RED, (x * GRID_SIZE, y * GRID_SIZE, food.weight, food.weight))

        for wall in walls:
            pygame.draw.rect(screen, BLUE, (wall[0] * GRID_SIZE, wall[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    font = pygame.font.SysFont(None, 25)
    text = font.render(f"Счет: {score}   Уровень: {level}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    food.update()
    clock.tick(speed)

pygame.quit()
