import pygame
import random

size = width, height = 400, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True
# параметра круга

circle_radius = 10

# Пустые списки для координат и скоростей наших кругов
circle = []
speed = []
# Создаем второй холст
screen2 = pygame.Surface(screen.get_size())
# Запускаем окно
while running:
    for event in pygame.event.get():
        screen2 = pygame.Surface(screen.get_size())
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            # Сохраняем полученные координаты
            circle += [(list(event.pos), circle_color)]
            speed.append([0, 1])

    # Чистим второй холст
    screen2.fill(pygame.Color('black'))
    # Перерисовываем круги
    for i in range(len(circle)):
        # Проверяем на столкновение со стенками
        for ext in (0, 1):
            if circle[i][0][ext] >= size[ext] - circle_radius:
                speed[i][ext] = 0
            # Изменяем координаты
            circle[i][0][ext] += speed[i][ext]
        # Рисуем круг
        pygame.draw.circle(screen2, circle[i][1], circle[i][0], circle_radius)

    # Рисуем на экране сохраненное на втором холсте
    screen.blit(screen2, (0, 0))
    pygame.display.flip()
    clock.tick(100)
pygame.quit()
