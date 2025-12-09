from pplay import sprite
import resacc

scores = []
reset = False

background = None

def init_score(res_access):
    global background
    
    background = sprite.Sprite(resacc.resource_path("res\\models\\rank_background.png"))

def save_score(score):
    file_save = open(resacc.resource_path("save\\save.txt"), "a")
    file_save.write(str(score)+"\n")
    file_save.close()

def define_scores():
    global scores, reset
    while(len(scores) != 0):
        scores.pop()
    try:
        with open(resacc.resource_path("save\\save.txt"), "r") as file_return:
            for line in file_return:
                scores.append((line))
    except FileNotFoundError:
        pass

    for i in range(len(scores)):
        for j in range(len(scores) - i - 1):
            if(scores[j] < scores[j+1]):
                scores[j], scores[j+1] = scores[j+1], scores[j]

    scores = scores[:3]
    reset = True

def render(screen):
    global scores, background

    background.draw()

    for i in range(len(scores)):
        screen.draw_text(str(scores[i])[:-1], 250, 370 + i*125, 40, (255,255,255))


