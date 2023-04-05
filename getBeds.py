def getBeds():
    myfile = open("Soup.txt")
    contents = myfile.read()
    myfile.close()
    
    locs = []
    begInd = 0

    while contents.find("isUndisclosedAddress", begInd) >= 0:
        begInd = contents.find("isUndisclosedAddress", begInd) + 1
        locs.append(begInd - 1)
    
    locs = [i+35 for i in locs]
    
    endInds = [ contents.find(",", i) for i in locs ]
    
    lines = []
    
    for i in range(len(locs)):
        lines.append( contents[ locs[i]:endInds[i] ] )
        
    lines = [ int(i) for i in lines ]
		
    return(lines)
    
if __name__ == "__main__":
    print(getBeds())