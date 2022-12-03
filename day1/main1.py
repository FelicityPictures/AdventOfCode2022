with open('input.txt', 'r') as f:
    lines = f.readlines()

elvesWithMostCalories = [-100, -100, -100]
currentElfCalorieCount = 0
for line in lines:
    if(line == '\n'):
        if currentElfCalorieCount > elvesWithMostCalories[2]:
            elfWithMostCalories = currentElfCalorieCount
        currentElfCalorieCount = 0
    else:
        currentElfCalorieCount += int(line)

print(elvesWithMostCalories)
