def parser(pFileName):
    content = []
    f = open(pFileName, 'r')
    text = f.read().split('\n\n')
    content.append(list(map(int, text[0].split(':\n')[1].split('\n'))))
    content.append(list(map(int, text[1].split(':\n')[1].split('\n')[:-1])))
    return content

def part1(pP1, pP2):
    while len(pP1) > 0 and len(pP2) > 0:
        p1 = pP1.pop(0)
        p2 = pP2.pop(0)
        if(p1 > p2):
            pP1.append(p1)
            pP1.append(p2)
        else:
            pP2.append(p2)
            pP2.append(p1)
    win = pP1 if len(pP1) > 0 else pP2
    result = 0
    for i, v in enumerate(win):
        result += v * (len(win) - i)
    return result

def part2(pP1, pP2, pSub, pSeen, pGame=1):
    pSeen = []
    i = 1
    while len(pP1) > 0 and len(pP2) > 0:

        if(pP1 in pSeen and pP2 in pSeen):
            return 0
        if(pP1 not in pSeen):
            pSeen.append(pP1.copy())
        if(pP2 not in pSeen):
            pSeen.append(pP2.copy())
        p1 = pP1.pop(0)
        p2 = pP2.pop(0)
        if p1 <= len(pP1) and p2 <= len(pP2):
            subGame = part2(pP1[:p1], pP2[:p2], True, pSeen, pGame+1)
            if(subGame == 0):
                pP1.append(p1)
                pP1.append(p2)
            else:
                pP2.append(p2)
                pP2.append(p1)
        elif(p1 > p2):
            pP1.append(p1)
            pP1.append(p2)
        elif(p2 > p1):
            pP2.append(p2)
            pP2.append(p1)
    if pSub:
        if len(pP1) > 0:
            return 0 
        else:
            return 1
    win = pP1 if len(pP1) > 0 else pP2
    result = 0
    for i, v in enumerate(win):
        result += v * (len(win) - i)
    return result


if __name__ == "__main__":
    content = parser('input.txt')
    print(part1(content[0].copy(), content[1].copy()))
    print(part2(content[0].copy(), content[1].copy(), False, []))
