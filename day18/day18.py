from operator import mul, add

def getExpression(pLine):
    line = pLine.replace(" ", "").strip("\n")
    finalExp = []
    queue = []
    currentExp = finalExp
    for c in line:
        if c == '(':
            queue.append(currentExp)
            currentExp = []
        elif c == ')':
            nextExp = queue.pop()
            nextExp.append(currentExp)
            currentExp = nextExp
        elif(c.isnumeric()):
            currentExp.append(int(c))
        else:
            currentExp.append(c)
    return finalExp

def parser(pFileName):
    content = []
    f = open(pFileName,'r')
    for line in f:
        content.append(getExpression(line))
    return content

def evaluate(pExp):
    total = 0
    nextOpe = add
    for c in pExp:
        if c == '*':
            nextOpe = mul
        elif c == '+':
            nextOpe = add
        else:
            if(isinstance(c, int)):
                total = nextOpe(total,c)
            else:
                total = nextOpe(total,evaluate(c))
    return total

def advEvaluate(pExp):
    nextExp = []
    currentV = 0
    nextOpe = None
    for c in pExp:
        if c == '*':
            nextExp.append(currentV)
            nextExp.append('*')
            currentV = 0
        elif c == '+':
            nextOpe = add
        else:
            if(nextOpe):
                if(isinstance(c, int)):
                    currentV = add(currentV, c)
                else:
                    currentV = add(currentV, advEvaluate(c))
                nextOpe = None
            else:
                if(isinstance(c, int)):
                    currentV = c
                else:
                    currentV = advEvaluate(c)
    nextExp.append(currentV)
    return evaluate(nextExp)

def part1(pContent):
    total = 0
    for exp in pContent:
        total += evaluate(exp)
    return total

def part2(pContent):
    total = 0
    for exp in pContent:
        total += advEvaluate(exp)
    return total

if __name__ == "__main__":
    content = parser('input.txt')
    print(part1(content))
    print(part2(content))
