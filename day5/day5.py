def openToArray(pFileName):
    content = []
    f = open(pFileName, 'r')
    for line in f:
        content.append(line.strip('\n'))
    return content

def searchHighestSeatID(pContent):
    highestID = 0
    for seat in pContent:
        row = searchSeat(seat[:7], 0, 127, 'F', 'B')
        col = searchSeat(seat[7:], 0, 7, 'L', 'R')
        seatID = (row*8)+col
        if seatID > highestID:
            highestID = seatID
    return highestID

def searchSeat(pSeatPos, pMin, pMax, pCMin, pCMax):
    sMin = pMin
    sMax = pMax
    for c in pSeatPos:
        if(c == pCMin):
            sMax = (sMax + sMin)//2
        elif(c == pCMax):
            sMin = ((sMax + sMin)//2)+1
    return sMin

def searchMissingSeat(pContent):
    seats = [True]*((127*8)+8)
    for y in range (11):
        for x in range(8):
            seats[((127-y)*8)+x]=False
            seats[(y*8)+x]=False
    for seat in pContent:
        row = searchSeat(seat[:7], 0, 127, 'F', 'B')
        if (row == 0 or row == 127):
            continue;
        col = searchSeat(seat[7:], 0, 7, 'L', 'R')
        seats[(row*8)+col]=False
    seatLeft = len([i for i,x in enumerate(seats) if x==True])
    row = 0
    while(seatLeft > 1):
        for x in range(8):
            if(seats[((127-y)*8)+8]):
                seats[((127-y)*8)+8]=False
                seatLeft -= 1
            if(seats[(y*8)+x]):
                seats[(y*8)+x]=False
                seatLeft -= 1
        y+=1
    return seats.index(True)

if __name__ == "__main__":
    content = openToArray('input.txt')
    print(searchHighestSeatID(content))
    print(searchMissingSeat(content))
