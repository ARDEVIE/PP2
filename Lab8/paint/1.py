import pygame
import random


white = (255, 255, 255)
eraser = (0, 0, 0)  # Цвет для "ластика" (черный)
green = (34, 139, 34)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)

pygame.display.set_caption("Paint")  # Заголовок окна
pygame.display.set_icon(pygame.image.load("paint_icon.png"))  # Иконка окна

def main():
    pygame.init()  # Инициализируем Pygame
    screen = pygame.display.set_mode((640, 480))  # Создаем окно приложения
    clock = pygame.time.Clock()  # Таймер для контроля FPS
    
    radius = 15  # Радиус кисти для рисования
    mode = white  # Текущий выбранный цвет
    last_pos = None  # Последняя позиция курсора для рисования линий
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return  # Завершаем приложение при закрытии окна или нажатии Esc
                
            # Обработка смены цвета при нажатии клавиш
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    mode = red
                elif event.key == pygame.K_g:
                    mode = green
                elif event.key == pygame.K_b:
                    mode = blue
                elif event.key == pygame.K_y:
                    mode = yellow
                elif event.key == pygame.K_BACKSPACE:
                    mode = eraser
                elif event.key == pygame.K_x:
# Генерируем случайный цвет при нажатии 'x'
                    mode = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    
# При нажатии клавиш w и c на клавиатуре рисуются прямоугольник и круг соответственно в позиции курсора мыши с текущим выбранным цветом.
                elif event.key == pygame.K_w:
                    drawRectangle(screen, pygame.mouse.get_pos(), 200, 100, mode)
                elif event.key == pygame.K_c:
                    drawCircle(screen, pygame.mouse.get_pos(), mode)
                    
# При нажатии и перемещении мыши рисуется линия между последней позицией и текущей позицией курсора. Ширина линии и цвет зависят от выбранного режима.
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                last_pos = pygame.mouse.get_pos()
            
            if event.type == pygame.MOUSEMOTION and event.buttons[0] and last_pos:
                drawLineBetween(screen, last_pos, pygame.mouse.get_pos(), radius, mode)
                last_pos = pygame.mouse.get_pos()
                
        pygame.display.flip()
        clock.tick(60)
        
        
        
# drawLineBetween() рисует линию между двумя точками, рассчитывая промежуточные точки и рисуя маленькие круги между ними для создания непрерывной линии.
def drawLineBetween(screen, start, end, width, color_mode):
    color = color_mode
    
# Рассчитывается горизонтальное (dx) и вертикальное (dy) расстояние между начальной и конечной точками.    
    dx = start[0] - end[0]
    dy = start[1] - end[1]

# Определяется количество итераций (шагов) на основе максимального из абсолютных значений dx и dy, чтобы гарантировать плавность линии.    
    iterations = max(abs(dx), abs(dy))

# В цикле для каждой итерации вычисляется прогрессивная позиция между начальной и конечной точками, и на каждом шаге рисуется круг, в результате чего образуется плавная линия.
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)
        
# drawRectangle() рисует прямоугольник с центром в текущем положении курсора. Ширина и высота прямоугольника фиксированы.
def drawRectangle(screen, mouse_pos, w, h, color):
    
# Создается объект Rect с помощью координат курсора, ширины и высоты
    x = mouse_pos[0]
    y = mouse_pos[1]
    rect = pygame.Rect(x, y, w, h)
    
# Используя этот Rect, функция pygame.draw.rect рисует прямоугольник на screen в заданном цвете.
    pygame.draw.rect(screen, color, rect, 3)
    
# drawCircle() рисует круг с центром в текущем положении курсора. Радиус круга фиксирован.
def drawCircle(screen, mouse_pos, color):

# Используя позицию курсора как центр, функция pygame.draw.circle рисует круг заданного цвета и радиуса (100 пикселей в этом примере) на экране. Толщина линии круга задается параметром 3.
    x = mouse_pos[0]
    y = mouse_pos[1]
    pygame.draw.circle(screen, color, (x, y), 100, 3)



main()