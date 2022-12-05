#!/usr/bin/python3
def findHigh():
    maxCal = 0
    curCalCnt = 0

    with open('elfcals.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.strip().isnumeric():
                curCalCnt += int(line)
            else:
                if maxCal <= curCalCnt:
                    maxCal = curCalCnt
                curCalCnt = 0
    return maxCal

if __name__ == '__main__':
    mostCals = findHigh()
    print(mostCals)