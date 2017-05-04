#!/bin/python

import argparse
import urllib.request
import re
import robotApp
from linkedList import linkedList



def main():

    #test STACK ADT using array and LinkedList

    objGrid = [[1], [2], [3]]
    objGrid1 = [[2], [2], [3]]

    ll = linkedList()
    ll.add(objGrid)
    ll.add(objGrid1)
    result = ll.is_empty()
    headres = ll.head()
    getheadelement = ll.head().get_element()
    containRes = ll.contains(objGrid)
    ll.remove(objGrid1)


    #Create World

    objFinish, objStart, arr, objGrid, a2d = robotApp.create_world("world1.txt")
    #Print World
    print("Below is the initial grid")
    robotApp.printf(a2d)

    #Find Robot
    p1,p2 = robotApp.where_is_robot(a2d,objGrid)

    #Try Move to a walled square

    print("Try Move to a walled square 1,7")
    destination = [[1], [7]]
    robotApp.move_robot(a2d,destination,objGrid)
    destination = [[5], [7]]
    robotApp.move_robot(a2d, destination, objGrid)
    destination = [[2], [5]]
    robotApp.move_robot(a2d, destination, objGrid)
    destination = [[3], [1]]
    robotApp.move_robot(a2d, destination, objGrid)
    destination = [[0], [7]]
    robotApp.move_robot(a2d, destination, objGrid)
    robotApp.where_is_robot(a2d, objGrid)
    robotApp.goal_reached(a2d,destination)
    robotApp.printf(a2d)

    #Find Shortest Path

    objFinish, objStart, arr, objGrid, maze = robotApp.create_world("world1.txt")
    start = [[objStart[1]],[objStart[2]]]
    end = [[objFinish[1]], [objFinish[2]]]


    res = robotApp.searchMaze(maze, start, end, objGrid)


    print("Below is result of searching the Maze")
    #Print World

    robotApp.printf(maze)

    return


if __name__ == '__main__':
    main()