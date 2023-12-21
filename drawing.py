import pygame

SCALE = 20
PADDING = SCALE*2
PRIMARY = "black"
SECONDARY = "white"

def draw_side_by_side(a, b):
    dimensions = (PADDING + len(a)*SCALE + PADDING + len(b)*SCALE + PADDING, PADDING + len(a)*SCALE + PADDING)

    screen = init(dimensions)
    aCorner = (PADDING,PADDING)
    bCorner = (PADDING + len(a)*SCALE + PADDING,PADDING)
    for row in range(len(a)):
        for col in range(len(a)):
            color = PRIMARY if a[row][col] == 1 else SECONDARY
            pos = (aCorner[0] + col*SCALE,aCorner[1] + row*SCALE) 
            pygame.draw.rect(screen,color,pygame.Rect(pos,(SCALE,SCALE)))
    for row in range(len(b)):
        for col in range(len(b)):
            color = PRIMARY if b[row][col] == 1 else SECONDARY
            pos = (bCorner[0] + col*SCALE,bCorner[1] + row*SCALE) 
            pygame.draw.rect(screen,color,pygame.Rect(pos,(SCALE,SCALE)))

    pygame.display.flip()


    
    awaitQuit()


def init(dimensions):
    pygame.init()
    screen = pygame.display.set_mode(dimensions)
    pygame.draw.rect(screen,"bisque",pygame.Rect((0,0),dimensions))
    pygame.display.flip()
    return screen

def awaitQuit():
    running = True
    while running:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:  
            running = False

