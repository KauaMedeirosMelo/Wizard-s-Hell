from pygame import draw, surface, SRCALPHA
from pplay import sprite
import entity
from resacc import res_access
import random as rand
import math, datetime

def start_towers(screen, res_access):
    for i in range(3):
        for j in range(3):
            my_sprite = sprite.Sprite(res_access+"torre1.png")
            posX = (screen.width - my_sprite.width*1.5)/2 + my_sprite.width*(i-1)*1.5
            posY = (screen.height - my_sprite.height)/2 + my_sprite.height*(j-1)*1.5
            entity.towers[i][j] = Tower(posX , posY, my_sprite)
    return

def release_bullets():
    for i in range(len(entity.towers)):
        for j in range(len(entity.towers[i])):
            for k in entity.towers[i][j].bullets:
                if(k.selected):
                    k.selected = False
    return

def select_bullets(posX1, posY1, posX2, posY2):
    for i in range(len(entity.towers)):
        for j in range(len(entity.towers[i])):
            for k in range(len(entity.towers[i][j].bullets)):
                #INICIO DO TRATAMENTO DAS BALAS
                if((not entity.towers[i][j].bullets[k].selected) and (not entity.towers[i][j].bullets[k].moving)):
                    if(min(posX1,posX2) <= entity.towers[i][j].bullets[k].x[0] <= max(posX1,posX2)):
                        if(min(posY1,posY2) <= entity.towers[i][j].bullets[k].y[0] <= max(posY1,posY2)):
                            entity.towers[i][j].bullets[k].selected = True

    return

def aim_bullets(posX1, posY1, posX2, posY2):
    distance = ((posX1 - posX2)**2 + (posY1 - posY2)**2)**(1/2)
    if(distance > 0):
        dot_product = (abs(posX1 - posX2) * 1)
        if(posX1 > posX2):
            angle = math.acos(dot_product/((distance)))
        else:
            angle = math.acos(dot_product/(distance*-1))
        dir = 1
        if(posY2 > posY1):
            dir = -1
        for i in range(len(entity.towers)):
            for j in range(len(entity.towers[i])):
                for k in range(len(entity.towers[i][j].bullets)):
                    if(entity.towers[i][j].bullets[k].selected):
                        entity.towers[i][j].bullets[k].dir = dir
                        entity.towers[i][j].bullets[k].set_move(angle, (distance*4000)**(1/2) * entity.towers[i][j].speed)
        
    release_bullets()
    return


class Tower():

    def __init__(self, x, y, sprite):
        sprite.x = x
        sprite.y = y
        self.x = x
        self.y = y
        self.sprite = sprite

        self.reload = 0
        self.cooldown = 4
        self.max_bullets = 3

        self.size = 5
        self.speed = 0.8

        self.stats = []
        self.bullets = []

        self.auto_shoot = False


    def collision(self, obj):
        if(self.sprite.collided(obj)):
            return True
        return False

    def tick(self, mouse, dt):
        self.reload+=dt
        if(self.reload >= self.cooldown):
            if(len(self.bullets) < self.max_bullets):
                self.reload = rand.randint(-8, 0)/10
                self.generate_bullet()

        if(self.collision(mouse)):
            pass
        
        i = 0
        while(i < len(self.bullets)):
            self.bullets[i].tick(dt)
            if(self.bullets[i].die):
                self.bullets.pop(i)
                i-=1
            i+=1

        pass

    def render(self, screen):
        self.sprite.draw()

        for i in self.bullets:
            i.render(screen)

        pass

    def generate_bullet(self):
        bX = self.x + rand.randint(-20, 60)
        bY = self.y + rand.randint(-20, 60)
        self.bullets.append(Bullet(bX, bY, self.size, self.stats))
        if(self.auto_shoot):
            rand.seed(str(datetime.datetime.now()))
            n = rand.randint(0, len(entity.enemies)-1)
            posX1 = self.bullets[-1].x[-1]
            posY1 = self.bullets[-1].y[-1]
            posX2 = entity.enemies[n].x
            posY2 = entity.enemies[n].y
            distance = ((posX1 - posX2)**2 + (posY1 - posY2)**2)**(1/2)
            if(distance > 0):
                dot_product = (abs(posX1 - posX2) * 1)
                if(posX1 > posX2):
                    angle = math.acos(dot_product/((distance)))
                else:
                    angle = math.acos(dot_product/(distance*-1))
                dir = 1
                if(posY2 > posY1):
                    dir = -1
            self.bullets[-1].dir = dir
            self.bullets[-1].set_move(angle, (distance*100)**(1/5) * self.speed*20)
        pass


class Bullet():

    stats = []
    die = False
    dir = 1
    moving = False
    selected = False
    

    def __init__(self, x, y, size, stats):
        self.x = []
        self.y = []

        self.orbX = x - 500
        self.orbY = y - 350

        self.x.append(x)
        self.y.append(y)
        
        self.life = 1

        self.size = size
        self.stats = stats


        self.linear = True
        self.orbit_timer = 0

    def set_move(self, angle, speed):
        self.angle = angle
        self.speed = speed
        self.moving = True
        self.signal = self.dir/abs(self.dir)
        print(self.signal)

    def move(self, dt):
        if(self.linear):
            if(len(self.x) < math.log2(self.speed) - 8):
                self.x.append(self.x[-1])
                self.y.append(self.y[-1])

                self.x[-1] = self.x[-2] - math.cos(self.angle)*self.speed/20
                self.y[-1] = self.y[-2] - math.sin(self.angle)*self.speed*self.dir/20
            else:
                for i in range(len(self.x)):
                    self.x[i] = self.x[i] + math.cos(self.angle)*self.speed*dt
                    self.y[i] = self.y[i] + math.sin(self.angle)*self.speed*self.dir*dt
        
        elif(self.orbit_timer >= 0.3):
            valX = self.orbX
            valY = self.orbY
            
            mydt = dt * math.log2(self.speed/100) * self.signal

            cX = (math.cos(mydt)*valX - math.sin(mydt)*valY)
            cY = (math.cos(-mydt)*valY + math.sin(mydt)*valX)

            self.x[-1] += cX - self.orbX
            self.y[-1] += cY - self.orbY
            self.orbX = cX
            self.orbY = cY
            
        else:
            self.orbit_timer = self.orbit_timer + dt

            cX = self.orbX + math.cos(self.angle)*self.speed*dt
            cY = self.orbY + math.sin(self.angle)*self.speed*self.dir*dt

            self.x[-1] += cX - self.orbX
            self.y[-1] += cY - self.orbY
            self.orbX = cX
            self.orbY = cY



    def tick(self, dt):
        if(self.moving):
            self.move(dt)
        if(self.linear):
            if(self.x[0] < -50 or self.x[0] > 1300 or self.y[0] < -50 or self.y[0] > 1300):
                self.die = True
        elif(self.life <= 0):
            self.die = True
    
    def render(self, screen):
        if(self.selected):
            draw.circle(screen.get_screen(), (255, 255, 255), (self.x[0], self.y[0]), self.size + 2)
        if(not self.moving or self.linear):
            for i in range(len(self.x)):
                #draw.circle(screen.get_screen(), (0, 0, 255), (self.x[i], self.y[i]), self.size)
                circle_surface = surface.Surface((self.size*2, self.size*2), SRCALPHA)
                draw.circle(circle_surface, (0, 0, 250, 255/(i+1)), (self.size, self.size), self.size)
                screen.screen.blit(circle_surface, (self.x[i]-self.size, self.y[i]-self.size))
        else:
            draw.circle(screen.get_screen(), (0, 0, 250), (screen.width/2 + self.orbX, screen.height/2 + self.orbY), self.size)
