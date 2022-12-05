def winRPS():
    values = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    total = 0
    with open('rps.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            elf = line[0]
            you = line[2]

            total += values[you]

            if values[elf] + 1 == values[you] or values[you] + 2 == values[elf]:
                total += 6
            elif values[elf] == values[you]:
                total += 3
            else:
                continue

    return total

if __name__ == '__main__':
    total = winRPS()
    print(total)