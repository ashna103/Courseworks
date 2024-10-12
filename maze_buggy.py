#!/usr/bin/env python
# coding: utf-8

# In[1]:


maze= [
    "XXXXXXXXXXXX",
    "s          X",
    "XXXXXXXX XXX",
    "X     XX XXX",
    "X XXXXXX   X",
    "X XXXe XXX X",
    "X      X   X",
    "X XXXXXX X X",
    "X X    XXX X",
    "X XXXX XXX X",
    "X          X",
    "XXXXXXXXXXXX"]


#The algorithm is the "left hand rule". 
#Keep walking with your left hand touching a wall
#If you meet an obstruction, turn to the right.

#Forward directions, row then column
#the directions are in order, so if you 
#turn right, you move to the next one
forward = [
    (0, 1),  # east Keep row same, increase column by 1
    (1, 0),  # South
    (0, -1), # west
    (-1, 0), # north
]

forward_symbol = "→↓←↑"


left_hand = [
    (-1,0),   #Facing east, left hand is north
    (0, 1),   #Facing south left hand is east
    (1, 0),   #Facing west left hand is south
    (0, -1),  #Facing north, left hand is west
]

print(maze,forward, left_hand)


# In[2]:


# Find start position
for r in range(len(maze)):
    if "s" in maze[r]:
        for c in range(len(maze[r])):
            if maze[r][c] == "s":
                row = r
                col = c


print("Start: row ", row, " column ", col)
#Start facing east
direction = 0


# In[3]:


#Keep going until we reach the end
while maze[row][col] != "e":

    #Print out the maze and the direction of travel
    maze_text=[]
    for r in maze:
        maze_text.append(list(r))
    maze_text[row][col] = forward_symbol[direction]
    

    for r in maze_text:
        print("".join(r))

    input()
    
    #Try and take a step forwards
    forward_row = row + forward[direction][0]
    forward_column = col + forward[direction][1]

    if maze[forward_row][forward_column] == "X":
        #If the path is blocked, turn left
        direction += 1
        if direction==4:
            direction=direction-4

    else:
        #Take a step forward
        row = forward_row
        col = forward_column

        #Now check to see if our left hand is still on the wall
        left_hand_row = row + left_hand[direction][0]
        left_hand_column = col + left_hand[direction][1]

        #If our left hand isn't on the wall, turn to the left
        if maze[left_hand_row][left_hand_column] != "X":
            direction -=1
            if direction == -1:
                direction = 3
        
    

print("End position", row, col)


# In[ ]:




