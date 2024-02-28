import pygame as pg

import constants as c
from enemy import Enemy


# initialise gane
pg.init()

clock = pg.time.Clock()

# create game window
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower defense")


# load images
enemy_image = pg.image.load('./assets/images/enemies/enemy_1.png').convert_alpha()

# create groups
enemy_group = pg.sprite.Group()


waypoints = [
    (100, 100),
    (400, 200),
    (400, 100),
    (200, 300),
]


enemy = Enemy(waypoints=waypoints, image=enemy_image)
enemy_group.add(enemy)


# game loop
run = True

while run:

    clock.tick(c.FPS)

    # draw background
    screen.fill((200,200,200))

    # draw enemy path
    pg.draw.lines(screen, (30,30,30), False, waypoints)

    enemy.update()

    # draw groups
    enemy_group.draw(screen)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.flip()


pg.quit()
