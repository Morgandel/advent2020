import re
import math

def parser(pFileName):
    content = dict()
    f = open(pFileName, 'r')
    spliter = re.compile('([a-zA-Z ]+): ([0-9\-]+) or ([0-9\-]+)')
    ticket = re.compile('([a-zA-Z ]+):\n(.+)')
    parts = f.read().split("\n\n")
    validV = set()
    category = dict()
    for line in parts[0].split("\n"):
        group = spliter.match(line).groups()
        newCategory = set()
        for r in group[1:]:
            first, secon = list(map(int, r.split('-')))
            for i in range(first, secon+1):
                validV.add(i)
                newCategory.add(i)
        category[group[0]] = newCategory
    content['category'] = category
    content['valid'] = validV
    content['ticket'] = list(map(int, ticket.match(parts[1]).groups()[1].split(',')))
    content['nearby'] = []
    for line in parts[2].split('\n')[1:-1]:
        content['nearby'].append(list(map(int, line.split(','))))
    return content

def part1(pContent):
    tickets = dict()
    for t in pContent['nearby']:
        for v in t:
            toAdd = int(v)
            if toAdd in tickets:
                tickets[toAdd] += 1
            else:
                tickets[toAdd] = 1
    invalid = set(tickets.keys()).difference(pContent['valid'])
    count = 0
    return sum([v*tickets[v] for v in invalid])

def part2(pContent):
    #Removing invalid tickets
    validTickets = []
    for t in pContent['nearby']:
        valid = True
        for v in t:
            if(v not in content['valid']):
                valid = False
                break
        if valid:
            validTickets.append(t)

    positions = dict()
    for i in range(len(pContent['ticket'])):
        positions[i] = list(pContent['category'].keys())
    for t in validTickets:
        for i, v in enumerate(t):
            for pos in positions[i]:
                if v not in pContent['category'][pos]:
                    positions[i].remove(pos)
    
    results = dict()
    nb = 0
    while(len(results) < len(pContent['ticket'])):
        nb+=1
        for k, cat in positions.items():
            if len(cat) == 1:
                results[k] = cat.pop(0)
                for l in positions.values():
                    if(results[k] in l):
                        l.remove(results[k])
    return results

def prodDeparture(pContent, pPositions):
    result = 1
    for k,v in pPositions.items():
        if v.find('departure') != -1:
            result *= pContent['ticket'][k]
    return result

if __name__ == "__main__":
    content = parser('input.txt')
    print(part1(content))
    print(prodDeparture(content, part2(content)))
