## Display
The village and king's health is displayed on screen
## Instructions

Here we are going to use Python 3:

- In the directory, where game is stored, open the terminal and type `python game.py`.
- Press `q` to quit the game.
- Press `a` to move the king to the left.
- Press `d` to move the king to the right.
- Press `s` to move the king to the bottom.
- Press `w` to move the king to the up.
- Press `z` to relase barbarian
- Press `x` to relase barbarian
- Press `c` to relase barbarian
- Press `v` for rage spell
- Press `b` for heal spell
- The game will end when:
  - at any given instance there isn't any enemy in the board termed as defeat
  - all the buildings excluding walls are removed is termed as victory

## Assumptions
- Every time v is pressed speed, damage becomes twice
- There is no limit on the number of barbarians.
- Distance is calculated using the formula `|x2-x1| + |y2-y1|`.
- Cannon has energy which recharges every 10th time, if there isn't any object in the radius of cannon the cannon looses its energy. Basically shooting at empty area.

## Bonus
Implemented axe of king which has radius 3 units which isn't hardcode and can be easily modified