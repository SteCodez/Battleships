import random

grid = [[]]
map_size = 15
num_ships = 4
bullets_left = 25
game_over = False
ships_sunk = 0
ship_placement = [[]]
grid_letters = "ABCDEFGHIJ"

def generate_map():
    
    rows, cols = (map_size, map_size)
    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append("~")
        grid.append(row)
           
ships_placed = 0