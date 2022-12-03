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
    # you need to lose
    if self == 'X':
        myScore += 0
        # they are rock, I am scissor
        if opponent == 'A':
            myScore += 3
        # they are paper, I am rock
        elif opponent == 'B':
            myScore += 1
        # they are scissors, I am paper
        elif opponent == 'C':
            myScore += 2

    # you need to draw
    elif self == 'Y':
        myScore += 3
        # they are rock, I am rock
        if opponent == 'A':
            myScore += 1
        # they are paper, I am paper
        elif opponent == 'B':
            myScore += 2
        # they are scissors, I am scissor
        elif opponent == 'C':
            myScore += 3

    # you need to win
    elif self == 'Z':
        myScore += 6
        # they are rock, I am paper
        if opponent == 'A':
            myScore += 2
        # they are paper, I am scissor
        elif opponent == 'B':
            myScore += 3
        # they are scissors, I am rock
        elif opponent == 'C':
            myScore += 1

 
file.close()

print(myScore)