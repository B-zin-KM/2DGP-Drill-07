from pico2d import *
import random

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(50, 750), 599
        self.speed = random.randint(4, 10)
        self.size = random.randint(1,2)
        if self.size == 1:
            self.size = 10
            self.image = load_image('ball21x21.png')
        elif self.size == 2:
            self.size = 20
            self.image = load_image('ball41x41.png')

    def update(self):
        self.y -= self.speed
        if self.y - self.size <= 60:
            self.speed = 0

    def draw(self):
        self.image.draw(self.x, self.y)


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def update_world():
    grass.update()
    for boy in team:
        boy.update()
    for o in world:
        o.update()


def render_world():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for o in world:
        o.draw()
    update_canvas()


def reset_world():
    global running
    global grass
    global team
    global world

    running = True
    world = []
    grass = Grass()
    world.append(grass)
    team = [Boy() for i in range(11)]
    balls = [Ball() for i in range(20)]
    world += team + balls


open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
