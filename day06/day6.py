def splitArray(pInput):
    return pInput.split('\n')

def openFileToArray(pFileName):
    f = open(pFileName,'r')
    content = list(map(splitArray, f.read().split("\n\n")))
    return content

def countUniqueList(pContent):
    sumAnswer = 0
    for group in pContent:
        answer = dict()
        for person in group:
            for c in person:
                answer[c]=True
        sumAnswer += len(answer.keys())
    return sumAnswer

def countSameAnswer(pContent):
    sumAnswer = 0
    for group in pContent:
        answer = dict()
        for person in group:
            for c in person:
                if c not in answer:
                    answer[c] = 1
                else:
                    answer[c] += 1
        for v in answer.values():
            if v == len(group):
                sumAnswer += 1

    return sumAnswer


if __name__ == "__main__":
    content = openFileToArray("input.txt")
    print(countUniqueList(content))
    print(countSameAnswer(content))
