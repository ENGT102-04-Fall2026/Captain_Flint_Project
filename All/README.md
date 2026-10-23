# Captain_Flint_Project

09/25/26
Pseudocode was written. Main components of the code consist of 5 components.
1. Variables
2. The main loop
3. Movement
4. Failure (If the battery or the hull integrity is low)
5. The search itself
6. Final verdict

Once these main components are coded, more specifics such as clue calculations, danger advice, or levels to hull integrity/battery power (Ex battery <= 30, it sends out a warning instead of ending completely) can be implemented for efficiency. 

Update 2 - Wk 6

 - Basic rover inputs were created
 - Variables Identified
 - figuring out how to connect map with rover
    - inital code didn't work, needed more research reguarding what specific code, where to put it, and how to connect it with the rover
 - fixed map setup, loading map, and started on the main loop
 - A lot of typos led to failure
    - "pos" not identified as position
    - battery vs Battery, etc

Update 3 - Wk 7

 - Added Fail and Success checks
 - Changed input variation
    - Added Target coords
 - Fixed code slightly
 - Not major change, needs to fix minor errors, add CSV add clue/hazard directory, + More

 Update 4 - Wk 8

 - Most major changes to code:
  - Added a new load_map(filename) that reads the CSV into a dictionary keyed by (x, y) coordinates instead of a plain list of rows.
  - Each location stores at_location, description, depth, distance, and time, converted to int or float.
  - pos = target_pos is now position = target_pos, so the rover actually moves.
 - more polish needs to be done reguarding continuity with load map, mission training, coordinates, hazard/clue