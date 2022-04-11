## Running The Code

### Game

`python3 game.py`

### Replay

`python3 replay.py` after that enter the file name that stores the replay of the particular game

## Display
The village and king's health is displayed on screen
## Instructions

Here we are going to use Python 3:

- In the directory, where game is stored, open the terminal and type `python game.py`.
- Press `q` to quit the game.
- Press `a` to move the king/queen to the left.
- Press `d` to move the king/queen to the right.
- Press `s` to move the king/queen to the bottom.
- Press `w` to move the king/queen to the up.
- Press `z` to release barbarian
- Press `x` to release barbarian
- Press `c` to release barbarian
- Press `j` to release balloon
- Press `k` to release balloon
- Press `l` to release balloon
- Press `i` to release Archer
- Press `o` to release Archer
- Press `p` to release Archer
- Press `e` to for queen's special attack
- Press `v` for rage spell
- Press `b` for heal spell
- The game will end when:
  - all the troops that can come to the board/ can be spawned are killed
  - all the buildings excluding walls are removed is termed as victory

## Assumptions
- Every time v is pressed speed, damage becomes twice
- Distance is calculated using the formula `|x2-x1| + |y2-y1|`.


## Troops

### King
```
    xpos = 0
    ypos = 0
    health = 4
    maxhealth = 4
    speed = 1
    damage = 1
```

### Queen
```
      xpos = 0
      ypos = 0
      health = 4
      maxhealth = 4
      speed = 1
      damage = 0.75
```

### Archer
```
      health = 0.5
      speed = 2
      damage = 0.125
```

### Balloon
```
      health = 1
      speed = 2
      damage = 0.5
```

## Buildings

### Walls
```
      health = 1
```

### Wizard Tower
```
      damage = 0.5
      health = 2
```

### Cannon
```
      damage = 0.5
      health = 2
```

### Townhall
```
      health = 10
```

### Huts
```
      health = 5
```

## Bonus
Implemented axe of king which has radius 3 units which isn't hardcode and can be easily modified
Implemented queen's special attack