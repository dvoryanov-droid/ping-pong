from pygame import *
from random import randint


win = display.set_mode((700, 500))
display.set_caption('Пинг-Понг')
clock = time.Clock()
FPS = 60
bg = (100, 200, 200)

class GameSprite(sprite.Sprite):
    def __init__(self, hero_image, hero_x, hero_y, hero_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(hero_image), (20, 100))
        self.speed = hero_speed
        self.rect = self.image.get_rect()
        self.rect.x = hero_x
        self.rect.y = hero_y

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

player_1 = Player('rocet_pong_1.png', 30, 200, 5)
player_2 = Player('rocet_pong_1.png', 650, 200, 5)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            
    win.fill(bg)


    player_1.update_l()
    player_2.update_r()

    player_1.reset()
    player_2.reset()

    display.update()
    clock.tick(FPS)