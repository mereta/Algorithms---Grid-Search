#!/bin/python

import argparse
import urllib.request
import re
from linkedList import linkedList



def printf(a2d):
    for a in a2d:
        print (a)


def create_world(path):

    a2d = []
    arr = list()
    objGrid = [[], [], []]
    # set size of grid, read each line from file (sep by return)
    with open(path) as buffer:

        for line in buffer:
            i=0
            f = line.split('\n')

            if f[0].startswith('goal'):
                objFinish = [[], [], []]
                objFinish[0] = "Goal"
                parse = f[0].replace(",", " ")
                val = [int(s) for s in parse.split() if s.isdigit()]

                objFinish[1] = val[0]
                objFinish[2] = val[1]
                arr.append(objFinish)

            elif f[0].startswith('r2d2'):
                objStart = [[], [], []]
                objStart[0] = "r2d2"
                parse = f[0].replace(",", " ")
                val = [int(s) for s in parse.split() if s.isdigit()]

                objStart[1] = val[0]
                objStart[2] = val[1]
                arr.append(objStart)

            elif f[0].startswith('w'):
                obj = [[], [], []]
                obj[0] = "Wall"
                parse = f[0].replace(",", " ")
                val = [int(s) for s in parse.split() if s.isdigit()]

                obj[1] = val[0]
                obj[2] = val[1]
                arr.append(obj)

            else:

                objGrid[0] = "Grid"
                parse = f[0].replace("x", " ")
                val = [int(s) for s in parse.split() if s.isdigit()]
                objGrid[1] = val[0]
                objGrid[2] = val[0]
                arr.append(objGrid)

            i += 1

    for li in arr:
        # Get Grid
        if li[0] == "Grid":
            a2d = [[0] * li[1] for _ in range(li[2])]
        # Create Wall
        if li[0] == "Wall":
            a2d[li[1]][li[2]] = 1
        # Set Robot Position
        if li[0] == "r2d2":
            a2d[li[1]][li[2]] = 2
        # Set Goal
        if li[0] == "Goal":
            a2d[li[1]][li[2]] = 3


    return objFinish, objStart,arr ,objGrid, a2d


def where_is_robot(a2d,obj):

    for i in range(0, obj[1]):
        for j in range(0, obj[2]):
            if a2d[i][j] == 2:
                print("Robot is at the Following Location: " + str([i][0]),str([j][0]))
                return int([i][0]),int([j][0])

    return False


def is_feasible(a2d, DestObj,gridsize):
    #check that number is not negative - outside grid

    if(DestObj[0][0]) < 0:
        return False
    if(DestObj[1][0]) < 0:
        return False

    # check that number is not larger than grid boundaries - outside grid
    if int(DestObj[0][0]) > int(gridsize[1] - 1):
        return False
    if int(DestObj[1][0]) > int(gridsize[2] - 1):
        return False

    if a2d[DestObj[0][0]][DestObj[1][0]] == 1:
        return False
    else:
        return True

def goal_reached(a2d, DestObj):

        if a2d[DestObj[0][0]][DestObj[1][0]] == 2:
            print('Goal Reached')
            return True
        else:
            return False


def move_robot(a2d, DestObj,objGrid):

    p1,p2 = where_is_robot(a2d,objGrid)
    result = is_feasible(a2d, DestObj, objGrid)
    if result:
        a2d[p1][p2] = 0
        a2d[DestObj[0][0]][DestObj[1][0]] = 2
        print("Robot Moved To:" + str(DestObj[0][0]) + " " + str(DestObj[1][0]))
    else:
        print("Cannot Move, Not Feasible")

def searchMaze(a2d, start_pos, finish_pos, gridSize):

    ll = linkedList()
    ll.add(start_pos)
    findPath(a2d,ll,start_pos,gridSize,start_pos,finish_pos)
    return ll.size()

def findPath(a2d, path_so_far, curPos, gridSize, start, finish):

    row = curPos[0][0]
    col = curPos[1][0]

    # Check if Feasible
    if not is_feasible(a2d,curPos,gridSize):
       return False # we've gone outside the maze

    if not curPos == start:
        if path_so_far.contains(curPos):
            return False

    # If at open path add that path to stack
    if a2d[row][col] == 0:
        path_so_far.add(curPos)
        a2d[row][col] = '-'
    # If at goal return true
    elif a2d[row][col] == 2:
        a2d[row][col] = "/"
    elif a2d[row][col] == 3:
        print("Path Size:" + str(path_so_far.size()))

        return True
    else:
        return False

    # Try moving left
    if findPath(a2d,path_so_far, [[row], [col - 1]] , gridSize, start, finish):
        return True
    # Try moving right
    elif findPath(a2d,path_so_far, [[row],[col + 1]], gridSize,start, finish):
        return True
    # Try moving up
    elif findPath(a2d, path_so_far,[[row - 1],[col]], gridSize,start, finish):
        return True
    # Try moving down
    elif findPath(a2d, path_so_far, [[row + 1],[col]], gridSize,start, finish):
        return True

    path_so_far.remove(curPos)
    return False




def main() -> object:




    return

if __name__ == '__main__':
    main()