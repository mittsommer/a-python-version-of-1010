import random
import numpy as np
from objectlib import objectlib


class map():
    def build(self):
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

    def set(self, object, row, line):
        if np.shape(object)[0]+row <= 10 and np.shape(object)[1]+line <= 10:
            pass
        else:
            print('unable to set here1')
            return
        for i in range(len(object)):
            for j in range(len(object[i])):
                if self.netz[row + i][line + j] == 0:
                    if object[i][j] == 1:
                        self.netz[row + i][line + j] = 1
                    else:
                        continue
                else:
                    print('unable to set here2')
                    return

    def check_eliminate(self):
        for i in range(10):
            if self.netz[i] == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
                self.netz[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(10):
            if self.netz[:][i] == [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]:
                self.netz[:][i] = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]

    def showmap(self):
        for i in range(10):
            print(map.netz[i])


class object_generator():
    def randompick(self):
        self.shape = np.array(random.choice(objectlib))

    def showobject(self):
        print(self.shape)


if __name__ == '__main__':
    map = map()
    map.build()
    ob = object_generator()
    ob.randompick()
    ob.showobject()
    map.set(ob.shape, 6, 6)
    map.showmap()
    map.check_eliminate()
    map.showmap()
