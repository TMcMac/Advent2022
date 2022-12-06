def cleanZones():
    inclusive = 0
    with open('zones.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            zones = line.split(',')
            zone1 = zones[0].split('-')
            zone2 = zones[1].split('-')
            if int(zone1[0]) <= int(zone2[0]) and int(zone1[1]) >= int(zone2[1]):
                inclusive += 1
            elif int(zone2[0]) <= int(zone1[0]) and int(zone2[1]) >= int(zone1[1]):
                inclusive += 1
            else:
                continue
    return inclusive

if __name__ == '__main__':
    total = cleanZones()
    print(total)
        