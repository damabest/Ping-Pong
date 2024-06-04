from pygame import *
from random import randint

window = display.set_mode((700, 500))
display.set_caption('Pong')
background = transform.scale(image.load('Mortal_Kombat.jpg'), (700, 500))
FPS = 360

font.init()
font1 = font.SysFont('Arial', 25)
scored = font1.render('Score', True, (255,255,255))
missed = font1.render('Missed', True, (255,255,255))

font2 = font.SysFont('Arial', 70)
win = font2.render('YOU WIN', True, (0,255,0))
lose = font2.render('YOU LOSE', True, (255,0,0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, win_width, win_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (win_width, win_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 395:
            self.rect.y += self.speed

racket_left = Player('bamboo_1.png', 600, 200, 10, 100, 100)
racket_right = Player('bamboo.png', 0, 200, 10, 100, 100)
bomb = Player('dynamite.png', 325, 200, 10, 50, 50)

dx = 4
dy = 4

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))
        
        racket_left.reset()
        racket_left.update_l()
        racket_right.reset()
        racket_right.update_r()
        bomb.update()
        bomb.reset()

        bomb.rect.x += dx
        bomb.rect.y += dy

        if bomb.rect.y > 450:
            dy *= -1
        
        if bomb.rect.y < 0:
            dy *= -1

        if bomb.rect.x > 600:
            bomb.rect.center
            dy *= -1
        

    display.update()
    time.delay(50)