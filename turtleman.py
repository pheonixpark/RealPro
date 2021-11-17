from pico2d import *
import random

class Turtleman:
    def __init__(self):
        self.x, self.y=random.randint(0,1600-1),70
        self.image = load_image('turtleman.png')
        speed=[-2,2]
        self.velocity=random.choice(speed)

    def update(self):
        self.x+=self.velocity

    def get_bb(self):
        return self.x-20, self.y-30, self.x+20, self.y+30

    def draw(self):
        self.image.draw(self.x,self.y)
        draw_rectangle(*self.get_bb())