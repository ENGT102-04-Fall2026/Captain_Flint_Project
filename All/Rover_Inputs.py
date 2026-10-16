import csv

# 1. Variables

position = (0,0)
battery = 100
integrity = 100
clue_score = 0
search_over = False
searched_location = set()
history = list()

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
    