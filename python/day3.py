def pt1(data):
    total = 0
    for backpack in data.split('\n'):
        compart1 = backpack[:len(backpack)//2]
        compart2 = backpack[len(backpack)//2:]
        for char in compart1:
            if char in compart2:
                if char.isupper():
                    total += ord(char) - 38
                else:
                    total += ord(char) - 96
                break
    print(total)

def pt2(data):
    allbackpacks = data.rstrip('\n').split('\n')
    div = []
    total = 0
    for x in range(0, len(allbackpacks), 3):
        div.append(allbackpacks[x:x+3])
    for grp in div:
        for char in grp[0]:
            if char in grp[1] and char in grp[2]:
                if char.isupper():
                    total += ord(char) - 38
                else:
                    total += ord(char) - 96
                break
    print(total)

with open("day3.txt") as rf:
    data = rf.read()
    pt1(data)
    pt2(data)
