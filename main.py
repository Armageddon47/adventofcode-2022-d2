import numpy as np

sums = []
points = 0
# read the input file and split the arrays
with open('input.txt') as f:
    values = []
    for line in f:
        if line[0] == 'A':
            if line[2] == 'X':
                points += 3
                points += 1
            elif line[2] == 'Y':
                points += 6
                points += 2
            elif line[2] == 'Z':
                points += 0
                points += 3
        elif line[0] == 'B':
            if line[2] == 'X':
                points += 0
                points += 1
            if line[2] == 'Y':
                points += 3
                points += 2
            if line[2] == 'Z':
                points += 6
                points += 3
                
        elif line[0] == 'C':
            if line[2] == 'X':
                points += 6
                points += 1
            if line[2] == 'Y':
                points += 0
                points += 2
            if line[2] == 'Z':
                points += 3
                points += 3
            
        # check if the line is empty        
        
print(points)
##### End of part one
secondpoints = 0
rock = 1
paper = 2
sc = 3

def Win(line):
    global secondpoints
    if line[0] == 'A':
         secondpoints += paper
    elif line[0] == 'B':
        secondpoints+= sc
    elif line[0] == 'C':
        secondpoints += rock
    secondpoints += 6
def Lose(line):
    global secondpoints
    if line[0] == 'A':
         secondpoints += sc
    elif line[0] == 'B':
        secondpoints+= rock
    elif line[0] == 'C':
        secondpoints += paper
def Draw(line):
    global secondpoints

    if line[0] == 'A':
         secondpoints += rock
    elif line[0] == 'B':
        secondpoints+= paper
    elif line[0] == 'C':
        secondpoints += sc
    secondpoints += 3
with open('input.txt') as f:
    values = []
    for line in f:
        if line[2] == 'Z':
            Win(line)
        elif line[2] == 'Y':
            Draw(line)
        elif line[2] == 'X':
            Lose(line)
            
print(secondpoints)