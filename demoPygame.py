import pygame, sys, random
pygame.init()
screen = pygame.display.set_mode([700,500])
screen.fill([250,250,250])
a = pygame.draw.circle(screen,[0,0,0],[round(random.random()*400),round(random.random()*400)],2,0)
pygame.display.flip()
b = pygame.draw.circle(screen,[0,0,0],[round(random.random()*400),round(random.random()*400)],2,0)
pygame.display.flip()
c = pygame.draw.circle(screen,[0,0,0],[round(random.random()*400),round(random.random()*400)],2,0)
pygame.display.flip()
e = pygame.draw.circle(screen,[0,0,0],[round(random.random()*400),round(random.random()*400)],2,0)
pygame.display.flip()

def cord(circle):
    return circle.center

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #======================================
    y = 0
    r = random.randint(1,3)
    if r == 1:
        y = a
    if r == 2:
        y = b
    if r == 3:
        y = c

    Ycord = cord(y)
    Xcord = cord(e)

    f = round(Xcord[0] + (Ycord[0] - Xcord[0])/2)
    s = round(Xcord[1] + (Ycord[1] - Xcord[1])/2)

    NewCord = [f,s]
    e = pygame.draw.circle(screen,[0,0,0],NewCord,2,0)
    pygame.display.flip()
    #======================================
pygame.quit()
    
