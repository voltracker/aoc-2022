from utils import read_input

data = read_input("day4.txt").split('\n')
totalp1 = 0
totalp2 = 0
for pair in data:
    ranges = pair.split(',')
    set1 = list(map(int, ranges[0].split('-')))
    set2 = list(map(int, ranges[1].split('-')))
    set1 = set(range(set1[0], set1[1]+1))
    set2 = set(range(set2[0], set2[1]+1))
    if (len(set1.intersection(set2)) == len(set1)) or (len(set2.intersection(set1)) == len(set2)):
        totalp1 += 1
    if (len(set1.intersection(set2))) > 0:
        totalp2 += 1

print(totalp1)
print(totalp2)
