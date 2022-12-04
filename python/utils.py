def read_input(filename):
    with open(filename) as rf:
        return rf.read().rstrip('\n')
