from pico2d import *
import game_framework
import theWorld

history=[]

R_down,L_down,R_up, L_up, S_down, S_up, Z_down, Z_up= range(8)

PIXEL_PER_METER = (20.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 30.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

time_action=1.0
action_time=1.0/time_action
action_frame= 8

key_event_table={
    (SDL_KEYDOWN, SDLK_RIGHT):R_down,
    (SDL_KEYUP, SDLK_RIGHT): R_up,
    (SDL_KEYDOWN, SDLK_LEFT): L_down,
    (SDL_KEYUP, SDLK_LEFT): L_up,
    (SDL_KEYDOWN,SDLK_z): Z_down,
    (SDL_KEYUP,SDLK_z): Z_up,
    (SDL_KEYDOWN,SDLK_LSHIFT):S_down,
    (SDL_KEYUP,SDLK_LSHIFT):S_up
}

class IdleState:
    def enter(Mario, event):
        if event == R_down:
            Mario.velocity += RUN_SPEED_PPS
        elif event == L_down:
            Mario.velocity -= RUN_SPEED_PPS
        elif event == R_up:
            Mario.velocity -= RUN_SPEED_PPS
        elif event == L_up:
            Mario.velocity += RUN_SPEED_PPS

    def exit(Mario, event):
        pass

    def Fr(Mario):
        Mario.frame=(Mario.frame+action_frame*action_time*game_framework.frame_time) % 8

    def draw(Mario):
        if Mario.dir==1:
            Mario.image.clip_draw()
        else:
            Mario.image.clip_draw()

class RunState:
    def enter(Mario,event):
        if event == R_down:
            Mario.velocity += RUN_SPEED_PPS
        elif event == L_down:
            Mario.velocity -= RUN_SPEED_PPS
        elif event == R_up:
            Mario.velocity -= RUN_SPEED_PPS
        elif event == L_up:
            Mario.velocity += RUN_SPEED_PPS
        Mario.dir=clamp(-1, Mario.velocity,1)

    def exit(Mario,event):
        pass

    def Fr(Mario):
        Mario.frame = (Mario.frame+action_frame*action_time*game_framework.frame_time) % 8
        Mario.x += Mario.velocity* game_framework.frame_time
        Mario.x+=clamp(25, Mario.x,1600-25)

    def draw(Mario):
        if Mario.dir ==1:
            Mario.image.clip_draw()
        else:
            Mario.image.clip_draw()

next_state = {
    IdleState: {R_up:RunState, R_down:RunState, L_up:RunState, L_down:RunState, S_up:IdleState, S_down:IdleState},
    RunState: {R_up:IdleState, R_down:IdleState, L_up:IdleState, L_down:IdleState}
}
class mario:
    def __init__(self):
        self.x, self.y = 1600//2 , 90
        self.image=load_image()
        self.dir=1
        self.velocity=0
        self.frame=0
        self.event_que=[]
        self.cur_state = IdleState
        self.cur_state.enter(self,None)

    def get_bb(self):
        return self.x-50, self.y-50, self.x+50, self.y+50

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
         if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

