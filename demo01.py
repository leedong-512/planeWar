import pygame
from pygame import *
import time

class Plane(object):
    def __init__(self, screen):
        self.x = 180
        self.y = 600
        self.plane_img = pygame.image.load(r"./image/hero1.png")
        self.speed = 10
        self.screen = screen
        self.bullets = []

    def display(self):
        self.screen.blit(self.plane_img, (self.x, self.y))
        for bullet in self.bullets:
            bullet.auto_move()
            bullet.display()

    def ctrl_plane(self):
        get_pass = key.get_pressed()
        if get_pass[K_w] or get_pass[K_UP]:
            print("上")
            self.y -= self.speed
        if get_pass[K_s] or get_pass[K_DOWN]:
            self.y += self.speed
            print("下")
        if get_pass[K_a] or get_pass[K_LEFT]:
            self.x -= self.speed
            print("左")
        if get_pass[K_d] or get_pass[K_RIGHT]:
            self.x += self.speed
            print("右")
        if get_pass[K_SPACE]:
            bullet = Bullet(self.screen, self.x, self.y)
            self.bullets.append(bullet)


class Bullet(object):
    def __init__(self, screen, x, y):
        self.x = x + 48
        self.y = y - 20
        self.screen = screen
        self.bullet_img = pygame.image.load(r"./image/bullet1.png")
        self.speed = 5

    def display(self):
        self.screen.blit(self.bullet_img, (self.x, self.y))

    def auto_move(self):
        self.y -= self.speed
def main():
    screen = pygame.display.set_mode((480, 852), 0, 32)
    backgrand = pygame.image.load(r"./image/background.png")
    planer = Plane(screen)
    while True:
        screen.blit(backgrand, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        planer.ctrl_plane()
        planer.display()
        pygame.display.update()

        time.sleep(0.02)



if __name__ == '__main__':
    main()
