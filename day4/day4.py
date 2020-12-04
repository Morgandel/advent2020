import re

def openInputPassports(pFileName):
    f = open(pFileName, 'r')
    newPassport = dict()
    content = [newPassport]
    for line in f:
        line = line.strip('\n')
        if line:
            for splited in line.split(" "):
                k, v = splited.split(":")
                newPassport[k] = v
        else:
            newPassport = dict()
            content.append(newPassport)
    return content

def countValidPassports(pContent, pKey):
    validPassports = 0
    for pp in pContent:
        valid = True
        for key in pKey:
            if key not in pp:
                valid = False
                break
        if valid:
            validPassports += 1
    return validPassports

def countValidPassportsStrictly(pContent, pKey):
    validPassports = 0
    for pp in pContent:
        valid = True
        for key in pKey:
            if key[0] not in pp:
                valid = False
                break
            val = pp[key[0]]
            if not key[1](val):
                valid = False
                break
            elif(len(key) == 4):
                if not xInRange(int(val), key[2], key[3]):
                    valid = False
                    break
        if valid:
            validPassports += 1
                
    return validPassports

def hgtVerif(pValue):
    if(re.match('^[0-9]+(in|cm)$', pValue)):
        if pValue.endswith('cm'):
            return xInRange(int(pValue.strip('cm')), 150, 193)
        if pValue.endswith('in'):
            return xInRange(int(pValue.strip('in')), 59, 76)
    return False

def xInRange(pValue, pMin, pMax):
    return pValue >= pMin and pValue <= pMax

if __name__ == "__main__":
    content = openInputPassports("input.txt")
    neededKey = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid1 = countValidPassports(content, neededKey)
    print(valid1)
    year = lambda x : re.match('^[0-9]{4}$', x)
    hgt = lambda x : hgtVerif(x)
    hcl = lambda x : re.match('^#[0-9a-f]{6}$', x)
    ecl = lambda x : x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    pid = lambda x : re.match('^[0-9]{9}$', x)
    keyVerif = [("byr", year , 1920, 2002), ("iyr", year, 2010, 2020), ("eyr", year, 2020, 2030), ("hgt", hgt), ("hcl", hcl), ("ecl", ecl), ("pid", pid)]
    valid2 = countValidPassportsStrictly(content, keyVerif)
    print(valid2) 
