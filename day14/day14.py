import re

def changeMask(pMask):
    for i, c in enumerate(pMask):
        if c != 'X':
            newMask = pMask[i:]
            break
    return newMask

def parser(pFileName):
    content = []
    f = open(pFileName, 'r')
    reg = re.compile('(mem)*(mask|\[[0-9]+\]) = ([0-9X]+)')
    line = f.readline()
    toAdd = (reg.match(line).groups()[2], [])
    for line in f:
        splited = reg.match(line).groups()
        if(splited[1] == 'mask'):
            content.append(toAdd)
            toAdd = (splited[2],[])
        else:
            toAdd[1].append((int(splited[1][1:-1]), int(splited[2])))
    content.append(toAdd)
    return content

def part1(pContent):
    addresses = dict()
    for mask, values in pContent:
        smallMask = changeMask(mask)
        maskOne = smallMask.replace('X', '1')
        maskZero = smallMask.replace('X', '0')
        for addr, v in values:
            addresses[addr] = (int(maskOne, 2) & v) | int(maskZero, 2)
    count = 0
    for v in addresses.values():
        count += v
    return count

def replaceBin(pMask):
    listX = []
    newBinary = ""
    for i, c in enumerate(pMask):
        if(c == 'X'):
            listX.append(i)
            newBinary += '0'
        else:
            newBinary += c
    return (newBinary, listX)

def completeAddr(pAddr, pIndex, pI):
    addresses = []
    if len(pIndex) > pI:
        xInd = pIndex[pI]
        for i in range(2):
            addresses += completeAddr(pAddr[:xInd] + str(i) + pAddr[xInd + 1:], pIndex, pI+1)
    else:
        return [int(pAddr,2)]
    return addresses



def part2(pContent):
    addresses = dict()
    for mask, values in pContent:
        newMask, xIndex = replaceBin(mask)
        addrTemp = []
        for addr, v in values:
            newAddr = addr | int(newMask, 2)
            addrTemp = completeAddr(str('{0:b}'.format(newAddr)).zfill(36), xIndex, 0)
            for a in addrTemp:
                addresses[a] = v
    count = 0
    for v in addresses.values():
        count += v
    return count
            
if __name__ == "__main__":
    content = parser("input.txt")
    print(part1(content))
    print(part2(content))
