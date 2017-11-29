#!/usr/bin/env python2.7
#encoding:utf-8
import sys

class Point():

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

def prisoner_or_citizen(list_coordinates, pf):
        result = 0
        for v in range(len(list_coordinates) - 1):
            v1, v2 = list_coordinates[v], list_coordinates[v + 1]
            cross_product = ((v2.x - v1.x) * (pf.y - v1.y)) - ((v2.y - v1.y) * (pf.x - v1.x))
            # print cross_product
            if cross_product > 0:
                result += 1
            elif cross_product < 0:
                result -= 1
            elif cross_product == 0:
                return False
        if result != 0:
            return False
        else:
            return True

def main():
    lines = open(sys.argv[1], 'r')
    n=0
    for l in lines:
        n+=1
        c, p = l.split('|')
        coordinates = c.split(',')
        pf = p.rstrip().strip().split(' ')
        pf = Point(pf[0], pf[1])
        list_coordinates = list()
        for coordinate in coordinates:
            point = coordinate.strip(' ').split(' ')
            point = [int(p) for p in point]
            if (point[0] >= 0 and point[0] <=10) and (point[1] >= 0 and point[1] <=10) :
                list_coordinates.append(Point(point[0], point[1]))
            else:
                raise Exception("linea {} de file txt:Numero de coordenada no esta entre 0-10".format(n))
        if len(list_coordinates) >= 3 and len(list_coordinates) <= 12:
            list_coordinates.append(list_coordinates[0])
            if prisoner_or_citizen(list_coordinates, pf):
                print 'ciudadano'
            else:
                print 'prisionero'
        else:
            raise Exception("linea {} de file txt: Cantidad de coordenadas de una prision no esta como min 3, max 12".format(n))


if __name__ == '__main__':
    main()
