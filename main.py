import pygame
import time
import random

pygame.init()

screen = pygame.display.set_mode((1800, 950))
pygame.display.set_caption('2D Plaformer')

# загрузка персонажа и монетки
character = pygame.image.load('1666265817_39-mykaleidoscope-ru-p-shrek-chelovek-vkontakte-43 (1).jpg')
coin = pygame.image.load('4b809286882144f289d5b04c4d22e140.jpeg')
background = pygame.image.load('i-125-13.jpeg')



# настройка начальных координат
x = 400
y = 300
vx = 0
vy = 0
direction = 'right'

# координаты монет
random.randint(950,1800)
coins = [(random.randint(950,1800), random.randint(200,500)), (random.randint(950,1800), random.randint(100,400)), (random.randint(950,1800),random.randint(100,300)), (random.randint(950,1800), random.randint(250,400))]

# счет
score = 0

# контроль частоты кадров
clock = pygame.time.Clock()

running = True

while running:
    clock.tick(60)

    events = pygame.event.get()

    # работа с событиями
    for event in events:
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                vx = -5
                direction = 'left'

            if event.key == pygame.K_RIGHT:
                vx = 5
                direction = 'right'

            if event.key == pygame.K_UP:
                vy = -10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                vx = 0

    # обновление координат с учетом скорости и гравитации
    x += vx
    y += vy
    vy += 1

    # ограничения на выход за границы карты
    if x < 0:
        x = 0
    if x > 1800:
        x = 1600
    if y < 0:
        y = 20
    if y > 950:
        y = 850

    screen.blit(background, (0, 0))

    # отобразил персонажа
    if direction == 'right':
        screen.blit(character, (x, y))
    else:
        flipped = pygame.transform.flip(character, True, False)
        screen.blit(flipped, (x, y))

    # отобразил монеты
    for coord in coins:
        screen.blit(coin, (coord[0], coord[1]))

    for i, (cx, cy) in enumerate(coins):
        if ((x + 25) - (cx + 25)) ** 2 + ((y + 25) - (cy + 25)) ** 2 < 50 ** 2:
            score += 1
            del coins[i]

    font = pygame.font.SysFont('Arial', 32)
    text = font.render(f"Счет {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # обновление экрана
    pygame.display.flip()

    # если монеты кончились, то закрываем игру
    if len(coins) == 0:
        raise SystemExit