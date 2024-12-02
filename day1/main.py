
file = open("input.txt", "r")

tot = 0
first = []
second = []

for x in file.readlines():
    line = x.strip().split()
    first.append(line[0])
    second.append(line[1])

first.sort()
second.sort()

#First Problem
summed = 0
for x in range(len(first)):
    summed += abs(int(first[x])-int(second[x]))

print(summed)


#Second problem
from collections import Counter
counted = Counter(second)

secSum = 0
for x in first:
    if x in counted:
        secSum += int(x)*counted[x]
print(secSum)