import sys

def readFile(pName):
    f = open(pName, "r")
    content = [int(line.strip('\n')) for line in f]
    return content

def getInputSum(pContent, pSum):
    k = 0
    for i in range(len(pContent)):
        inp1 = pContent[i]
        for j in range(k, len(pContent)):
            inp2 = pContent[j]
            if(inp1 + inp2 == pSum):
                print(inp1, inp2, inp1*inp2)
        k+=1

if __name__ == "__main__":
    if (len(sys.argv) == 2):
        listInput = readFile(sys.argv[1])
        getInputSum(listInput, 2020)
    else:
        print("Please give the name of the imput file")

