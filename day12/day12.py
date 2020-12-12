import re

def parser(pFileName):
    content = []
    spliter = re.compile("([A-Z])([0-9]+)")
    f = open(pFileName, "r")
    for line in f:
        inst, value = spliter.match(line).groups()
        content.append((inst, int(value)))
    return content

def getDirection(pDegrees):
    if(pDegrees == 0):
        return 'W'
    if(pDegrees == 90):
        return 'N'
    if(pDegrees == 180):
        return 'E'
    if(pDegrees == 270):
        return 'S'
    print("erreur degrée", pDegrees)
    exit()
    return "erreur"

def move(pDir, pV, pX, pY):
    if(pDir == 'N'):
        return (pX, pY+pV)
    if(pDir == 'S'):
        return (pX, pY-pV)
    if(pDir == 'E'):
        return (pX+pV, pY)
    if(pDir == 'W'):
        return (pX-pV, pY)
    print("erreur direction", pDir)
    exit()

def part1(pContent):
    d = 180
    direction = "E"
    x = 0
    y = 0
    changed = False
    for inst, v in pContent:
        if(inst == 'L' or inst == 'R'):
            d = getDegree(inst, v, d)
            direction = getDirection(d)
        elif(inst == 'F'):
            x, y = move(direction, v, x, y)
        else:
            x, y = move(inst, v, x, y) 
    return abs(x)+abs(y)

def getDegree(pDir, pV, pD):
    if(pDir == 'L'):
        nextD = pD - pV
        if nextD < 0:
            return 360 + nextD
        else:
            return nextD
    elif(pDir == 'R'):
        return (pD+pV)%360

def changeWaypoint(pV, pX, pY, pInst):
    if pV == 180:
        return (-pX, -pY)
    if pV == 360 or pV == 0:
        return (pX, pY)
    if pV == 90:
        if pInst == 'R':
            return (pY, -pX)
        else:
            return (-pY, pX)
    if pV == 270:
        if pInst == 'R':
            return (-pY, pX)
        else:
            return (pY, -pX)

def part2(pContent):
    deg1 = 180
    deg2 = 90
    wpX = 10
    wpY = 1
    x = 0
    y = 0
    for inst, v in pContent:
        if(inst == 'L' or inst == 'R'):
            deg1 = getDegree(inst, v, deg1)
            deg2 = getDegree(inst, v, deg2)
            wpX, wpY = changeWaypoint(v, wpX, wpY, inst)
        elif(inst == 'F'):
            x += wpX*v
            y += wpY*v
        else:
            wpX, wpY = move(inst, v, wpX, wpY)
    return abs(x) + abs(y)

if __name__ == "__main__":
    content = parser("input.txt")
    print(part1(content))
    print(part2(content))

