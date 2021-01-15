import pygame
from random import choice


def draw():
    screen.fill(pygame.Color('white'))
    global animcount
    global run
    global g
    global j
    global ptero


    if animcount + 1 >= 7:
        animcount = 0

    if die:
        screen.blit(dino_die, (x, y))
        run = False
        screen.blit(game, (300, 150))

    elif sit:
        screen.blit(sitnanim[animcount // 3], (x, y))
        animcount += 1

    elif ISjump:
        screen.blit(dino, (x, y))

    else:
        screen.blit(runanim[animcount // 3], (x, y))
        animcount += 1

    font = pygame.font.Font(None, 20)
    text_points = str(points)
    text = font.render('Your points: ' + text_points, True, (99, 99, 99))
    text_x = 800
    text_y = 50
    screen.blit(text, (text_x, text_y))

    if points < 400:
        if g <= -100:
            g += 1400
            j += 1
            screen.blit(obstacle[j], (g, 274))
        else:
            screen.blit(obstacle[j], (g, 274))
        g -= 15
        if j >= 6:
            j = 0
    else:
        if ptero and j >= 7:
            a = choice((274, 200, 120))
            if j % 8 == 0:
                screen.blit(obstacle[j], (g, a))
                j -= 1
            else:
                screen.blit(obstacle[j], (g, a))
                j += 1
        else:
            if g <= -100:
                n = choice((1100, 1200, 1300, 1400))
                g += n
                j += 1
                screen.blit(obstacle[j], (g, 274))
            else:
                screen.blit(obstacle[j], (g, 274))
            g -= 15
            if j >= 7:
                j = 0


    screen.blit(bg, (z, 330))
    screen.blit(bg, (z + 2398, 330))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1000, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Dino')
    g = 500
    j = 0
    x = 80
    y = 260
    f = 0
    width1 = 87
    height1 = 83
    cikl = 0

    z = 0
    points = 0
    ptero = False
    ISjump = False
    sit = False
    die = False
    run = True
    Jumpcount = 10

    delay1 = 70
    animcount = 0

    runanim = [pygame.image.load('dino_run1.png'), pygame.image.load('dino_run2.png')]
    sitnanim = [pygame.image.load('dino_sit1.png'), pygame.image.load('dino_sit2.png')]
    bg = pygame.image.load('Doroga.png')
    dino = pygame.image.load('dino.png')
    dino_die = pygame.image.load('dino_die.png')
    obstacle = [pygame.image.load('one_small.png'), pygame.image.load('two_small.png'),\
                pygame.image.load('three_small.png'), pygame.image.load('one_big.png'),\
                pygame.image.load('two_big.png'), pygame.image.load('two_big_and_small.png'),\
                pygame.image.load('polet1.png'), pygame.image.load('polet2.png')]
    obstacle_size = [(34, 70), (68, 70), (102, 70), (50, 96), (98, 96), (103, 97), (92, 60), (92, 60)]
    game = pygame.image.load('game_over.png')

    draw()
    while run:
        pygame.time.delay(delay1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.KMOD_CTRL] or keys[pygame.K_DOWN]:
            x = 111
            y = 293
            width1 = 118
            height = 60
            sit = True
        else:
            sit = False

        if not ISjump and not sit:
            x = 80
            y = 260
            width1 = 87
            height1 = 83

        if not ISjump:
            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                ISjump = True
        else:
            if Jumpcount >= -10 and not sit:
                if Jumpcount < 0:
                    y += (Jumpcount ** 2) / 2
                else:
                    y -= (Jumpcount ** 2) / 2
                Jumpcount -= 1
            else:
                ISjump = False
                Jumpcount = 10

        if z < -2398:
            z = 0
        else:
            z -= 15

        points += 1
        if points == 100:
            delay1 = 60
        elif points == 500:
            delay1 = 50
        elif points == 800:
            delay1 = 40
        elif points == 1000:
            delay1 = 30
        elif points == 1000:
            delay1 = 20
        elif points == 1100:
            delay1 = 17
        elif points == 1250:
            delay1 = 15
        elif points == 1400:
            points = 12
        elif points == 1500:
            delay1 = 10

        x1, y1, w1, h1 = x, y, width1, height1
        if cikl > 0:
            d = obstacle.index(obstacle[j])
            s = obstacle_size[d]
            if ptero:
                a = choice((274, 200, 120))
                x2, y2, w2, h2 = g + 10, a, s[0] - 15, s[1] - 15
            else:
                x2, y2, w2, h2 = g + 10, 274, s[0] - 15, s[1] - 15
            if x1 <= x2 <= x1 + w1 and y1 <= y2 <= y1 + h1:
                die = True
            elif x1 <= x2 + w2 <= x1 + w1 and y1 <= y2 <= y1 + h1:
                die = True
            elif x1 <= x2 <= x1 + w1 and y1 <= y2 + h2 <= y1 + h1:
                die = True
            elif x1 <= x2 + w2 <= x1 + w1 and y1 <= y2 + h2 <= y1 + h1:
                die = True

            elif x2 <= x1 <= x2 + w2 and y2 <= y1 <= y2 + h2:
                die = True
            elif x2 <= x1 + w1 <= x2 + w2 and y2 <= y1 <= y2 + h2:
                die = True
            elif x2 <= x1 <= x2 + w2 and y2 <= y1 + h1 <= y2 + h2:
                die = True
            elif x2 <= x1 + w1 <= x2 + w2 and y2 <= y1 + h1 <= y2 + h2:
                die = True
            else:
                die = False
        cikl += 1
        draw()
        pygame.display.update()
        if points >= 400 and j > 7:
            ptero = True

    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()



