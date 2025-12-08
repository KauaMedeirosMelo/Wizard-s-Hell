from pplay import sprite
import random, math
from datetime import datetime
import entity
from resacc import res_access
import toolbar
#from toolbar import exp, exp_change, score, game_timer

def generate_enemies(screen, res_access, N):
    random.seed(str(datetime.now()))
    for i in range(N):
        my_sprite = sprite.Sprite(res_access+"enemy1.png")
        UD = random.randint(0, 1)
        LF = random.randint(0, 1)

        if(UD):
            posX = random.randint(int(screen.width*(8/9)), screen.width)
        else:
            posX = random.randint(0, int(screen.width*(1/9)))

        if(LF):
            posY = random.randint(int(screen.height*(8/9)), screen.height)
        else:
            posY = random.randint(0, int(screen.height*(1/9)))

        entity.enemies.append(Enemy(posX, posY, my_sprite))
        entity.enemies[-1].set_move(screen.width/2, screen.height/2)
        entity.enemies[-1].life = int(toolbar.game_timer[0]/240) + 1
        entity.enemies[-1].speed = 10+(math.log2(toolbar.game_timer[0]/64+1))
        

    return


class Enemy():

    stats = []

    def __init__(self, x, y, sprite):
        sprite.x = x
        sprite.y = y

        self.x = x
        self.y = y
        self.sprite = sprite
        self.life = 1
        self.die = False


    def set_move(self, endX, endY):
        distance = ((self.x - endX)**2 + (self.y - endY)**2)**(1/2)
        if(distance > 0):
            dot_product = (abs(self.x - endX) * 1)
            if(self.x > endX):
                angle = math.acos(dot_product/((distance)))
            else:
                angle = math.acos(dot_product/(distance*-1))
            dir = 1
            if(self.y > endY):
                dir = -1
            
            self.angle = angle
            self.dir = dir
            self.speed = 10

    def move(self, dt):
        self.x = self.x - math.cos(self.angle)*self.speed*dt
        self.y = self.y + math.sin(self.angle)*self.speed*self.dir*dt
        self.sprite.x = self.x
        self.sprite.y = self.y

    def collision(self):
        global score, exp
        for i in range(len(entity.towers)):
            for j in range(len(entity.towers[i])):
                if(self.sprite.collided(entity.towers[i][j].sprite)):
                    self.life -= 1
                    toolbar.exp[0] -= 30
                    toolbar.score[0] = int(score[0]*8/10)
                for k in entity.towers[i][j].bullets:
                    distance = ((self.x - k.x)**2 + (self.y - k.y)**2)**(1/2)
                    if(distance < 20+k.size):
                        self.life -= 1
                        k.life -= 1
                        toolbar.exp[0] += 15/toolbar.exp_change[0]
                        toolbar.score[0] += int(10*toolbar.exp_change[0])
        pass

    def tick(self, dt):
        self.move(dt)
        self.collision()
        if(self.life <= 0):
            self.die = True
        pass

    def render(self):
        self.sprite.draw()
        pass