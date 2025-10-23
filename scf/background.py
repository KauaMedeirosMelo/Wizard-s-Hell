from pplay import sprite

image = None

def start(res_access):
    global image
    image = sprite.Sprite(res_access+"background1.png")

def render():
    image.draw()