import re

def parser(pFileName):
    content = []
    f = open(pFileName, 'r')
    for line in re.findall(r'(.*) \(contains (.*)\)',f.read()):
        content.append([set(line[0].split(' ')), set(line[1].split(', '))])
    return content

def part1(pContent):
    toRemove = dict()
    for ingre, aller in pContent:
        for l in aller:
            if l in toRemove:
                toRemove[l] &= ingre
            else:
                toRemove[l] = ingre.copy()
    alrgs = set()
    for al in toRemove.values():
        for a in al:
            alrgs.add(a)
    count = 0
    for ingr, _ in pContent:
        for ing in ingr:
            if ing not in alrgs:
                count += 1
    return (count, toRemove)

def part2(pContent, pAlrgs):
    for lis in pAlrgs.values():
        if(len(lis) == 1):
            break
    lis = list(lis)
    while len(lis) > 0:
        l = set()
        toRemove = lis.pop()
        for a in pAlrgs:
            if(len(pAlrgs[a]) > 1 and toRemove in pAlrgs[a]):
                pAlrgs[a].remove(toRemove)
                if len(pAlrgs[a]) == 1:
                    l |= alrgs[a]
        lis += list(l)
    toSort = [(k, v) for k, v in pAlrgs.items()]
    toSort.sort(key=lambda x: x[0])
    result = ''
    for allergens, ingredients in toSort:
        result += ingredients.pop()+','
    return result[:-1]
    
if __name__ == "__main__":
    content = parser('input.txt')
    p1, alrgs = part1(content)
    print(p1)
    print(part2(content, alrgs))