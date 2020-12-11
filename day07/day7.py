import re
def parseInputColor(pFileName):
    content = dict()
    f = open(pFileName, 'r')
    splitColorBags = re.compile('([a-zA-Z]+ [a-zA-Z]+) bags contain (.*)')
    splitBags = re.compile('([0-9]+) ([a-zA-Z]+ [a-z A-Z]+) bags?')
    for line in f:
        color, bags = splitColorBags.match(line).groups()
        newColor = dict()
        for match in splitBags.finditer(bags):
            newColor[match.group(2)] = int(match.group(1))
        content[color] = newColor
    return content

def checkColor(pContent, pColor, pObjColor):
    return any(bag == pObjColor or checkColor(pContent, bag, pObjColor) for bag in pContent[pColor].keys())

def countContainBag(pContent, pColor):
    count = 0
    for k,v in pContent.items():
        if k == pColor:
            continue
        if(checkColor(pContent, k, pColor)):
            count +=1
    return count


def countC(pContent, pColor):
    count = 1
    for k, v in pContent[pColor].items():
        count += countC(pContent, k) * v
    return count

def countBags(pContent, pColor):
    return countC(pContent, pColor) - 1
    
if __name__ == "__main__":
    content = parseInputColor("input.txt")
    print(countContainBag(content, 'shiny gold'))
    print(countBags(content, 'shiny gold'))
