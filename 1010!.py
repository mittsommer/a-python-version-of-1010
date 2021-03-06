import random
import sys
import numpy as np
import pygame
import objectlib
import time

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

bg = 'image/bg.png'
blue = 'image/blue.png'
yellow = 'image/yellow.png'
pink = 'image/pink.png'
green = 'image/green.png'
red = 'image/red.png'
orange = 'image/orange.png'
cyan = 'image/cyan.png'
purple = "image/purple.png"

bg_image = pygame.image.load(bg)
blue_image = pygame.image.load(blue)
yellow_image = pygame.image.load(yellow)
pink_image = pygame.image.load(pink)
green_image = pygame.image.load(green)
red_image = pygame.image.load(red)
orange_image = pygame.image.load(orange)
cyan_image = pygame.image.load(cyan)
purple_image = pygame.image.load(purple)

color_lib = {'bg': bg_image, 'blue': blue_image, 'yellow': yellow_image, 'pink': pink_image, 'green': green_image,
             'red': red_image, 'orange': orange_image, 'cyan': cyan_image, 'purple': purple_image}

gameover = pygame.image.load('image/gameover.png')
gameover_rect = gameover.get_rect()


class Map:
    def __init__(self):
        self.netz = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ]
        self.netz_color = [['bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg'],
                           ['bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg'],
                           ['bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg'],
                           ['bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg'],
                           ['bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg'],
                           ['bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg'],
                           ['bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg'],
                           ['bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg'],
                           ['bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg'],
                           ['bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg', 'bg']
                           ]

        self.bg_image = pygame.image.load(bg)
        self.score = 0
        self.score_font = pygame.font.SysFont('microsoft Yahei', 40)

    def canput(self, object, row, line):
        if np.shape(object)[0] + row <= 10 and np.shape(object)[1] + line <= 10:
            pass
        else:
            # print('unable to set here1')
            return False
        for i in range(len(object)):
            for j in range(len(object[i])):
                if not (self.netz[row + i][line + j] and object[i][j]):
                    canput = True
                else:
                    # print('unable to set here2')
                    return False
        return canput

    def set(self, shape, row, line, color):
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                self.netz[row + i][line + j] += shape[i][j]
                if shape[i][j] == 1:
                    self.netz_color[row + i][line + j] = color

    def check_eliminate(self):
        for i in range(10):
            if self.netz[i] == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
                for j in range(10):
                    self.netz[i][j] = 0
                    self.netz_color[i][j] = 'bg'
                    self.score += 1
        for i in range(10):
            line = [j[i] for j in self.netz]
            if line == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
                for j in range(10):
                    self.netz[j][i] = 0
                    self.netz_color[j][i] = 'bg'
                    self.score += 1

    def buildmap(self, display):
        y = 100
        for i in range(10):
            x = 100
            for j in range(10):
                display.blit(self.get_color_image(self.netz_color[i][j]), (x, y))  # 根据颜色矩阵放置不同颜色的色块
                x = x + 40
            y = y + 40

    def get_color_image(self, color):
        color_image = color_lib[color]
        return color_image

    def show_score(self, display):
        font_surface = self.score_font.render(('SCORE: ' + str(self.score)), False, (255, 200, 10))
        display.blit(font_surface, (230, 20))


class Square:
    def square_gen(self):
        self.shape, self.color = np.array(random.choice(objectlib.objectlib), dtype=object)  # 随机创建图形
        self.color_image = color_lib[self.color]
        self.color_rect = self.color_image.get_rect()

    def blitsquare(self, display, pos):
        y = pos[1]
        for i in self.shape:
            x = pos[0]
            for j in i:
                if j == 1:
                    self.color_rect.left = x
                    self.color_rect.top = y
                    display.blit(self.color_image, self.color_rect)
                x = x + 40
            y = y + 40


def check_gameover(map, display, sq):
    gamecon = False
    for row in range(10):
        for line in range(10):
            gamecon = map.canput(sq.shape, row, line) or gamecon
    if not gamecon:
        gameover_rect.left, gameover_rect.top = 0, 300
        display.blit(gameover, gameover_rect)


def run_game():
    pygame.init()
    display = pygame.display.set_mode((600, 800))
    pygame.display.set_caption('1010!')
    map = Map()
    sq = Square()
    sq.square_gen()
    click = False
    clock = pygame.time.Clock()
    pickup = False

    while True:
        set = False
        display.fill(BLACK)
        map.buildmap(display)
        map.show_score(display)
        check_gameover(map, display, sq)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                square = sq.shape
                if 300 <= x <= 300 + len(square[0]) * 40 and 600 <= y <= 600 + len(square) * 40:
                    click = True
                    pickup = True
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if not (80 <= x <= 520 and 80 <= y <= 520):
                    pickup = False
                click = False
                if pickup:
                    set = True
        if set:
            x, y = pygame.mouse.get_pos()
            row = round(10 * (y - 100) / 400)
            line = round(10 * (x - 100) / 400)
            if map.canput(sq.shape, row, line):
                map.set(sq.shape, row, line, sq.color)
                map.check_eliminate()
                sq.square_gen()
        if not click:
            sq.blitsquare(display, (300, 600))
        elif click:
            x, y = pygame.mouse.get_pos()
            sq.blitsquare(display, (x, y))
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    run_game()
