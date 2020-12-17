from collections import Counter
import itertools as itt

def parser(pFileName):
    content = []
    f = open(pFileName, 'r')
    return [line.strip() for line in f]

def notStart(coord):
    for c in coord:
        if c != 0:
            return True
    return False

def part1(pContent, pDim):
    cubes = set()
    for y, line in enumerate(pContent):
        for x, elem in enumerate(line):
            if elem == '#':
                coord = pDim * [0]
                coord[0], coord[1] = y, x
                cubes.add(tuple(coord))
    for i in range(6):
        newCubes = set()
        counts = Counter()
        for c in cubes:
            for coord in itt.product([-1,0,1], repeat=pDim):
                if notStart(coord):
                    toAdd = []
                    for j in range(pDim):
                        toAdd.append(coord[j]+c[j])
                    counts[tuple(toAdd)] += 1

        for coord, count in counts.items():
            if count == 3 or (coord in cubes and count == 2):
                newCubes.add(coord)
        cubes = newCubes
    return len(cubes)


if __name__ == "__main__":
    content = parser('input.txt')
    print(part1(content, 3))
    print(part1(content, 4))
