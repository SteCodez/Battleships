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

ship_placement = []

while num_ships != ships_placed:
    random_row = random.randint(0, rows -1)
    random_col = random.randint(0, col -1)
    direction = random.choice(["left", "right", "up", "down"])
    ship_size = random.randint(2, 5)
    if grid_placer(random_row, random_col, direction, ship_size):
            ships_placed += 1