import math
def parser(pFileName):
    content = []
    f = open(pFileName, 'r')
    for line in f:
        content.append(int(line))
    content.sort()
    return content

def part1(pContent, pRating):
    count1 = 0
    count3 = 1
    for jolt in pContent:
        diff = jolt - pRating
        if diff == 1:
            count1 += 1
            pRating = jolt
        elif diff == 2:
            pRating = jolt
        elif diff == 3:
            count3 += 1
            pRating = jolt
        else:
            break
    print(count1, count3)
    return count1 * count3

def findCom(pContent, pSet):
    toMult = []
    currentCount = 0
    content = [0]+pContent
    for v in content:
        mult = 0
        if(v+1 in pSet):
            mult += 1
        if(v+2 in pSet):
            mult += 1
        if(v+3 in pSet):
            mult += 1
        if(currentCount == 0 or mult == 3):
            currentCount += mult
        else:
            currentCount += max(mult-1,0)
        if mult == 1:
            toMult.append(currentCount)
            currentCount = 0
    return math.prod(toMult)

def part2(pContent, pRating):
    setContent = set(pContent)
    return findCom(pContent, setContent) 

if __name__ == "__main__":
    content = parser("input.txt")
    print(part1(content, 0))
    print(part2(content, 0))
