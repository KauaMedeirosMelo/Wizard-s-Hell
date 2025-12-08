from pplay import sprite, sound


current = "Menu"
main_buttons = []

def init_menu(screen, res_access, sound_access):
    global main_buttons

    button_sound = sound.Sound(sound_access+"button.wav")
    button_sound.set_volume(100)

    jogar_sprite = sprite.Sprite(res_access+"jogar.png")
    jogar = Button(jogar_sprite, button_sound, (screen.width + jogar_sprite.width)/2, 200, "Jogar", main_buttons)

    sair_sprite = sprite.Sprite(res_access+"sair.png")
    sair = Button(sair_sprite, button_sound, (screen.width + sair_sprite.width)/2, 400, "Sair", main_buttons)


    main_buttons.append(jogar)
    main_buttons.append(sair)

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

