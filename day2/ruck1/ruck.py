def ruck():
    total = 0
    with open('ruck1.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            linleng = len(line)
            pouch1 = line[:linleng//2]
            pouch2 = line[linleng//2:]

            for item in pouch1:
                if item in pouch2:
                    if item.isupper():
                        total += ord(item) - 38
                    else:
                        total += ord(item) - 96
                    break
    return total

if __name__ == '__main__':
    total = ruck()
    print(total)