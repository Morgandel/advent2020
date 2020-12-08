def parser(pFileName):
    content = []
    f = open(pFileName, 'r')
    for line in f:
        instruction, value = line.split(" ")
        content.append((instruction, int(value)))
    return content

def checkInst(pInst, pAccu, pI, pVisited):
    if pI in pVisited:
        return (pAccu, pI, pVisited, False)
    pVisited[pI] = True
    if(pInst[0] == "acc"):
        pAccu += pInst[1]
        pI += 1
    elif(pInst[0] == "jmp"):
        pI += pInst[1]
    elif(pInst[0] == "nop"):
        pI += 1
    return (pAccu, pI, pVisited, True)


def part1(pContent):
    visited = dict()
    accu = 0
    i = 0
    loop = True
    while loop:
        accu, i, visited, loop = checkInst(pContent[i], accu, i, visited)
    return accu

def invertInst(pContent, pNewInst, pIndex):
    for j in pIndex:
        visited = dict()
        accu = 0
        i = 0
        loop = True
        while loop and i < len(pContent):
            inst, value = pContent[i]
            if(i == j):
                inst = pNewInst
            accu, i, visited, loop = checkInst((inst, value), accu, i, visited)
        if(i >= len(pContent)):
            return (accu, True)
    return (0, False)

def part2(pContent):
    indexJmp = []
    indexNop = []
    for i, v in enumerate(pContent):
        if v[0] == "jmp":
            indexJmp.append(i)
        elif v[0] == "nop" and v[1] != 0:
            indexNop.append(i)
    value = invertInst(pContent, "nop", indexJmp)
    if(value[1]):
        return value[0]
    value = invertInst(pContent, "jmp", indexNop)
    if(value[1]):
        return value[0]
    return "Not found"


if __name__ == "__main__":
    content = parser("input.txt")
    print(part1(content))
    print(part2(content))
