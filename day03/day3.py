import math

def readSlopeFile(pFileName):
    f = open(pFileName, 'r')
    content = []
    for line in f:
        content.append(list(line.strip('\n')))
    return content

def countTree(pContent, pR, pD):
    length = len(pContent[0])
    end = len(pContent)
    nbOfTree = 0
    xPos = 0
    yPos = 0
    while (yPos < end):
        xPos += pR
        yPos += pD
        if(yPos >= end):
            break;
        if(pContent[yPos][xPos % length] == '#'):
            nbOfTree += 1
    return nbOfTree


if __name__ == "__main__":
    content = readSlopeFile("input.txt")
    result1 = countTree(content, 3, 1)
    print(result1)
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    result2 = math.prod([countTree(content, r, d) for r, d in slopes])
    print(result2)
    

