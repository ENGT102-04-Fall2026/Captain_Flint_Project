# Import csu and load into dictionary
import csv

def load_map(filename):
    locations = {}
    with open(filename, mode='r') as file:
        for row in csv.reader(file):
            x = int(row[0])
            y = int(row[1])
            locations[(x, y)] = {
                "at_location": row[2],
                "description": row[3],
                "depth": float(row[4]),
                "distance": float(row[5]),
                "time": float(row[6]),
            }
    return locations

grid = load_map('data/mission_training.csv')

num_cols = max(x for x, y in locations) + 1
num_rows = max(y for x, y in locations) + 1

# 1. Variables

position = (0,0)
battery = 100
integrity = 100
clue_score = 0
search_over = False
searched_location = set()
history = list()

current_depth = 2.0
total_time = 0.0

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
def load_map(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        return [row for row in reader]

# Loading map
grid = load_map('mission_training.csv')
max_rows = len(grid)
max_cols = len(grid[0])

# 3. Main Loop
while search_over is False:
    print(f"Current Position: {position}, Battery: {Battery}%, Hull: {integrity}%")

    cmd = input("Move (N/S/E/W): ").strip().upper()

    target_pos = get_target_coords(position, cmd)
    if not is_within_bounds(target_pos, grid):
        print("Outside perimeter")
        continue

    position = target_pos
    battery -= 1.5
    