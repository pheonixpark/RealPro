from pico2d import *
import random

class Gumba:
    def __init__(self):
        self.x, self.y=random.randint(0,1600-1),80
        self.image = load_image('Gumba.png')
        speed=[-2,2]
        self.velocity=random.choice(speed)

    def update(self):
        self.x+=self.velocity

    def get_bb(self):
        return self.x-20, self.y-15, self.x+20, self.y+15

    def draw(self):
        self.image.draw(self.x,self.y)
        draw_rectangle(*self.get_bb())




