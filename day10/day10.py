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

def addValueToLists(pToAdd, pLists):
    concat = []
    for l in pLists:
        concat.append(pToAdd + l)
    print("concat", concat)
    return concat

def findCom(pContent, pI, pRating):
    count = 0
    if(pI == len(pContent)):
        return 1
    for i in range(pI, len(pContent)):
        diff = pContent[i] - pRating
        if diff >= 1 and diff <= 3:
            count += findCom(pContent, (i+1), pContent[i])
        else:
            break;
    return count
        
def findCom1(pContent, pSet):
    count = 0
    toMult = []
    currentV = 0
    i = -1
    currentCount = 0
    sub = 0
    depth = 0
    jump3 = False
    while(i<len(pContent)-1):
        mult = 0
        if(currentV+1 in pSet):
            mult += 1
        if(currentV+2 in pSet):
            mult += 1
        if(currentV+3 in pSet):
            mult += 1
            jump3 = True
        if(currentCount == 0 or mult == 3):
            currentCount += mult
        else:
            currentCount += max(mult-1,0)
        if mult == 1 and jump3:
            toMult.append(currentCount)
            jump3 = False
            currentCount = 0
            depth = 0
        else:
            depth += 1
        i+=1 
        if(i<len(pContent)-1):
            currentV = pContent[i]
    return math.prod(toMult)



def part2(pContent, pRating):
    setContent = set(pContent)
    return findCom1(pContent, setContent) 

if __name__ == "__main__":
    content = parser("input.txt")
    print(content)
    print(part1(content, 0))
    print(part2(content, 0))
