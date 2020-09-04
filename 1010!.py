import random
import sys
import numpy as np
import pygame
import objectlib
import time

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
bg = pygame.image.load('image/gray.png')


class Map():
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

    def canput(self, object, row, line):
        if np.shape(object)[0] + row <= 10 and np.shape(object)[1] + line <= 10:
            pass
        else:
            #print('unable to set here1')
            return False
        for i in range(len(object)):
            for j in range(len(object[i])):
                if not (self.netz[row + i][line + j] and object[i][j]):
                    canput = True
                else:
                    #print('unable to set here2')
                    return False
        return canput


    def set(self,object,row,line):
        for i in range(len(object)):
            self.netz[row + i][line:line + len(object[i])] += object[i]



    def check_eliminate(self):
        eliminate = False
        for i in range(10):
            if self.netz[i] == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
                for j in range(10):
                    self.netz[i][j] = 0
                    eliminate = True
        for i in range(10):
            line = [j[i] for j in self.netz]
            if line == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
                for j in range(10):
                    self.netz[j][i] = 0
                    eliminate = True
        return eliminate
    def buildmap(self, bg, pinksq, display):
        y = 100
        for i in self.netz:
            x = 100
            for j in i:
                if j == 0:
                    display.blit(bg, (x, y))# 矩阵为0的位置放置背景色块
                else:
                    display.blit(pinksq, (x, y))  # 矩阵为1的位置放置颜色色块
                x = x + 40
            y = y + 40


class Square():
    def Square_gen(self):
        self.shape = np.array(random.choice(objectlib.objectlib))  # 随机创建图形

    def blitsquare(self, display, pos, pinksq, pinksq_rect):
        y = pos[1]
        for i in self.shape:
            x = pos[0]
            for j in i:
                if j == 1:
                    pinksq_rect.left = x
                    pinksq_rect.top = y
                    display.blit(pinksq, pinksq_rect)
                x = x + 40
            y = y + 40


def run_game():
    pinksq = pygame.image.load('image/pink.png')
    pinksq_rect = pinksq.get_rect()
    gameover = pygame.image.load('image/gameover.png')
    gameover_rect = gameover.get_rect()
    pygame.init()
    display = pygame.display.set_mode((600, 800))
    pygame.display.set_caption('1010!')
    map = Map()
    sq = Square()
    sq.Square_gen()
    click = False
    clock = pygame.time.Clock()
    pickup = False

    while True:
        set = False
        display.fill(BLACK)
        map.buildmap(bg, pinksq, display)
        gamecon = False
        for row in range(10):
            for line in range(10):
                gamecon = map.canput(sq.shape, row, line) or gamecon
        if not gamecon:
            gameover_rect.left, gameover_rect.top = 0, 300
            display.blit(gameover, gameover_rect)

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
                map.set(sq.shape, row, line)
                map.check_eliminate()
                sq.Square_gen()
        if not click:
            sq.blitsquare(display, (300, 600), pinksq, pinksq_rect)
        elif click:
            x, y = pygame.mouse.get_pos()
            sq.blitsquare(display, (x, y), pinksq, pinksq_rect)
        pygame.display.flip()
        #clock.tick(30)


run_game()
