import pygame as pg, random as rd
from pygame.locals import *
#defines the objects in game. like the snake and the apple (could be more than one)
class Stuff:
    def __init__(self, position, body, color, points = None, record = None, direction = None):
        self.position = position
        self.body = body
        self.color = color
        self.points = points
        self.record = record
        self.direction = direction
#defines the apple coordinates
def on_grid_random():
    x, y = rd.randint(0, 690), rd.randint(0, 690)
    return (x//10 * 10, y//10 * 10)
#moves the snakes
def move(wich_snake):
    for i in range(len(wich_snake.position) - 1, 0, -1):
        wich_snake.position[i] = (wich_snake.position[i-1][0], wich_snake.position[i-1][1])
    if wich_snake.direction == up:
        wich_snake.position[0] = (wich_snake.position[0][0], wich_snake.position[0][1] - 10)
    if wich_snake.direction == down:
        wich_snake.position[0] = (wich_snake.position[0][0], wich_snake.position[0][1] + 10)
    if wich_snake.direction == left:
        wich_snake.position[0] = (wich_snake.position[0][0] - 10, wich_snake.position[0][1])
    if wich_snake.direction == right:
        wich_snake.position[0] = (wich_snake.position[0][0] + 10, wich_snake.position[0][1])
#keep snake moving and changes snake direction
def key_verify(wich_snake):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                if wich_snake.direction != down:
                    wich_snake.direction = up
            if event.key == K_DOWN:
                if wich_snake.direction != up:
                    wich_snake.direction = down
            if event.key == K_LEFT:
                if wich_snake.direction != right:
                    wich_snake.direction = left
            if event.key == K_RIGHT:
                if wich_snake.direction != left:
                    wich_snake.direction = right
#verify colissions and defines the pontuation
def colission(wich_snake):
    if wich_snake.points > wich_snake.record: wich_snake.record += 1

    if wich_snake.position[0] == apple.position:
        wich_snake.position.append([700, 700])
        apple.position = on_grid_random()
        wich_snake.points += 1
        
    if wich_snake.position[0][0] in wall or wich_snake.position[0][1] in wall:
        wich_snake.direction = right
        snake.position = [(200, 200), (210, 200), (220, 200)]
        apple.position = on_grid_random()
        wich_snake.points = 0
        wich_snake.direction = hit_wall

    if cnt > 2:
        if wich_snake.position[0] in wich_snake.position[1:-2]:
            wich_snake.position = [(200, 200), (210, 200), (220, 200)]
            apple.position = on_grid_random()
            wich_snake.points = 0
            wich_snake.direction = ate_itself
#variables used in game
up, down, left, right, ate_itself, hit_wall = 0, 1, 2, 3, 4, 5
snake = Stuff(([(200, 200), (210, 200), (220, 200)]), pg.Surface((10, 10)), (255, 215, 0), 0, 0, right)
apple = Stuff(on_grid_random(), pg.Surface((10, 10)), (50, 205, 50))
wall = [700, -10]
clock = pg.time.Clock()
cnt = 0
pg.init()
screen = pg.display.set_mode((700, 700))
#game running
while True:
    cnt += 1
    clock.tick(35)
    screen.fill((255, 255, 250))
    apple.body.fill(apple.color)
    screen.blit(apple.body, apple.position)
    snake.body.fill(snake.color)
    caption = 'Snake size ' + str(snake.points) + ' | record: ' + str(snake.record)
    if snake.direction == ate_itself:
        caption = 'Ate itself! Choose a new direction'
        print(caption)
    if snake.direction == hit_wall:
        caption = 'It hit the wall! choose a new direction'
        
    
    pg.display.set_caption(caption)

    key_verify(snake)
    move(snake)
    colission(snake)

    for pos in snake.position:
        screen.blit(snake.body, pos)
    pg.display.update()
