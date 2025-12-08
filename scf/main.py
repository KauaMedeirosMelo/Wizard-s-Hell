from pplay import window, sprite, mouse
from pygame import display, NOFRAME
from resacc import res_access, change_access, sound_access
import entity, tower, background, enemy, toolbar, models, card, menu

event = False

screen = window.Window(1000, 700)
display.set_mode((screen.width, screen.height), NOFRAME)
#mouse.Mouse.hide(mouse)

key = screen.get_keyboard()

menu.init_menu(screen, res_access[0], sound_access[0])

card.init()
background.init(res_access[0])
toolbar.init(screen, res_access[0])
entity.init()
tower.start_towers(screen, res_access[0])
enemy.generate_enemies(screen, res_access[0], 5)

timer = 0
num = 5

def init_master(screen, res_access):
    global key, timer, num
    key = screen.get_keyboard()

    mouse.Mouse.hide(mouse)
    card.init()
    background.init(res_access[0])
    toolbar.init(screen, res_access[0])
    entity.init()
    tower.start_towers(screen, res_access[0])
    enemy.generate_enemies(screen, res_access[0], 5)

    timer = 0
    num = 5

def tick():
    global timer, num, myX, myY

    dt = screen.delta_time()

    match menu.current:

        case "Menu":
            toolbar.tick(screen, res_access[0], sound_access[0])

            if(toolbar.click):
                for i in range(len(menu.main_buttons)):
                    if(menu.main_buttons[i].collision(toolbar.mouse_mask)):
                        menu.main_buttons[i].sound.play()
                        menu.current = menu.main_buttons[i].state
                        mouse.Mouse.hide(mouse)
                pass

        case "Jogar":
            timer += dt
            toolbar.game_timer[0] += dt

            if(timer >= 15):
                enemy.generate_enemies(screen, res_access[0],num)
                num = num+2
                timer = 0
            
            entity.tick(toolbar.mouse_mask, dt)
            card.tick(screen, res_access[0], toolbar.mouse_mask, dt)

            if(key.key_pressed("esc")):
                init_master(screen, res_access)
                mouse.Mouse.unhide(mouse)
                menu.current = "Menu"

            if(key.key_pressed("p")):
                change_access("models")

            if(key.key_pressed("space")):
                models.change_models(screen)

            toolbar.tick(screen, res_access[0], sound_access[0])
            if(toolbar.exp[0] <= 0):
                screen.close()

            if(toolbar.click and toolbar.mode == 3):
                for i in range(len(entity.towers)):
                    for j in range(len(entity.towers[i])):
                        if(entity.towers[i][j].collision(toolbar.mouse_mask)):
                            toolbar.visible = True
                            toolbar.towerI = i
                            toolbar.towerJ = j
                            toolbar.show_stats[0] = entity.towers[i][j].size
                            toolbar.show_stats[1] = entity.towers[i][j].speed
                            toolbar.show_stats[2] = entity.towers[i][j].cooldown
                            entity.towers[i][j].show_cards = True

            if(card.set_stat and toolbar.click):
                for i in range(len(entity.towers)):
                    for j in range(len(entity.towers[i])):
                        if(entity.towers[i][j].collision(toolbar.mouse_mask)):
                            if(not (card.stat in entity.towers[i][j].stats)):
                                entity.towers[i][j].stats.append(card.stat)
                                entity.towers[i][j].execute_stats(res_access[0])
                                card.set_stat = False
                                card.stat = None
                                card.show_select = False
                            pass

        
        case "Sair":
            screen.close()


def render(screen):
    match menu.current:

        case "Menu":
            screen.set_background_color((0,0,0))
            for i in menu.main_buttons:
                i.render()
            screen.update()
            pass
        
        case "Jogar":
            screen.set_background_color((0,0,0))
            background.render()
            entity.render(screen)
            toolbar.render(screen)
            card.render(screen)
            toolbar.mouse_mask.draw()
            screen.update()

while(True):

    tick()
    render(screen)
    
    pass