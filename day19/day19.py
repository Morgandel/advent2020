import re

def parser(pFileName):
    content = dict()
    f = open(pFileName, 'r')
    text = f.read().split("\n\n")
    rules = dict()
    for r in re.findall('([0-9]+): (.+)', text[0]):
        rules[r[0]] = r[1].split(" ")
    content['rules'] = rules
    content['messages'] = text[1].split("\n")[:-1]
    return content

def buildRules(pContent, pRule, pLast, pD):
    reg = ""
    for r in pRule:
        if r.isdigit():
            if r == pLast:
                pD += 1
            if pD < 10:
                toAdd = buildRules(pContent, pContent[r], r, pD)
                if toAdd == '"a"' or toAdd == '"b"':
                    reg += toAdd[1]
                else:
                    reg += "("+toAdd+")"
        else:
            reg += r
            
    return reg

def matchRule(pContent, pReg):
    count = 0
    for mess in pContent:
        if pReg.match(mess):
            count += 1
    return count

def part1(pContent, start='0'):
    reg = re.compile("^"+buildRules(pContent['rules'], pContent['rules'][start], None, 0)+"$")
    return matchRule(pContent["messages"], reg)

def part2(pContent, start='0'):
    pContent['rules']['8'] = ['42', '|', '42', '8']
    pContent['rules']['11'] = ['42', '31', '|', '42', '11', '31']
    reg = re.compile("^"+buildRules(pContent['rules'], pContent['rules'][start], None, 0)+"$")
    return matchRule(pContent["messages"], reg)

if __name__ == "__main__":
    content = parser('input.txt')
    print(part1(content))
    print(part2(content))
