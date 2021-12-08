from pico2d import *
import game_framework
import server
import theWorld

history=[]

R_down,L_down,R_up, L_up, S_down, S_up, Z_down, Z_up= range(8)

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

time_action=0.5
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
    def enter(mario, event):
        if event == R_down:
            mario.velocity += RUN_SPEED_PPS
        elif event == L_down:
            mario.velocity -= RUN_SPEED_PPS
        elif event == R_up:
            mario.velocity -= RUN_SPEED_PPS
        elif event == L_up:
            mario.velocity += RUN_SPEED_PPS
        mario.timer=50


    def exit(mario, event):
        pass

    def do(mario):
        mario.frame=(mario.frame+action_frame*action_time*game_framework.frame_time) % 8

    def draw(mario):
        if mario.dir==1:
            mario.image.clip_draw(int(mario.frame) * 100, 300, 100, 100, mario.x, mario.y)
        else:
            mario.image.clip_draw(int(mario.frame) * 100, 200, 100, 100, mario.x, mario.y)

class RunState:
    def enter(mario,event):
        if event == R_down:
            mario.velocity += RUN_SPEED_PPS
        elif event == L_down:
            mario.velocity -= RUN_SPEED_PPS
        elif event == R_up:
            mario.velocity -= RUN_SPEED_PPS
        elif event == L_up:
            mario.velocity += RUN_SPEED_PPS
        mario.dir=clamp(-1, mario.velocity,1)

    def exit(mario,event):
        pass

    def do(mario):

        mario.frame = (mario.frame+action_frame*action_time*game_framework.frame_time) % 8
        mario.x += mario.velocity* game_framework.frame_time


    def draw(mario):
        cx, cy= mario.x-server.background.window_left, mario.y-server.background.window_bottom
        if mario.dir ==1:
            mario.image.clip_draw(int(mario.frame) * 100, 100, 100, 100, mario.x, mario.y)
        else:
            mario.image.clip_draw(int(mario.frame) * 100, 0, 100, 100, mario.x, mario.y)


class DashState:
    def enter(mario,event):
        mario.dir=mario.velocity

    def exit(mario,event):
        pass

    def do(mario):
        mario.frame = (mario.frame + action_frame * action_time * game_framework.frame_time) % 8
        mario.x += mario.velocity * game_framework.frame_time *3


    def draw(mario):
        if mario.dir >= 1:
            mario.image.clip_draw(int(mario.frame) * 100, 100, 100, 100, mario.x, mario.y)
        else:
            mario.image.clip_draw(int(mario.frame) * 100, 0, 100, 100, mario.x, mario.y)

class JumpState:
    def enter(mario,event):
        mario.timer=5
        pass

    def exit(mario, event):
        pass
    def do(mario):
        mario.frame = (mario.frame + action_frame * action_time * game_framework.frame_time) % 8
        mario.y+=5* game_framework.frame_time
        mario.timer -= 1
        if mario.timer==0:
            mario.y-=5* game_framework.frame_time
    def draw(mario):
        if mario.dir >= 1:
            mario.image.clip_draw(int(mario.frame) * 100, 100, 100, 100, mario.x, mario.y)
        else:
            mario.image.clip_draw(int(mario.frame) * 100, 0, 100, 100, mario.x, mario.y)


next_state = {
    IdleState: {R_up:RunState, R_down:RunState, L_up:RunState, L_down:RunState,
                S_up:IdleState,S_down:IdleState,Z_up:IdleState,Z_down:IdleState},
    RunState: {R_up:IdleState, R_down:IdleState, L_up:IdleState, L_down:IdleState,S_down:DashState,S_up:RunState,
               Z_up:RunState, Z_down:JumpState},
    DashState:{R_up:IdleState, R_down:IdleState, L_up:IdleState, L_down:IdleState,S_up:RunState},
    JumpState:{R_up:IdleState, R_down:IdleState, L_up:IdleState, L_down:IdleState,Z_up:RunState}
}
class Mario:
    def __init__(self):
        self.x, self.y = 200 , 160
        self.image=load_image('animation_sheet.png')
        self.fallspeed = 269
        self.dir=1
        self.velocity=0
        self.jump=50
        self.frame=0

        self.jump=1
        self.event_que=[]
        self.cur_state = IdleState
        self.cur_state.enter(self,None)

    def get_bb(self):
        return self.x-30, self.y-50, self.x+30, self.y+50

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)
        self.y -= self.fallspeed * game_framework.frame_time
        self.x = clamp(0, self.x, server.background.w - 1)
        self.y = clamp(0, self.y, server.background.h - 1)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
         if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
    def stop(self):
        self.fallspeed=0

