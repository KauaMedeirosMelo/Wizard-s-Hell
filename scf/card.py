from pplay import sprite, sound
import toolbar, entity
import random

cards = None

types = None

set_stat = None
stat = None

texts = None
show_select = None
show_applied = None

timer = 2

def init():
    global show_select, show_applied, cards, types, set_stat, stat, texts, timer

    cards = []

    types = ["size", "speed", "cooldown", "orbit", "auto"]

    set_stat = False
    stat = None

    texts = ["Selecione uma carta", "Upgrade aplicado a todas as torres!"]
    show_select = False
    show_applied = False

    timer = 2

def render(screen):
    global show_applied, timer

    for i in cards:
        i.render(screen)

    if(show_select):
        screen.draw_text(texts[0], (screen.width - len(texts[0])*10)/2, screen.height - 50, 30, (255,255,255))
    elif(show_applied):
        screen.draw_text(texts[1], (screen.width - len(texts[1])*10)/2, screen.height - 50, 30, (255,255,255))

def tick(screen, res_access, mouse_mask, dt):
    global show_applied, timer

    for i in cards:
        i.tick(mouse_mask, dt)

    if(show_applied):
        timer-=dt
        if(timer < 0):
            show_applied = False
            timer = 2

def new_cards(screen, res_access, sound_access):
    toolbar.exp[0] = toolbar.exp[0]/2
    toolbar.exp_change[0] += 0.15

    for i in range(3):
        t = 0
        card_type = random.randint(0, 10)
        card_sound = sound.Sound(sound_access+"card.wav")
        if(card_type > 8):
            t = random.randint(3, 4)
            my_sprite = sprite.Sprite(res_access+types[t]+"_card.png")
            cards.append(Card(my_sprite, card_sound, screen.width - my_sprite.width*1.25, 20 + my_sprite.height*i*1.2, types[t], False))
            pass
        else:
            t = random.randint(0, 2)
            my_sprite = sprite.Sprite(res_access+types[t]+"_card.png")
            cards.append(Card(my_sprite, card_sound, screen.width - my_sprite.width*1.25, 20 + my_sprite.height*i*1.2, types[t], True))
            pass


    return

def release_cards():
    while(len(cards) != 0):
        cards.pop(0)

class Card():

    def __init__(self, sprite, sound, x, y, type, stat):
        self.x = x
        self.y = y
        sprite.x = x
        sprite.y = y
        self.sprite = sprite
        self.sound = sound
        self.stat = stat

        self.type = type

    def collision(self, obj):
        if(self.sprite.collided(obj)):
            return True

    def tick(self, mouse_mask, dt):
        global set_stat, stat, show_select, show_applied
        if(toolbar.click):
            if(self.collision(mouse_mask)):
                self.sound.play()
                if(self.stat):
                    for i in range(len(entity.towers)):
                        for j in range(len(entity.towers[i])):
                            setattr(entity.towers[i][j], self.type, getattr(entity.towers[i][j], self.type) *1.2)
                            show_applied = True
                else:
                    set_stat = True
                    stat = self.type
                    show_select = True
                    pass
                release_cards()

        pass

    def render(self, screen):
        global show_select
        self.sprite.draw()