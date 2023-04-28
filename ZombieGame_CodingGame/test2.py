import sys
import math

# Save humans, destroy zombies!

def human_zombie_distance(x_human, y_human, x_zombie, y_zombie):   
    # find distance from human to zombie 
    distance = (x_human - x_zombie)**2 + (y_human - y_zombie)**2
    distance = distance ** (0.5)
    return distance

def min_distance(humans_hashmap, zombies_hashmap):
    # find the couple (human-zombie) with minimum distance (next TURN !!)
    smallest_distance = 1e10
    closest_human = 0
    closest_zombie = 0

    for human_id in humans_hashmap.keys():
        human_x, human_y = humans_hashmap[human_id]
        for zombie_id in zombies_hashmap.keys():
            _, _ , zombie_x, zombie_y, = zombies_hashmap[zombie_id]

            distance = human_zombie_distance(human_x, human_y,zombie_x, zombie_y)
            if distance <= smallest_distance:
                smallest_distance = distance
                closest_human = human_id
                closest_zombie = zombie_id
  
    return smallest_distance, closest_human, closest_zombie

def find_barycenter(x_human, y_human, x_zombie, y_zombie):

    barycenter_x = (x_human + x_zombie) / 2
    barycenter_y = (y_human + y_zombie) / 2

    return barycenter_x, barycenter_y


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

    smallest_distance, closest_human, closest_zombie = min_distance(humans, zombies)

    x_human, y_human   = humans[closest_human]
    _,_, x_zombie, y_zombie = zombies[closest_zombie] 

    target_position_x, target_position_y = find_barycenter(x_human, y_human, x_zombie, y_zombie)

    print(int(target_position_x), int(target_position_y))
