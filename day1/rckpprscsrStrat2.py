def winRPS():
    values = {'A': 1, 'B': 2, 'C': 3}
    total = 0
    with open('rps.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            elf = line[0]
            you = line[2]

            if you == 'X':
                if elf == 'A':
                    total += 3
                else:
                    total += values[elf] - 1
            elif you == 'Y':
                total += 3 + values[elf]
            else:
                total += 6
                if elf == 'C':
                    total += 1
                else:
                    total += values[elf] + 1

    return total

if __name__ == '__main__':
    total = winRPS()
    print(total)