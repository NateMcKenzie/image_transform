import pygame

SCALE = 20
PADDING = SCALE*2

def draw_side_by_side(a, b):
    dimensions = (PADDING + len(a[0])*SCALE + PADDING + len(b[0])*SCALE + PADDING, PADDING + len(a[0])*SCALE + PADDING)

    screen = init(dimensions)
    aCorner = (PADDING,PADDING)
    bCorner = (PADDING + len(a[0])*SCALE + PADDING,PADDING)
    draw(a,aCorner,screen)
    draw(b,bCorner,screen)

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

def draw(channels, corner,screen):
    for row in range(len(channels[0])):
        for col in range(len(channels[0])):
            r = channels[0][row][col] * 255 
            g = channels[1][row][col] * 255 
            b = channels[2][row][col] * 255 
            color = pygame.Color(r,g,b)
            pos = (corner[0] + col*SCALE, corner[1] + row*SCALE) 
            pygame.draw.rect(screen,color,pygame.Rect(pos,(SCALE,SCALE)))
