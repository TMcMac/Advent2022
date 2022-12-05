#!/usr/bin/python3
def findHigh():
    maxCal1 = 0
    maxCal2 = 0
    maxCal3 = 0
    curCalCnt = 0

    with open('elfcals.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.strip().isnumeric():
                curCalCnt += int(line)
            else:
                if maxCal1 <= curCalCnt:
                    maxCal3 = maxCal2
                    maxCal2 = maxCal1
                    maxCal1 = curCalCnt
                elif curCalCnt >= maxCal2 and curCalCnt < maxCal1:
                    maxCal3 = maxCal2
                    maxCal2 = curCalCnt
                elif curCalCnt >= maxCal3 and curCalCnt < maxCal2:
                    maxCal3 = curCalCnt
                curCalCnt = 0
    return maxCal1 + maxCal2 + maxCal3

if __name__ == '__main__':
    mostCals = findHigh()
    print(mostCals)