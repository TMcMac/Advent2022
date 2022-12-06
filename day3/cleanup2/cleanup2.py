def cleanZones():
    inclusive = 0
    with open('zones.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            zones = line.split(',')
            zone1 = zones[0].split('-')
            zone2 = zones[1].split('-')
            range1 = range(int(zone1[0]), int(zone1[1]) + 1)
            range2 = range(int(zone2[0]), int(zone2[1]) + 1)
            x = set(range1)
            y = x.intersection(range2)

            if len(y) != 0:
                inclusive += 1
            else:
                continue
    return inclusive

if __name__ == '__main__':
    total = cleanZones()
    print(total)
        