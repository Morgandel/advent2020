def parser(pFileName):
    content = []
    f = open(pFileName, 'r')
    for line in f:
        content.append(int(line))
    return content

def checkValue(pPreAmb, pVal):
    for i, x in enumerate(pPreAmb):
        for y in pPreAmb[i+1:]:
            if(x+y == pVal):
                return True
    return False
def part1(pContent, pPreAmbSize):
    preAmb = pContent[:pPreAmbSize]
    for i, v in enumerate(pContent[pPreAmbSize:]):
        if not checkValue(preAmb, v):
            return (v, i)
        preAmb.pop(0)
        preAmb.append(v)
    return "Not Found"

def part2(pContent, pValue):
    listVal = []
    minI = 0
    sumValue = 0
    for i, v in enumerate(pContent):
        sumValue += v
        listVal.append(v)
        while sumValue > pValue:
            listVal.pop(0)
            sumValue -= pContent[minI]
            minI+=1
        if(sumValue == pValue):
            return max(listVal) + min(listVal)


if __name__ == "__main__":
    content = parser('input.txt')
    v, i = part1(content, 25)
    print(part2(content[:i], v))


