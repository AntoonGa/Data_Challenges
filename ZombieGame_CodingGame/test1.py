# -*- coding: utf-8 -*-
"""
Zombie game on CodingGame
"""

import sys
import math

# Save humans, destroy zombies!

def human_zombie_distance(x_human, y_human, x_zombie, y_zombie):   
    # find distance from human to zombie 
    distance = (x_human - x_zombie)**2 + (y_human - y_zombie)**2
    distance = distance ** (0.5)
    return distance

def min_distance(humans_hashmap, zombies_hashmap):
    smallest_distance = 1e10
    target_position_x, target_position_y = 0, 0

    for human_id in humans_hashmap.keys():
        human_x, human_y = humans_hashmap[human_id]
        for zombie_id in zombies_hashmap.keys():
            _, _ , zombie_x, zombie_y, = zombies_hashmap[zombie_id]

            distance = human_zombie_distance(human_x, human_y,zombie_x, zombie_y)
            if distance <= smallest_distance:
                smallest_distance = distance
                target_position_x, target_position_y = human_x, human_y
            
    return smallest_distance, target_position_x, target_position_y


# game loop
while True:
    x, y = [int(i) for i in input().split()]

    # loading human coordinates into hashmap
    humans = {}
    human_count = int(input())
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        humans[human_id] = [human_x, human_y]

    # loading zombies coordinates into hashmap
    zombies = {}
    zombie_count = int(input())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        zombies[zombie_id] = [zombie_x, zombie_y, zombie_xnext, zombie_ynext]

    smallest_distance, target_position_x, target_position_y = min_distance(humans, zombies)

    print(target_position_x, target_position_y)
