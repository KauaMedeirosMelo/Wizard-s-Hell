from pplay import sprite, sound
import resacc


current = "Menu"
main_buttons = []
background = None

def init_menu(screen, res_access, sound_access):
    global main_buttons, background

    button_sound = sound.Sound(resacc.resource_path("snd\\button.wav"))
    button_sound.set_volume(100)

    jogar_sprite = sprite.Sprite(resacc.resource_path("res\\models\\jogar.png"))
    jogar = Button(jogar_sprite, button_sound, (screen.width + 2*jogar_sprite.width)/2, 250, "Jogar", main_buttons)

    sair_sprite = sprite.Sprite(resacc.resource_path("res\\models\\sair.png"))
    sair = Button(sair_sprite, button_sound, (screen.width + 2*sair_sprite.width)/2, 450, "Sair", main_buttons)


    main_buttons.append(jogar)
    main_buttons.append(sair)

    background = sprite.Sprite(resacc.resource_path("res\\models\\menu_background.png"))

    pass

def init_esc():
    pass

class Button:
    
    def __init__(self, mask, sound, x, y, state, arr):
        self.x = x
        self.y = y
        self.mask = mask
        self.sound = sound
        self.state = state
        mask.x = x
        mask.y = y
        arr.append(self)
    
    def collision(self, obj):
        if(self.mask.collided(obj)):
            return True
        
    def render(self):
        self.mask.draw()

