# Tron
import pgzrun

speed = 3

dirs=[0,90,180,270]
moves = [(0,-1),(-1,0),(0,1),(1,0)]


WIDTH = 800
HEIGHT = 483

def update():
    global matrix
    bike.angle = dirs[bike.direction]
    bike.x += moves[bike.direction][0]*speed
    bike.y += moves[bike.direction][1]*speed

def on_key_down(key):
    if key == keys.LEFT:
        bike.direction += 1
        if bike.direction == 4 : bike.direction = 0


    if key == keys.RIGHT:
        bike.direction -= 1
        if bike.direction == -1 : bike.direction = 3

def draw():
    screen.blit("background", (0, 0))
    bike.draw()

def init():
    global bike,matrix
    bike = Actor('bike1', center=(400, 500))
    bike.direction = 0
    matrix = [[0 for y in range(60)] for x in range(80)]




init()
pgzrun.go()
