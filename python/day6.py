from utils import read_input

string = read_input("day6.txt")

def pt1(string):
    for x in range(len(string)-4):
        if len(set(string[x:x+4])) == 4:
            print(x+4)
            break

def pt2(string):
    for x in range(len(string)-14):
        if len(set(string[x:x+14])) == 14:
            print(x+14)
            break


pt1(string)
pt2(string)
