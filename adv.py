from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
path = []
visited = {}
direction = {'n':'s', 's':'n', 'e':'w', 'w':'e'}

visited[ player.current_room.id] = player.current_room.get_exits()

while len( visited) < len( room_graph) - 1:
    """
    While visited list is less than rooms in graph:
        check if room has been visited or all paths have been explored,
    otherwise, default behaviour:
        add first unexplored direction to traversal_path,
        explore new room
    """
    ...
    if player.current_room.id not in visited:
        """ 
        If room not visited yet: 
        build hashtable of possible exits at room id's index in visited,
        remove last direction traversed from potential paths
        """
        visited[ player.current_room.id] = player.current_room.get_exits()
        prev_direction = path[ -1]
        visited[ player.current_room.id].remove( prev_direction)
    while len( visited[ player.current_room.id]) == 0:
        """
        while all paths have been explored:
        backtrack to previous room until an open path is found
        """
        prev_direction = path.pop()
        traversal_path.append( prev_direction)
        player.travel( prev_direction)

#    direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

    move = visited[ player.current_room.id].pop(0)
    traversal_path.append( move)
    path.append( direction[ move])
    player.travel( move)

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
