import pygame
from pygame import *
import time

def main():
    screen = pygame.display.set_mode((320, 568), 0, 32)
    backgrand = pygame.image.load("./image/background_1.png")
    screen.blit(backgrand, (0, 0))

    my_planr = pygame.image.load("./image/我的飞机.gif")
    screen.blit(my_planr, (120, 400))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        get_pass = key.get_pressed()
        if get_pass[K_w] or get_pass[K_UP]:
            print("上")
        if get_pass[K_s] or get_pass[K_DOWN]:
            print("下")
        if get_pass[K_a] or get_pass[K_LEFT]:
            print("左")
        if get_pass[K_d] or get_pass[K_RIGHT]:
            print("右")
        # if get_pass[K_] or get_pass[K_]:
        #     print("上")
        pygame.display.update()

        time.sleep(0.01)




if __name__ == '__main__':
    main()