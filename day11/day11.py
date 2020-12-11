import numpy as np

def parser(pFileName):
    content = []
    f = open(pFileName, 'r')
    for line in f:
        content.append([c for c in line.strip('\n')])
    return np.array(content)

def part1(pContent, pX, pY):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            v = pContent[pY+i][pX+j]
            if(i == 0 and j == 0):
                continue
            elif(v == '#'):
                count+=1
    return count

def part2(pContent, pX, pY):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if(i == 0 and j == 0):
                continue
            v = search(pContent, pX+j, pY+i, j, i)
            if(v == '#'):
                count+=1
    return count

def search(pContent, pX, pY, pXStep, pYStep):
    while True:
        v = pContent[pY][pX]
        if(v != '.'):
            return v
        pX = pX + pXStep
        pY = pY + pYStep

def changeSeats(pContent, countAdjacent, pNbOccu):
    content = np.where(pContent=='L', '#', pContent)
    nextCon = np.copy(content)
    maxY, maxX = content.shape
    change = True
    while change:
        change = False
        for y in range(1, maxY-1):
            for x in range(1, maxX-1):
                ocp = countAdjacent(content, x, y)
                if content[y][x] == 'L':
                    if ocp == 0:
                        nextCon[y][x] = '#'
                        change = True
                elif content[y][x] == '#':
                    if ocp >= pNbOccu:
                        nextCon[y][x] = 'L'
                        change = True
        content = np.copy(nextCon)
    return np.count_nonzero(content == '#')


def addFloor(pContent):
    nbY, nbX = content.shape
    toAddX = np.full((nbY+2, nbX+2), '+')
    toAddX[1:-1,1:-1] = content
    return toAddX

if __name__ == "__main__":
    content = parser("input.txt")
    contentWithFloor = addFloor(content)
    print(changeSeats(contentWithFloor, part1, 4))
    print(changeSeats(contentWithFloor, part2, 5))
