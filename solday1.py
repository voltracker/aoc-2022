final = []
with open("day1p1.txt") as rf:
    out = rf.read()
    elves = out.split('\n\n')
    for elf in elves:
        final.append(sum([int(x) for x in elf.split('\n') if x != '']))

    final.sort(reverse=True)
    print(final[0])
    print(sum([final[0], final[1], final[2]]))

