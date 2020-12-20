import numpy as np
import re
from collections import Counter

def parser(pFileName):
    content = dict()
    f = open(pFileName, 'r')
    reg = re.compile("Tile ([0-9]+):\n([\n\.#]*)")
    for t in f.read().split("\n\n"):
        splited = reg.match(t).groups()
        content[int(splited[0])] = np.array(list(map(list,splited[1].split('\n'))))
    return content

def getAllPossibilities(pTile):
    posblt = []
    for rotation in range(4):
        newArray = np.rot90(pTile, k=rotation)
        posblt.append(newArray)
        posblt.append(np.flip(newArray))
        posblt.append(np.flip(newArray, 0))
        posblt.append(np.flip(newArray, 1))
    return posblt




def part1(pTiles):
    size = int(np.sqrt(len(tiles)))
    for tileID in pTiles:
        for tile in getAllPossibilities(pTiles[tileID]):
            end = True
            gridId = [tileID]
            gridTile = [tile]
            used = {tileID}
            for i in range(1, len(pTiles.keys())):
                match = False
                for tId, t in pTiles.items():
                    if tId in used:
                        continue

                    prevL = []
                    prevT = []
                    if i%size != 0:
                        prevL = gridTile[i-1]
                    if i//size != 0: 
                        prevT = gridTile[i-size]
                    
                    for nextTile in getAllPossibilities(t):
                        if len(prevL) != 0 and not np.all(prevL[:, -1] == nextTile[:, 0]):
                            continue
                        if len(prevT) != 0 and not np.all(prevT[-1, :] == nextTile[0, :]):
                            continue
                        gridId.append(tId)
                        gridTile.append(nextTile)
                        used.add(tId)
                        match = True
                        break
                if not match:
                    end = False
                    break
            if end:
                gridId = np.array(gridId).reshape((size,size))
                gridTile = np.array([gridTile]).reshape((size,size, len(gridTile[0]), len(gridTile[0])))
                return (gridId, gridTile, np.prod(np.array([gridId[0,0], gridId[0,-1], gridId[-1,0], gridId[-1,-1]], 'int64')))

def recompose(pTiles):
    _, totalWidth, _, tileWidth = pTiles.shape
    tileWidth -= 2
    size = tileWidth * totalWidth
    newArray = np.empty((size, size), dtype=str)
    for i, y in enumerate(range(0, size, tileWidth)):
        for j,x in enumerate(range(0, size, tileWidth)):
            newArray[y:y+tileWidth,x:x+tileWidth] = pTiles[i,j][1:-1,1:-1]
    return newArray


def part2(pId, pTiles):
    monster = np.array([
        list("                  # "),
        list("#    ##    ##    ###"),
        list(" #  #  #  #  #  #   ")
    ])
    image = recompose(pTiles)
    for nextImg in getAllPossibilities(image):
        count = 0
        shpMon = monster.shape
        for i in range(image.shape[0] - monster.shape[0] + 1):
            for j in range(image.shape[1] - monster.shape[1] +1):
                imgSli = nextImg[i:i+shpMon[0], j:j+shpMon[1]]
                match = True
                for y in range(imgSli.shape[0]):
                    for x in range(imgSli.shape[1]):
                        if monster[y][x] == " ":
                            continue
                        if imgSli[y][x] != monster[y][x]:
                            match = False
                            break;
                if match:
                    count += 1
        if count > 0:
            countImg = Counter(image.ravel())
            countMon = Counter(monster.ravel())
            return countImg['#'] - count * countMon['#']

if __name__ == "__main__":
    tiles = parser("input.txt")
    gridId, gridTile, p1 = part1(tiles)
    print(p1)
    print(part2(gridId, gridTile))
