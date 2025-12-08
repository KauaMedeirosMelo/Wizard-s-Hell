from pygame import draw, surface, SRCALPHA
from pplay import sprite, mouse, sound
import tower, menu
from card import new_cards
import entity
import math


mouse_mask = None
tower_stats = None
toolbar1 = None
toolbar2 = None
dice = None

visible = False


mode = 2
key = None

mouse_pressed = False
click = False
key_pressed = False
key_released = False

selection = False
aim = False
shoot = False
posX1 = posX2 = posY1 = posY2 = 0

exp = [100]
exp_change = [1]

score = [0]
game_timer = [0]

show_stats = [0,0,0]
towerI = 0
towerJ = 0

def init(screen, res_access):
    global mouse_mask, tower_stats, toolbar1, toolbar2, dice, visible, mode, key, mouse_pressed, click, key_pressed, key_released, selection, aim, shoot, posX1, posX2, posY1, posY2, exp, exp_change, score, game_timer, show_stats, towerI, towerJ

    mouse_mask = None
    tower_stats = None
    toolbar1 = None
    toolbar2 = None
    dice = None

    visible = False


    mode = 2
    key = None

    mouse_pressed = False
    click = False
    key_pressed = False
    key_released = False

    selection = False
    aim = False
    shoot = False
    posX1 = posX2 = posY1 = posY2 = 0

    exp = [100]
    exp_change = [1]

    score = [0]
    game_timer = [0]

    show_stats = [0,0,0]
    towerI = 0
    towerJ = 0

    init_sprites(screen, res_access)


def init_sprites(screen, res_access):
    global mouse_mask, tower_stats, toolbar1, toolbar2, dice, key

    key = screen.get_keyboard()

    mouse_mask = sprite.Sprite(res_access+"mouse.png")


    toolbar1 = sprite.Sprite(res_access+"toolbar.png")
    toolbar2 = sprite.Sprite(res_access+"toolbar.png")
    toolbar1.x = 0
    toolbar2.x = 850
    toolbar1.y = 0
    toolbar2.y = 0
    
    tower_stats = sprite.Sprite(res_access+"tower_stats.png")
    tower_stats.x = toolbar1.width/2 - tower_stats.width/2
    tower_stats.y = 20 + tower_stats.height*1.2*3

    dice = sprite.Sprite(res_access+"dice.png")
    dice.x = screen.width - dice.width*2
    dice.y = screen.height - dice.height*1.5

def tick(screen, res_access, sound_access):
    global visible, mouse_mask, key, mode, mouse_pressed, key_pressed, key_released, click, selection, aim, shoot, posX1, posX2, posY1, posY2, dice

    mouse_mask.x, mouse_mask.y = mouse.Mouse.get_position(mouse)

    click = False
    shoot = False

    key_released = False

    posX2, posY2 = mouse.Mouse.get_position(mouse)
    
    #Pressionou a tecla
    
    if(menu.current == "Jogar"):
        if(key.key_pressed("1")):
            if(not key_pressed):
                key_pressed = True
                mouse_mask = sprite.Sprite(res_access+"mouse_selection.png")
                mouse_mask.x = posX2
                mouse_mask.y = posY2
                visible = False
            mode = 1
        elif(key.key_pressed("2")):
            if(not key_pressed):
                key_pressed = True
                visible = False
                mouse_mask = sprite.Sprite(res_access+"mouse.png")
                mouse_mask.x = posX2
                mouse_mask.y = posY2
                visible = False
            mode = 2
        elif(key.key_pressed("3")):
            if(not key_pressed):
                key_pressed = True
                visible = False
                mouse_mask = sprite.Sprite(res_access+"mouse.png")
                mouse_mask.x = posX2
                mouse_mask.y = posY2
                tower.release_bullets()
            mode = 3
        else:
            if(key_pressed):
                #Alguma tecla foi solta:
                key_released = True
                key_pressed = False



    if(mouse.Mouse.is_button_pressed(mouse, 1)):
        if(not mouse_pressed):
            #O clique começou

            mouse_pressed = True
            if(menu.current == "Jogar"):
                match mode:
                    case 1:
                        if(not key.key_pressed("LEFT_CONTROL")):
                            tower.release_bullets()
                        posX1, posY1 = mouse.Mouse.get_position(mouse)
                        selection = True
                    
                    case 2:
                        posX1, posY1 = mouse.Mouse.get_position(mouse)
                        aim = True
    else:
        if(mouse_pressed):
            #O clique acabou

            click = True
            mouse_pressed = False
            if(menu.current == "Jogar"):
                selection = False
                aim = False

                match mode:
                    case 2:
                        tower.aim_bullets(posX1, posY1, posX2, posY2)
                        pass

                    case 3:
                        if(exp[0] >= 200 and mouse_mask.collided(dice)):
                            dice_sound = sound.Sound(sound_access+"dice.wav")
                            dice_sound.play()
                            new_cards(screen, res_access, sound_access)

            

    if(menu.current == "Jogar"):
        match mode:
            case 1:
                if(selection):
                    tower.select_bullets(posX1, posY1, posX2, posY2)
                    pass
            
            case 2:
                if(shoot):
                    pass
                pass


def render(screen):
    global visible, selection, posX1, posX2, posY1, posY2, exp, towerI, towerJ

    draw.line(screen.get_screen(), (255,255, 0), (screen.width/2-exp[0], 10), (screen.width/2+exp[0], 10), width=7)

    screen.draw_text(str(score[0]), (screen.width - int(math.log10(score[0]+1))*15)/2, 50, 40, (255,255,255))

    toolbar1.draw()
    toolbar2.draw()

    if(exp[0] >= 200):
        dice.draw()
    if(selection):
        rect_surface = surface.Surface((abs(posX1 - posX2), abs(posY1 - posY2)), SRCALPHA)
        draw.rect(rect_surface, (255, 255, 255, 150), (0,0, abs(posX1-posX2), abs(posY1-posY2)), width=3)
        screen.screen.blit(rect_surface, (min(posX1, posX2), min(posY1,posY2)))
    
    if(aim):
        # line_surface = surface.Surface((2*abs(posX1 - posX2), 2*abs(posY1 - posY2)), SRCALPHA)
        # draw.line(line_surface, (255, 255, 255, 150), (line_surface.get_width()/2, line_surface.get_height()/2), (posX1 - posX2, posY1 - posY2), width=3)
        # screen.screen.blit(line_surface, (min(posX1, posX2), min(posY1,posY2)))
        draw.line(screen.get_screen(), (255, 255, 255), (posX1, posY1), (posX2, posY2), width=3)

    if(visible):
        #tower_stats.draw()
        for i in (entity.towers[towerI][towerJ].card_sprites):
            i.draw()
        
        # screen.draw_text(str(int(show_stats[0])), tower_stats.x + 20, tower_stats.y + 10, 20, (255, 0, 0))
        # screen.draw_text(str(int(show_stats[1])), tower_stats.x + 20, tower_stats.y + 40, 20, (0, 255, 0))
        # screen.draw_text(str(int(show_stats[2])), tower_stats.x + 20, tower_stats.y + 70, 20, (0, 0, 255))
