import pygame
import random

# Define basic colors and game dimensions
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WALL_COLOR = (226, 135, 67)
LINE_COLOR = (50, 50, 50)
HEIGHT = 400
WIDTH = 400
BLOCK_SIZE = 20
MAX_LEVEL = 2

pygame.display.set_caption("Snake Game")

class Point:
    """Represents a point on the game grid."""
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

class Wall:
    """Represents the walls in the game, loaded from a level file."""
    def __init__(self, level):
        self.body = []
        with open(f"level{level}.txt", "r") as f:
            for y in range(HEIGHT // BLOCK_SIZE + 1):
                for x in range(WIDTH // BLOCK_SIZE + 1):
                    if f.read(1) == '#':
                        self.body.append(Point(x, y))

    def draw(self):
        """Draws the wall on the game screen."""
        for point in self.body:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, WALL_COLOR, rect)

class Food:
    """Represents the food in the game."""
    def __init__(self, snake, walls):
        self.location = self.generate_new_location(snake, walls)

    def generate_new_location(self, snake, walls):
        """Generates a new location for food, ensuring it does not overlap with the snake or walls."""
        while True:
            x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
            y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
            if not any(point.x == x and point.y == y for point in snake.body + walls.body):
                return Point(x, y)

    def draw(self):
        """Draws the food on the game screen."""
        rect = pygame.Rect(BLOCK_SIZE * self.location.x, BLOCK_SIZE * self.location.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, GREEN, rect)

class Snake:
    """Represents the snake in the game."""
    def __init__(self):
        self.body = [Point(10, 11)]
        self.dx = 0
        self.dy = 0
        self.level = 0
        self.score = 0

    def move(self):
        """Moves the snake based on current direction."""
        new_head = Point(self.body[0].x + self.dx, self.body[0].y + self.dy)
        # Check for self collision
        if any(part.x == new_head.x and part.y == new_head.y for part in self.body):
            self.reset()
        self.body.insert(0, new_head)
        self.body.pop()  # Remove the tail unless food is eaten

        # Handle border crossing
        if self.body[0].x * BLOCK_SIZE >= WIDTH:
            self.body[0].x = 0
        elif self.body[0].y * BLOCK_SIZE >= HEIGHT:
            self.body[0].y = 0
        elif self.body[0].x < 0:
            self.body[0].x = WIDTH // BLOCK_SIZE - 1
        elif self.body[0].y < 0:
            self.body[0].y = HEIGHT // BLOCK_SIZE - 1

    def reset(self):
        """Resets the snake to the initial state."""
        self.body = [Point(10, 11)]
        self.dx = 0
        self.dy = 0
        self.level = 0
        self.score = 0

    def draw(self):
        """Draws the snake on the game screen."""
        for index, point in enumerate(self.body):
            color = RED if index == 0 else GREEN
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, color, rect)

    def check_collision(self, food, walls):
        """Checks for collisions with food and walls. Extends the snake and increases score on food collision."""
        if self.body[0].x == food.location.x and self.body[0].y == food.location.y:
            self.body.append(Point(food.location.x, food.location.y))  # Keep tail for growth
            self.score += 1
            return True
        # Check for wall collision
        for wall in walls.body:
            if self.body[0].x == wall.x and self.body[0].y == wall.y:
                self.reset()  # Reset the game on collision
        return False

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    
    snake = Snake()
    walls = Wall(snake.level)
    food = Food(snake, walls)

    while True:
        SCREEN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and snake.dx == 0:
                    snake.dx = 1
                    snake.dy = 0
                if event.key == pygame.K_LEFT and snake.dx == 0:
                    snake.dx = -1
                    snake.dy = 0
                if event.key == pygame.K_UP and snake.dy == 0:
                    snake.dx = 0
                    snake.dy = -1
                if event.key == pygame.K_DOWN and snake.dy == 0:
                    snake.dx = 0
                    snake.dy = 1
        
        snake.move()

        if snake.check_collision(food, walls):
            food = Food(snake, walls)
            if snake.score % 3 == 0 and snake.score > 0:  # Level up condition
                snake.level = (snake.level + 1) % MAX_LEVEL
                walls = Wall(snake.level)
                food = Food(snake, walls)

        walls.draw()
        food.draw()
        snake.draw()
        drawGrid()

        pygame.display.update()
        CLOCK.tick(10 + snake.level * 5)  # Increase speed with level

def drawGrid():
    """Draws the grid lines on the game screen."""
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, LINE_COLOR, rect, 1)

if __name__ == "__main__":
    main()