
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

if __name__ == "__main__":
    content = readToMatrix("input")
    validPW = countValidPW(content)
    print(validPW)
