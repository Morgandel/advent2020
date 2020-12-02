
def readToMatrix(pFileName):
    content = []
    f = open(pFileName, 'r')
    for line in f:
        splited = line.split(' ')
        minValue, maxValue = splited[0].split('-')
        content.append([int(minValue), int(maxValue), splited[1].strip(':'), splited[2].strip('\n')])
    return content

def countValidPW(pContent):
    validCount = 0
    for pw in pContent:
        counted = 0
        valid=True
        for c in pw[3]:
            if c == pw[2]:
                counted += 1
                if counted > pw[1]:
                    break;
        if(counted >= pw[0] and counted <= pw[1]):
            validCount += 1
    return validCount

def validCharPosition(pContent):
    validCount = 0
    for pw in pContent:
        pos1 = pw[3][pw[0]-1] == pw[2]
        pos2 = pw[3][pw[1]-1] == pw[2]
        if ((not pos1 and pos2) or (pos1 and not pos2)):
            validCount += 1
    return validCount

if __name__ == "__main__":
    content = readToMatrix("input.txt")
    #validPW = countValidPW(content)
    validPW = validCharPosition(content)    
    print(validPW)
