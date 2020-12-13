def parser(pFileName):
    f = open(pFileName)
    minTime = int(f.readline())
    buses = f.readline().split(',')
    return (minTime, buses)

def part1(pContent):
    start = pContent[0]
    waitB = []
    for bus in pContent[1]:
        modu = start%bus
        waitB.append((bus, bus-modu))
    minWait = waitB[0]
    for bus in waitB[1:]:
        if(bus[1] < minWait[1]):
            minWait = bus
    return minWait[0] * minWait[1]

def part2(pContent):
    timestamp = 0
    buses = [(int(bus), time) for time, bus in enumerate(pContent) if bus !='x']
    jump = 1
    for bus, time in buses:
        notFound = True
        while notFound:
            if(time + timestamp)% bus == 0:
                notFound = False
            else:
                timestamp += jump
        jump *= bus
    return timestamp

if __name__ == "__main__":
    content = parser('input.txt')
    noX = (content[0], list(map(int, filter(('x').__ne__, content[1]))))
    print(part1(noX))
    test1 = parser('test1.txt')
    test2 = parser('test2.txt')
    test3 = parser('test3.txt')
    test4 = parser('test4.txt')
    test5 = parser('test5.txt')
    test6 = parser('test6.txt')
    print(part2(test1[1]))
    print(part2(test2[1]))
    print(part2(test3[1]))
    print(part2(test4[1]))
    print(part2(test5[1]))
    print(part2(test6[1]))
    print(part2(content[1]))

