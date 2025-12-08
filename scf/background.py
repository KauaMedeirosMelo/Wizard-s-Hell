from pplay import sprite

image = None

def init(res_access):
    global image
    image = sprite.Sprite(res_access+"background1.png")
    image.x = 150

def render():
    image.draw()