# Robot Vacuum Cleaner  

## Overview  
This project simulates a **robotic vacuum cleaner** using Python. The robot navigates a room, identifies dirty spots (`*`), and cleans them by moving strategically. The simulation ensures that the robot behaves rationally, efficiently targeting dirty spots and moving to the next row when the current row is clean.

---

## Features  
- **Row-by-Row Cleaning**:  
  The robot scans its current row for dirty spots.  
  - If dirty spots exist, it moves left or right to clean them.  
  - If the row is clean, the robot moves down to the next row.  

- **Rational Behavior**:  
  - The robot only moves when necessary.  
  - Prioritizes cleaning over unnecessary movement.  

- **Simulation Display**:  
  - The board is displayed after every move, showing the robot’s progress.  

- **Goal-Oriented**:  
  - The robot stops once all dirty spots have been cleaned.  

---

## How It Works  
- **Symbols on the Board**:  
  - `*`: Dirty spot.  
  - `.`: Clean spot.  
  - `@`: Robot’s position on a clean spot.  
  - `!`: Robot’s position on a dirty spot (just before cleaning it).  

- **Behavior**:  
  1. If the robot is on a dirty spot (`!`), it cleans it by converting it to a clean spot (`@`).  
  2. If there are dirty spots (`*`) in the current row:  
     - Moves left or right to clean them.  
  3. If the row is clean, the robot moves **down** to the next row.  

- **Room Boundaries**:  
  - The robot checks for out-of-bounds movement to avoid errors.  

---

## How to Run  
1. **Requirements**:  
   - A valid text file representing the room layout (e.g., `room2.txt`).

2. **Input File Format**:  
   - The room layout should be a grid with symbols, and the initial robot location must be in the top row. Example for a grid:  
     ```
@ * . . . *
. . * . . .
. . . . .
. . * .
. * .
     ```
