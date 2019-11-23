import brickgame
import pygame
pygame.init()

width = 1000
height = 500

screen = pygame.display.set_mode((width, height))
red = 255, 0, 0
blue = 0, 0, 255
green = 0, 255, 0
black = 0, 0, 0
white = 255, 255, 255
screen.fill(white)


def start_game():
    font = pygame.font.SysFont(None, 75)
    text = font.render("PRESS SPACE TO START THE GAME", True, black)
    screen.blit(text, (40, height / 2 - 50))
    font1 = pygame.font.SysFont(None, 30)
    text1 = font1.render("PRESS SPACE TO RELEASE THE BALL AND ARROW KEYS TO MOVE THE BAR", True, black)
    screen.blit(text1, (120, height / 2 + 20))


def home_screen():
    while True:
        screen.fill(white)
        start_game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    brickgame.game()

        pygame.display.update()


if __name__ == '__main__':
    home_screen()
