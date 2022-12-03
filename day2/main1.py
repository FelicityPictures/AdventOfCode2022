file = open('input.txt', 'r')
 
myScore = 0
while 1:
    # read by character
    opponent = file.read(1)
    file.read(1)
    self = file.read(1)
    file.read(1) 
    if not opponent or not self:
        break
    print("Opponent:" + opponent)
    print("Self:" + self)
    # you are rock
    if self == 'X':
        myScore += 1
        # they are rock
        if opponent == 'A':
            myScore += 3
        # they are paper
        elif opponent == 'B':
            myScore += 0
        # they are scissors
        elif opponent == 'C':
            myScore += 6

    # you are paper
    elif self == 'Y':
        myScore += 2
        # they are rock
        if opponent == 'A':
            myScore += 6
        # they are paper
        elif opponent == 'B':
            myScore += 3
        # they are scissors
        elif opponent == 'C':
            myScore += 0

    # you are scissors
    elif self == 'Z':
        myScore += 3
        # they are rock
        if opponent == 'A':
            myScore += 0
        # they are paper
        elif opponent == 'B':
            myScore += 6
        # they are scissors
        elif opponent == 'C':
            myScore += 3

 
file.close()

print(myScore)