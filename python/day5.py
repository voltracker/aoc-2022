from utils import read_input

lists = [['F', 'G','V','R','J','L','D'],['S','J','H','V','B','M','P','T'],['C','P','G','D','F','M','H','V'],['Q','G','N','P','D','M'],['F','N','H','L','J'],['Z','T','G','D','Q','V','F','N'],['L','B','D','F'],['N','D','V','S','B','J','M'],['D','L','G']]

data = read_input("day5.txt").split('\n')

for move in data:
    l = move.split(' ')
    quantity, frm, to = int(l[1]), int(l[3]), int(l[5])
    for x in range(quantity):
        mv = lists[frm-1].pop(0)
        lists[to-1].insert(0,mv)
print([x[0] for x in lists])

lists = [['F', 'G','V','R','J','L','D'],['S','J','H','V','B','M','P','T'],['C','P','G','D','F','M','H','V'],['Q','G','N','P','D','M'],['F','N','H','L','J'],['Z','T','G','D','Q','V','F','N'],['L','B','D','F'],['N','D','V','S','B','J','M'],['D','L','G']]
for move in data:
    l = move.split(' ')
    quantity, frm, to = int(l[1]), int(l[3]), int(l[5])
    mv = lists[frm-1][:quantity]
    lists[frm-1] = lists[frm-1][quantity:]
    lists[to-1] = mv + lists[to-1]
print([x[0] for x in lists])
