with open('input.txt', 'r') as f:
    lines = f.readlines()

elvesWithMostCalories = [-100, -100, -100]
currentElfCalorieCount = 0
for line in lines:
    if(line == '\n'):
        if currentElfCalorieCount > elvesWithMostCalories[-1]:
            elvesWithMostCalories[-1] = currentElfCalorieCount
            for elves in range(len(elvesWithMostCalories)-1, 0, -1):
                right = elvesWithMostCalories[elves]
                left = elvesWithMostCalories[elves-1]
                if right > left:
                    elvesWithMostCalories[elves-1] = right
                    elvesWithMostCalories[elves] = left
                else:
                    break
        currentElfCalorieCount = 0
    else:
        currentElfCalorieCount += int(line)

print(elvesWithMostCalories)
sumOfElvesWithMostCalories = 0
for elf in elvesWithMostCalories:
    sumOfElvesWithMostCalories += elf
print(sumOfElvesWithMostCalories)