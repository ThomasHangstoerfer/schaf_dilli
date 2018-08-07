import sys, pygame
pygame.init()

size = width, height = 800, 600
speed = [1, 1]
black = 0, 0, 0

w = 10
h = 10
field = [[0 for x in range(w)]for y in range(h)]
field[0][0] = 1

screen = pygame.display.set_mode(size)

wolf = pygame.image.load("wolf.png")
wolfrect = wolf.get_rect()

sheep = pygame.image.load("sheep.png")
sheeprect = sheep.get_rect()

ticks = pygame.time.get_ticks()

clck = pygame.time.Clock()

font = pygame.font.SysFont("Monospaced", 39)
name = 'Dilli'
print('Hallo %s' % name)

def showSpeed():
    global text
    x = abs(speed[0])
    font = pygame.font.SysFont("Monospaced", 39)
    text = font.render(" speed: %i" % x, True, (128, 0, 0))

def drawGrass():
    rect = pygame.Rect(3, 3, 50, 50)
    pygame.draw.rect(screen, (0, 128, 0),  rect, 0)

def drawField():
    rect = pygame.Rect(3, 3, 50, 50)
    if field[0][0] == 1:
        pygame.draw.rect(screen, (118, 47, 50), rect, 0)
    if field[0][0] == 0:
        pygame.draw.rect(screen, (0, 128, 0), rect, 0)

#showSpeed()
drawGrass()

def beschleunige():
    if speed[0]<0:
        speed[0] = speed[0]-1
    if speed[0]>0:
        speed[0] = speed[0]+1
    if speed[1]<0:
        speed[1] = speed[1]-1
    if speed[1]>0:
        speed[1] = speed[1]+1

    showSpeed()

while True:
    clck.tick(40)
    #print("ticks: %i" % ticks)
    for event in pygame.event.get():
        #print('event: ', event)
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            print('KEYDOWN event.unicode = %s' % event.unicode)
            #print('KEYDOWN pygame.K_q = %s' % pygame.K_q)
            if event.key == pygame.K_q:
                print('Q')
                sys.exit()
            if event.key == pygame.K_LEFT:
                print('LEFT')
            if event.key == pygame.K_RIGHT:
                print('RIGHT')

    #if pygame.time.get_ticks() - ticks > 50:
    #ballrect = ballrect.move(speed)
    #    ticks = pygame.time.get_ticks()

    #if ballrect.left <= 0 or ballrect.right >= width:
    #    beschleunige()
    #    speed[0] = -speed[0]
    #if ballrect.top <= 0 or ballrect.bottom >= height:
    #    beschleunige()
    #    speed[1] = -speed[1]

    screen.fill(black)
    #screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))
    #screen.blit(text, (0, 0))
    #drawGrass()
    drawField()

    screen.blit(wolf, wolfrect)
    screen.blit(sheep, sheeprect)

    pygame.display.flip()
