import pygame
import sys
import time

#主に15章のバルーンをモチーフにした。
FPS = 40

clock = pygame.time.Clock()

WIDTH = 1000
HEIGHT = 600
screen_right = 1000
screen_left = 0
screen_top = 580
screen_bottom = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))

FONT_SIZE = 24

CHARACTER_X = 500
CHARACTER_Y = 400
CHARACTER_DIAM = 45
CHARACTER_JUMP = WIDTH + CHARACTER_DIAM

BOMB_TOP = 18 + screen_top
BOMB_GAP = 35
BOMB_GAP_Y = 20
BOMB_VX = 5
BOMB_DIAM = 20
BOMB_JUMP = WIDTH + BOMB_DIAM + BOMB_GAP
BOMB_LAST_X = BOMB_JUMP + 1
BOMB_STEP = BOMB_DIAM + BOMB_GAP


TREASURE_X = 0
TREASURE_Y = 10
TREASURE_VX = 8
TREASURE_DIAM = 20
TREASURE_JUMP = WIDTH + TREASURE_DIAM

IMG = 'image/'


CHARACTER = 'nurikabe.png'
BOMB = 'bomb.png'
TREASURE = 'takara.png'

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, vx, vy, speed, image):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.vx, self.vy = (vx, vy)
        self.image = pygame.image.load(image)
        self.image = self.image.convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = pygame.Rect(x, y, 40, 60)

    def update(self):
        self.rect.move_ip(self.vx, self.vy)
        if self.rect.x < -CHARACTER_DIAM:
            self.rect.move_ip(CHARACTER_JUMP, 0)
        if self.rect.x > screen_right:
            self.rect.move_ip(-CHARACTER_JUMP, 0)
    def move_left(self):
        self.vx = -self.speed

    def move_right(self):
        self.vx = self.speed

    def move_up(self):
        self.vy = -self.speed

    def move_down(self):
        self.vy = self.speed
    def stop(self):
        self.vx = 0
        self.vy = 0

class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y, d, vx, image):
        pygame.sprite.Sprite.__init__(self)
        self.vx = vx
        self.image = pygame.image.load(image)
        self.image = self.image.convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = pygame.Rect(x, y, 50, d)


    def update(self):
        self.rect.move_ip(self.vx, 0)
        if self.rect.x < -BOMB_DIAM:
            self.rect.move_ip(BOMB_JUMP, 0)
        if self.rect.x > screen_right:
            self.rect.move_ip(-BOMB_JUMP, 0)

class Treasure(pygame.sprite.Sprite):
    def __init__(self, x, y, d, vx, image):
        pygame.sprite.Sprite.__init__(self)
        self.vx = vx
        self.image = pygame.image.load(image)
        self.image = self.image.convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = pygame.Rect(x, y, d, d)

    def update(self):
        self.rect.move_ip(self.vx, 0)
        if self.rect.x < -TREASURE_DIAM:
            self.rect.move_ip(TREASURE_JUMP, 0)
        if self.rect.x > screen_right:
            self.rect.move_ip(-TREASURE_JUMP, 0)

class Board():
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.width, self.height = (width, height)
        self.clock = pygame.time.Clock()

    def setup(self):
        self.player = pygame.sprite.Group()
        self.bombs = pygame.sprite.Group()
        self.treasures = pygame.sprite.Group()

        self.setup_player()
        self.setup_bombs()
        self.setup_treasures()

        self.obj = [self.player, self.bombs, self.treasure]
        self.obj.add = [self.player, self.bombs, self.treasure]

    player = Character(500, 500, 0, 0, 7, IMG + CHARACTER)
    obj = pygame.sprite.Group()
    obj.add(player)

    bombs = pygame.sprite.Group()
    bombs.add(Bomb(10, 0, 60, 6, IMG + BOMB))
    bombs.add(Bomb(240, 0, 60, 6, IMG + BOMB))
    bombs.add(Bomb(550, 0, 60, 6, IMG + BOMB))
    bombs.add(Bomb(740, 0, 60, 6, IMG + BOMB))

    bombs.add(Bomb(0, 80, 60, 5, IMG + BOMB))
    bombs.add(Bomb(170, 80, 60, 5, IMG + BOMB))
    bombs.add(Bomb(250, 80, 60, 5, IMG + BOMB))
    bombs.add(Bomb(330, 80, 60, 5, IMG + BOMB))
    bombs.add(Bomb(410, 80, 60, 5, IMG + BOMB))
    bombs.add(Bomb(580, 80, 60, 5, IMG + BOMB))
    bombs.add(Bomb(660, 80, 60, 5, IMG + BOMB))
    bombs.add(Bomb(740, 80, 60, 5, IMG + BOMB))
    bombs.add(Bomb(900, 80, 60, 5, IMG + BOMB))
    bombs.add(Bomb(990, 80, 60, 5, IMG + BOMB))

    bombs.add(Bomb(0, 170, 60, 4, IMG + BOMB))
    bombs.add(Bomb(200, 170, 60, 4, IMG + BOMB))
    bombs.add(Bomb(450, 170, 60, 4, IMG + BOMB))
    bombs.add(Bomb(670, 170, 60, 4, IMG + BOMB))
    bombs.add(Bomb(900, 170, 60, 4, IMG + BOMB))

    bombs.add(Bomb(100, 280, 60, 3, IMG + BOMB))
    bombs.add(Bomb(200, 280, 60, 3, IMG + BOMB))
    bombs.add(Bomb(300, 280, 60, 3, IMG + BOMB))
    bombs.add(Bomb(400, 280, 60, 3, IMG + BOMB))
    bombs.add(Bomb(600, 280, 60, 3, IMG + BOMB))
    bombs.add(Bomb(700, 280, 60, 3, IMG + BOMB))
    bombs.add(Bomb(800, 280, 60, 3, IMG + BOMB))
    bombs.add(Bomb(900, 280, 60, 3, IMG + BOMB))

    bombs.add(Bomb(0, 430, 60, 1, IMG + BOMB))
    bombs.add(Bomb(250, 430, 60, 1, IMG + BOMB))
    bombs.add(Bomb(550, 430, 60, 1, IMG + BOMB))
    bombs.add(Bomb(800, 430, 60, 1, IMG + BOMB))
    obj.add(bombs)

    treasures = pygame.sprite.Group()
    treasures.add(Treasure(30, 15, 30, 0, IMG + TREASURE))
    treasures.add(Treasure(800, 180, 30, 0, IMG + TREASURE))
    treasures.add(Treasure(300, 370, 30, 0, IMG + TREASURE))
    obj.add(treasures)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_left()
                if event.key == pygame.K_RIGHT:
                    player.move_right()
                if event.key == pygame.K_UP:
                    player.move_up()
                if event.key == pygame.K_DOWN:
                    player.move_down()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.stop()
                if event.key == pygame.K_RIGHT:
                    player.stop()
                if event.key == pygame.K_UP:
                    player.stop()
                if event.key == pygame.K_DOWN:
                    player.stop()

        collided = []
        for bomb in bombs:
            if bomb.rect.colliderect(player.rect):
                collided.append(bomb)
        for bomb in collided:
            pygame.quit()
        collided = []
        for treasure in treasures:
            if treasure.rect.colliderect(player.rect):
                collided.append(treasure)
        for t in collided:
            treasures.remove(t)
            t.kill()
        if len(treasures) == 0:
            time.sleep(2)
            pygame.quit()

        obj.update()
        obj.draw(screen)
        pygame.display.flip()
        screen.fill((0, 0, 0))
        clock.tick(FPS)
