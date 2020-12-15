def part1(pInput, pTurn):
    turn = 0
    numbers = dict()
    last = 0
    for v in pInput.split(","):
        numbers[int(v)] = [0,turn,None]
        last = int(v)
        turn+=1
    while turn < pTurn:
        s = numbers[last]
        if(s[0] == 0):
            last = 0
        else:
            last = s[1]-s[2]

        if last in numbers:
            new = numbers[last]
            numbers[last] = [new[0]+1,turn,new[1]]
        else:
            numbers[last] = [0, turn, None]
        turn+=1
    return last

if __name__ == "__main__":
    inp = "2,0,1,9,5,19"
    print(part1(inp, 2020))
    print(part1(inp,30000000))
