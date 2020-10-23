import pygame
import random
from pygame.draw import *
from random import randint

pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
LIGHT_BLUE = (50, 204, 255)
LIGHT_GREY = (240, 240, 250)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class Score:

    def __init__(self):
        self.score = 0

    def increase(self, points):
        self.score += points

    def decrease(self):
        self.score -= self.score

    def text(self):
        surface_score = pygame.font.SysFont('Helvetic', 100).render(str(self.score), False, BLACK)
        screen.blit(surface_score, (50, 50))

    def hello(self):
        surface_hi = pygame.font.SysFont('Helvetic', 500).render('Do not touch my car', False, BLACK)
        screen.blit(surface_hi, (200, 200))


class Ball(object):

    def __init__(self):
        self.color = random.choice(COLORS)
        self.x = randint(100, 1000)
        self.y = randint(100, 800)
        self.r = randint(30, 50)
        self.speed_x = randint(-100, 100)
        self.speed_y = randint(-100, 100)

    def draw_ball(self):
        circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        self.x += self.speed_x / FPS
        self.y += self.speed_y / FPS
        self.draw_ball()
        if self.x >= 1100:
            self.speed_x = randint(-100, -10)
        if self.x <= 50:
            self.speed_x = randint(10, 100)
        if self.y >= 800:
            self.speed_y = randint(-100, -10)
        if self.y <= 50:
            self.speed_y = randint(10, 100)

    def click(self, pos):
        x, y = pos
        if (self.x - x) ** 2 + (self.y - y) ** 2 <= self.r ** 2:
            self.color = random.choice(COLORS)
            self.x = randint(100, 1000)
            self.y = randint(100, 800)
            self.r = randint(30, 50)
            self.speed_x = randint(-100, 100)
            self.speed_y = randint(-100, 100)
            return True
        else:
            return False


class Aim(object):

    def __init__(self):
        self.color = random.choice(COLORS)
        self.x = randint(100, 1000)
        self.y = randint(100, 800)
        self.r = randint(50, 200)
        self.speed_x = randint(-200, 200)
        self.speed_y = randint(-200, 200)

    def draw_aim(self):
        polygon(screen, self.color, [(self.x, self.y), (self.x + self.r * 1.71 / 2, self.y - self.r / 2),
                                     (self.x + self.r * 1.71, self.y), (self.x + self.r * 1.71, self.y + self.r),
                                     (self.x + self.r * 1.71 / 2, self.y + 3 * self.r / 2), (self.x, self.y + self.r)])

    def move_aim(self):
        self.color = random.choice(COLORS)
        self.x += 3 * self.speed_x / FPS
        self.y += 3 * self.speed_y / FPS
        self.r -= 1
        self.draw_aim()
        if self.r <= 10:
            self.color = random.choice(COLORS)
            self.x = randint(100, 1000)
            self.y = randint(100, 800)
            self.r = randint(50, 100)
            self.speed_x = randint(-200, 200)
            self.speed_y = randint(-200, 200)
        if self.x >= 1100:
            self.speed_x = randint(-100, -10)
        if self.x <= 50:
            self.speed_x = randint(10, 100)
        if self.y >= 800:
            self.speed_y = randint(-100, -10)
        if self.y <= 50:
            self.speed_y = randint(10, 100)

    def click_aim(self, pos):
        x, y = pos
        if (self.x - x) ** 2 + (self.y - y) ** 2 <= self.r ** 2:
            self.color = random.choice(COLORS)
            self.x = randint(100, 1000)
            self.y = randint(100, 800)
            self.r = randint(50, 100)
            self.speed_x = randint(-200, 200)
            self.speed_y = randint(-200, 200)
            return True
        else:
            return False


class Car(object):

    def __init__(self):
        self.x = randint(200, 500)
        self.y = randint(200, 500)
        self.h = randint(10, 50)
        self.dir = 1
        self.speed_x = randint(10, 200)

    def draw_car(self):
        a = self.h / 50
        ellipse(screen, BLACK, (self.x - 15 * a, self.y + 35 * a, 30 * a, 10 * a))
        rect(screen, LIGHT_BLUE, (self.x, self.y, self.dir * 260 * a, self.h))
        rect(screen, LIGHT_BLUE, (self.x + self.dir * 40 * a, self.y - 40 * a, self.dir * 130 * a, 40 * a))
        rect(screen, LIGHT_GREY, (self.x + self.dir * 50 * a, self.y - 30 * a, self.dir * 45 * a, 30 * a))
        rect(screen, LIGHT_GREY, (self.x + self.dir * 120 * a, self.y - 30 * a, self.dir * 48 * a, 30 * a))
        rect(screen, LIGHT_GREY, (self.x + self.dir * 248 * a, self.y + 2 * a, self.dir * 10 * a, 10 * a))
        circle(screen, BLACK, (self.x + self.dir * int(220 * a), self.y + int(50 * a)), int(25 * a))
        circle(screen, BLACK, (self.x + self.dir * int(50 * a), self.y + int(50 * a)), int(25 * a))

    def move_car(self):
        a = self.h / 50
        self.x += self.speed_x / FPS
        if self.x + 170 * a >= 1100:
            self.dir = -1
            self.speed_x = -self.speed_x
        if self.x - 170 * a <= 50:
            self.dir = 1
            self.speed_x = -self.speed_x

    def click_car(self, pos):
        a = self.h / 50
        x, y = pos
        if ((x > self.x) and (x < self.x + 260 * a) and (y > self.y - 40 * a)
                and (y < self.y + self.h + 25 * a)):
            self.x = randint(200, 500)
            self.y = randint(200, 500)
            self.h = randint(10, 50)
            self.dir = 1
            self.speed_x = randint(10, 200)
            return True
        else:
            return False


pygame.display.update()
clock = pygame.time.Clock()
finished = False
score = Score()
balls = [Ball() for i in range(10)]
aims = [Aim() for j in range(3)]
cars = [Car() for k in range(1)]

while not finished:
    clock.tick(FPS)
    for ball in balls:
        ball.move()
        ball.draw_ball()
    for aim in aims:
        aim.move_aim()
        aim.draw_aim()
    for car in cars:
        car.draw_car()
        car.move_car()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                if ball.click(event.pos):
                    score.increase(1)
            for aim in aims:
                if aim.click_aim(event.pos):
                    score.increase(int(100 / aim.r))
            for car in cars:
                if car.click_car(event.pos):
                    score.decrease()
    score.text()

    pygame.display.update()
    screen.fill(WHITE)

pygame.quit()