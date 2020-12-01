import sys

def readFile(pName):
    f = open(pName, "r")
    content = [int(line.strip('\n')) for line in f]
    return content

def getInputSumOfTwo(pContent, pSum):
    m = 1
    found = False
    for i in range(len(pContent)-1):
        inp1 = pContent[i]
        for j in range(m, len(pContent)):
            inp2 = pContent[j]
            if(inp1 + inp2 == pSum):
                print(inp1, inp2, inp1*inp2)
                found = True
                break;
        if found:
            break;
        m+=1

def getInputSumOfThree(pContent, pSum):
    m=0
    n=1
    found = False
    for i in range(len(pContent)-2):
        m+=1
        n+=1
        o=m
        p=n
        inp1 = pContent[i]
        for j in range(o, len(pContent)):
            inp2 = pContent[j]
            for k in range(p, len(pContent)):
                inp3 = pContent[k]
                if(inp1 + inp2 + inp3 == pSum):
                    print(inp1, inp2, inp3, inp1*inp2*inp3)
                    found = True
                    break;
            if found:
                break;
        if found:
            break;

if __name__ == "__main__":
    if (len(sys.argv) == 3):
        listInput = readFile(sys.argv[2])
        if(sys.argv[1] == "-tw"):
            getInputSumOfTwo(listInput, 2020)
        elif(sys.argv[1] == "-th"):
            getInputSumOfThree(listInput, 2020)

    else:
        print("Please give the name of the imput file")

