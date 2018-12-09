import sys, pygame, random
pygame.init()

size = width, height = 800, 600
speed = [1, 1]
black = 0, 0, 0

w = 10
h = 10
field = [[0 for x in range(w)]for y in range(h)]
field[0][0] = 1
#field[2][0] = 1
#field[4][0] = 1
#field[6][0] = 1

screen = pygame.display.set_mode(size)

wolf = pygame.image.load("wolf.png")
wolfrect = wolf.get_rect()
wolfrect.move_ip(450, 450)
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


def drawBlock(x, y):
    rect = pygame.Rect(x*50+3, y*50+3, 50-3, 50-3)
    if field[x][y] == 1:
        pygame.draw.rect(screen, (118, 47, 50), rect, 0)
    if field[x][y] == 0:
        pygame.draw.rect(screen, (0, 128, 0), rect, 0)




def drawField():
    for zeile in range(10):
        for spalte in range(10):
            drawBlock(spalte, zeile)

def drawSheep():
    screen.blit(sheep, sheeprect)

def moveWolf():
    direction = random.choice(['right', 'left', 'up', 'down', 'sit'])
    if direction == 'right' and wolfrect.x < 450:
        wolfrect.move_ip(50, 0)
    if direction == 'left' and wolfrect.x > 0:
        wolfrect.move_ip(-50, 0)
    if direction == 'up' and wolfrect.y > 0:
        wolfrect.move_ip(0, -50)
    if direction == 'down' and wolfrect.y < 450:
        wolfrect.move_ip(0, 50)
    print (direction)

#showSpeed()w




while True:
    clck.tick(40)
    #print("ticks: %i" % ticks)
    for event in pygame.event.get():
        #print('event: ', event)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            print('KEYDOWN event.unicode = %s' % event.unicode)
            #print('KEYDOWN pygame.K_q = %s' % pygame.K_q)
            if event.key == pygame.K_q:
                print('Q')
                sys.exit()
            if event.key == pygame.K_LEFT and sheeprect.x > 0:
                print('LEFT')
                sheeprect.move_ip(-50, 0)
            if event.key == pygame.K_RIGHT and sheeprect.x < 450:
                print('RIGHT')
                sheeprect.move_ip(50, 0)
            if event.key == pygame.K_UP and sheeprect.y > 0:
                print('UP')
                sheeprect.move_ip(0, -50)
            if event.key == pygame.K_DOWN and sheeprect.y < 450:
                print('DOWN', sheeprect)
                sheeprect.move_ip(0, 50)

            field[int(sheeprect.x / 50)][int(sheeprect.y / 50) ] = 1



    if pygame.time.get_ticks() - ticks > 120:
        moveWolf()
        ticks = pygame.time.get_ticks()

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
    drawSheep()

    pygame.display.flip()

















































