def getWin(opp):
    if opp == 'C':
        return 'X'
    elif opp == 'A':
        return 'Y'
    elif opp == 'B':
        return 'Z'

def getDraw(opp):
    return chr(ord(opp)+23)

def getLoss(opp):
    if opp == 'C':
        return 'Y'
    elif opp == 'A':
        return 'Z'
    elif opp == 'B':
        return 'X'

def getScore(you):
    return ord(you)-87

def playValue(opp, you):
    if you == 'X':
        return getScore(getLoss(opp)) + 0
    elif you == 'Y':
        return getScore(getDraw(opp)) + 3
    elif you == 'Z':
        return getScore(getWin(opp)) + 6

with open("day2input.txt") as rf:
    plays = rf.read().rstrip("\n").split("\n")
    total = 0
    for play in plays:
        move = play.split(" ")
        total += playValue(move[0], move[1])
    print(total)
