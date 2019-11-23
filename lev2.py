import random
import time
import pygame
pygame.init()
import main

width, height = 1000, 500
screen = pygame.display.set_mode((width,height))
red = 255, 0, 0
blue = 0, 0, 255
green = 0, 255, 0
black = 0, 0, 0
white = 255, 255, 255
screen.fill(white)

#winSound = pygame.mixer.Sound('Ta Da.wav')

def score(count):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Score : {}".format(count), True, black)
    screen.blit(text, (width-100, 0))

def gameOver():
    font = pygame.font.SysFont(None, 100)
    text = font.render("GAME OVER",True, black)
    screen.blit(text, (width/2-200,height/2-50))


def win():
    font = pygame.font.SysFont(None, 100)
    text = font.render("YOU WIN", True, black)
    screen.blit(text, (width / 2 - 200, height / 2 - 50))
    #winSound.play()


def game():
    FPS = 1000
    clock = pygame.time.Clock()

    barHeight = 15
    barWidth = 180
    barX = (width - barWidth) / 2
    barY = height - barHeight
    barmoveX = 0

    ballRadius = 10
    ballY = barY - ballRadius
    moveBallY = 0
    moveBallX = 0
    moveBall = False
    Flag = True

    hitlist = []
    clrlist = []
    brickwidth = 100
    brickheight = 15
    brickList = []
    for row in range(5):
        for col in range(width // brickwidth):
            brickList.append(pygame.Rect([(5 + brickwidth) * col, (5 + brickheight) * (row+1), brickwidth,brickheight]))

    for i in range(len(brickList)):
        clrlist.append(green)
        hitlist.append(1)
    count =0
    lifeList = []
    lifeRadius = 5
    for life in range(3):
        lifeList.append(pygame.Rect((10 + lifeRadius)* life,(10 + lifeRadius) , 5, lifeRadius))


    breakSound = pygame.mixer.Sound('point.wav')

    while True:
        screen.fill(white)
        if not moveBall:
            ballX = int(barX + (barWidth//2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    barmoveX = 2
                elif event.key == pygame.K_LEFT:
                    barmoveX = -2
                while Flag:
                    if event.key == pygame.K_SPACE:
                        moveBallY= -1
                        moveBallX = 1
                        moveBall = True
                        Flag = False
                    break

            if event.type == pygame.KEYUP:
                barmoveX=0



        bar_rect = pygame.draw.rect(screen, black, [barX, barY, barWidth, barHeight])
        ball_rect = pygame.Rect(ballX-ballRadius, ballY-ballRadius, ballRadius+ballRadius, ballRadius+ballRadius)
        ball = pygame.draw.circle(screen,red,[ballX,ballY],ballRadius)
        for i in range(len(brickList)):
            brick_rect = pygame.draw.rect(screen,clrlist[i],brickList[i])
        for i in range(len(lifeList)):
            pygame.draw.circle(screen,red,[(10+(lifeRadius+10)*i), 10], lifeRadius)



        if ball_rect.colliderect(bar_rect):
            moveBallX = random.randint(-1,1)
            moveBallY = -1

        for i in range(len(brickList)):
            if ball_rect.colliderect(brickList[i]):
                if hitlist[i] == 1:
                    clrlist[i] = blue
                    hitlist[i] = 2
                elif hitlist[i] == 2:
                    del brickList[i]
                    del clrlist[i]
                    del hitlist[i]
                moveBallY = 1
                moveBallX = random.randint(-1,1)
                count += 1
                FPS += 10000
                breakSound .play()
                break
        for i in range(len(lifeList)):
            if ballY == height+height:
                del lifeList[-1]
                break

        score(count)



        if ballY < 0 +(ballRadius*2)+ brickheight:
            moveBallY = 1
        elif ballY > height + height:
            moveBallX = 0
            moveBallY = 0
            moveBall = False
            ballY = barY - ballRadius
            if len(lifeList) ==0:
                Flag = False
            else:
                Flag = True
        elif ballX > width - (ballRadius *2):
            moveBallX = -1
        elif ballX < 0:
            moveBallX = 1

        if barX < -barWidth:
            barX = width
        elif barX > width:
            barX = 0

        barX += barmoveX
        ballY += moveBallY
        ballX += moveBallX

        if len(lifeList) == 0:
            gameOver()
            main.home_screen()
        elif len(brickList) == 0:
            moveBallY =0
            moveBallX = 0
            win()
            main.home_screen()

        clock.tick(FPS)
        pygame.display.update()


