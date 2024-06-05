from pygame import *
from random import randint

window = display.set_mode((700, 500))
display.set_caption('Pong')
background = transform.scale(image.load('Mortal_Kombat.jpg'), (700, 500))
FPS = 360

mixer.init()
mixer.music.load('Epic.ogg')
mixer.music.play()
mixer.music.set_volume(0.5)

font.init()

font2 = font.SysFont('Arial', 70)

player_1 = font2.render('Left Player WINS', True, (0,255,0))
player_2 = font2.render('Right Player WINS', True, (0,255,0))

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

racket_left = Player('bamboo_1.png', 600, 200, 10, 50, 100)
racket_right = Player('bamboo.png', 0, 200, 10, 50, 100)
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

        if sprite.collide_rect(racket_right, bomb) or sprite.collide_rect(racket_left, bomb):
            dx *= -1

        if bomb.rect.x > 700:
            finish = True
            window.blit(player_1, (125,200))
        
        if bomb.rect.x < 0:
            finish = True
            window.blit(player_2, (125,200))
        
    else:
        finish = False

        bomb.rect.x = 325
        bomb.rect.y = 200

        time.delay(5000)


    display.update()
    time.delay(50)
