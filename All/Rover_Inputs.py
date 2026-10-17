import csv

# 1. Variables

position = (0,0)
battery = 100
integrity = 100
clue_score = 0
search_over = False
searched_location = set()
history = list()

# Coordinate functions
def get_target_coords(current_pos, cmd):
    r, c = current_pos
    move_map = {'N': (-1, 0), 'S': (1, 0), 'E': (0,1), 'W': (0, -1)}
    dr, dc = move_map.get(cmd, (0, 0))
    return (r + dr, c + dc)
def is_within_bounds(target_pos, grid):
    r, c = target_pos
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])
# 2. Map setup
def load_map(mission_training.csv)
open('mission_training.csv', mode='r') as file:
    reader = csv.reader(file)
    return [row for row in reader]

# Loading map
    grid = load_map('mission_training.csv')
    max_rows = len(grid)
    max_cols = len(grid[0])

# 2. Main Loop
While search_over is False:
    print("current Position: {position}, Battery: {Battery}%, Hull: {integrity}%")
    cmd = input("Move (N/S/E/W): ").strip().upper()

    target_pos = get_target_coords(position, emd)
    if not is_within_bounds(target_pos, grid):
        print("Outside perimeter")
        continue

    pos = target_pos
    battery -= 1.5
    