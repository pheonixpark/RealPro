from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400,30)



class Boy:
    global running_right
    def __init__(self):
        #self.x=(1-0.05)*self.x+0.05*dir
        self.x,self.y=10,90
        self.jump=0
        self.image=load_image('animation_sheet.png')
        self.frame=0
    def draw(self):
        if running_right:
            self.image.clip_draw(self.frame * 100, 100*1 , 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 100*0 , 100, 100, self.x, self.y)
    def jump(self,j):
        self.jump1=j
    def update(self):
        self.x += (1-0.1) * Lun + 0.1 * Lun
        s








def handle_events   ():
    global running
    global Lun
    global running_right
    global jump1
    running_right=dir>= 0
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            Lun += 10
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            Lun -= 10
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            Lun -= 10
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            Lun += 10
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_z):
            jump1+=50


open_canvas()
Lun=0
jump1=0
grass=Grass()
boy=Boy()

running=True
running_right=True
while running:
    handle_events()
    boy.update()
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()


close_canvas()
