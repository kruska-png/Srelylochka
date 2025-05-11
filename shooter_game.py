from pygame import *
from random import randint

font.init()
font1 = font.Font(None, 80)
win = font1.render('YOU WINNER', True, (255, 255, 255))
lose = font1.render('YOU LOSER', True, (180, 0, 0))


font2 = font.Font(None, 36)


game = True


window = display.set_mode((700, 500))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')
 
display.set_caption('Galaxy_defenders')
background = transform.scale(image.load('Black_hole.png'), (700, 500))

lost = 0


img_bullet = "bulllet.png"
img_hero = "rocket.png"
img_enemy = "ufo.png"
score = 0
goal = 10
lost = 0
max_lost = 3
monsters = sprite.Group()
bullets = sprite.Group()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        sprite.Sprite__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= speed
        if keys_pressed[K_d] and self.rect.x  < win_width - 80:
            self.rect.x += speed
        Sprite_x = Player.rect.x
        Sprite_y = Player.rect.y
        Sprite_center_x = Player.rect.centerx
        Sprite_top = Player.rect.top
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1 

        
        monsters.add(monsters)


        


class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed

        if self.rect.y < 0:
            self.kill

        bullets = sprite.Group()
        bullets.add(bullet)
        sprites_list = sprite.spritecollide(
        ship, monsters, False
    )
    sprites_list = sprite.groupcollide(
        monsters, bullets, True, True
    )

win_width = 700
win_height = 500

ship = Player(img_hero, 5, win_height - 100, 80)


for i in range(1, 6):
    monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monsters)
bullets = sprite.Group()
finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run == False

        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                ship.fire()
    
    if not finish:
        window.blit(background, (0, 0))
        
        monsters.update()
        bullets.update()
        ship.update() 


        ship.reset()
        monsters.draw(window)
        bullets.draw(window)

        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score = score + 1
            monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)

        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True

            window.blit(lose, (200, 200))
            

        if score >= goal:
            finish = True
            window.blit(win, (200, 200))
        text = font2.render("Счет: " + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))


        text_lose = font2.render("Пропущено: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))


       


    else:
        finish = False
        score = 0
        lost = 0
        for b in bullets:
            b.kill()
        for m in monsters:
            m.kill()

        time.delay(3000)
        for i in range(1, 6):
            monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)

        
    time.delay(50)

        
