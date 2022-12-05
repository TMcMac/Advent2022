def ruck():
    total = 0
    count = 0
    with open('ruck1.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if count == 0:
                line1 = line
            elif count == 1:
                line2 = line
            elif count == 2:
                line3 = line
                for item in line1:
                    if item in line2 and item in line3:
                        if item.isupper():
                            total += ord(item) - 38
                        else:
                            total += ord(item) - 96
                        break
                count = -1
                line1 = line2 = line3 = ''
            count += 1
    return total

if __name__ == '__main__':
    total = ruck()
    print(total)