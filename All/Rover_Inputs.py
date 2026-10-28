# Import csu and load into dictionary
import csv
import os
import matplotlib.pyplot as plt

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

filename = input("Mission file [data/mission_training.csv]: ").strip()
if filename == "":
    filename = "data/mission_training.csv"
grid = load_map(filename)

num_cols = max(x for x, y in grid) + 1
num_rows = max(y for x, y in grid) + 1

# 1. Variables

SEARCH_EFFECTS = {
    "Low Hazard":      (-5,  -5,  0),
    "Medium Hazard":   (-10, -5,  0),
    "High Hazard":     (-15, -10, 0),
    "Low Value Clue":  (-5,  -5,  1),
    "Strong Clue":     (-2,  -5,  2),
    "High Value Clue": (-2,  -2,  3),
    "None":            (-2,  -5,  0),
}

SIMPLE_NAMES = {
    "Low Hazard": "Hazard", "Medium Hazard": "Hazard", "High Hazard": "Hazard",
    "Low Value Clue": "Clue", "Strong Clue": "Clue", "High Value Clue": "Clue",
    "None": "Nothing", "Treasure": "Treasure",
}

position = (0,0)
battery = 100
integrity = 100
clue_score = 0
search_over = False
searched_location = set()
outcome = ""

current_depth = grid[(0, 0)]["depth"]  
total_time = 0.0

history = [(0.0, battery, integrity)]

# Coordinate functions
directions = {
    'forward':  (0, 1),    # y + 1
    'backward': (0, -1),   # y - 1
    'right':    (1, 0),    # x + 1
    'left':     (-1, 0),   # x - 1
}

def get_target_coords(current_pos, cmd):
    x, y = current_pos
    dx, dy = directions[cmd]
    return (x + dx, y + dy)

def is_within_bounds(target_pos):
    x, y = target_pos
    return 0 <= x < max_cols and 0 <= y < max_rows


# 2. Map setup
def load_map(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        return [row for row in reader]

def update_plot():
    times = [h[0] for h in history]
    energy_vals = [h[1] for h in history]
    hull_vals = [h[2] for h in history]
    plt.clf()
    ax1 = plt.gca()
    ax2 = ax1.twinx()
    line1, = ax1.plot(times, energy_vals, color="tab:blue", label="Energy remaining (%)")
    line2, = ax2.plot(times, hull_vals, color="tab:red", label="Hull integrity (%)")
    ax1.set_xlabel("Total mission time (min)")
    ax1.set_ylabel("Energy remaining (%)")
    ax2.set_ylabel("Hull integrity (%)")
    ax1.set_title("Captain Flint Recovery Mission: Rover Status")
    ax1.legend(handles=[line1, line2], loc="best")
    plt.pause(0.1)


# 3. Main Loop

while True:
    print(f"Current Position: {position}, Battery: {battery:.2f}%, Hull: {integrity:.2f}%")

   cmd = input("Move (Forward/Backward/Right/Left): ").strip().lower()
    if cmd not in directions:
        print("Unsupported direction. Use Forward, Backward, Right, or Left.")
        continue
    target_pos = get_target_coords(position, cmd)
    if not is_within_bounds(target_pos):
        print("Outside perimeter. No changes applied.")
        continue

 dest = grid[target_pos]
    depth_change = abs(dest["depth"] - current_depth)       # uses the OLD depth
    hull_loss = depth_change * 0.8 * dest["time"]
    energy_loss = depth_change * 0.5 + (dest["distance"] / dest["time"]) * 1.2
 
    integrity -= hull_loss
    battery -= energy_loss
    total_time += dest["time"]
    position = target_pos
    current_depth = dest["depth"]
 
    history.append((total_time, battery, integrity))
    update_plot()
    print(f"Energy loss: {energy_loss:.2f} | Hull loss: {hull_loss:.2f}")
    print_status()

# 4. Outcomes


 # search command 
 if not ask_yes_no("Search this location? (yes/no): "):
        continue
    if position in searched_location:
        print("This location was already searched. No effects applied.")
        continue
 searched_location.add(position)
    category = dest["at_location"]
    print(f"Discovery: {SIMPLE_NAMES[category]} - {dest['description']}")

 if is_failure():                                    
        outcome = "FAILURE"
        break

  if category == "Treasure":                           
        outcome = "SUCCESS (Treasure)"
        break

hull_change, energy_change, clue_change = SEARCH_EFFECTS[category]
    integrity += hull_change
    battery += energy_change
    clue_score += clue_change
 
    history[-1] = (total_time, battery, integrity)        
    update_plot()
    print_status()

     if is_failure():                                        # failure FIRST (SYS-08)
        outcome = "FAILURE"
        break
    if clue_score >= 6:                                     # clue success SECOND
        outcome = "SUCCESS (Clues)"
        break

# Ending stuff
if outcome == "FAILURE":
    print("MISSION FAILED: energy/hull failed")
elif outcome == "SUCCESS (Treasure)":
    print("MISSION SUCCESS")
else:
    print("MISSION SUCCESS: enough clues gathered.")

# Summary

print("\n===== FINAL SUMMARY =====")
print(f"Outcome: {outcome}")
print(f"Final coordinate: {position}")
print(f"Total time: {total_time:.1f} min")
print(f"Battery remaining: {battery:.2f}%")
print(f"Hull integrity: {integrity:.2f}%")
print(f"Clue score: {clue_score}")
print(f"Locations searched: {len(searched_location)}")

update_plot()
os.makedirs("plots", exist_ok=True)        
plt.savefig("plots/final_status_plot.png")
plt.ioff()