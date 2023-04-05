def GetLatLong():

    myfile = open("Soup.txt")
    contents = myfile.read()
    myfile.close()

    #print(contents.find("latLong", 449144))

    locs = []
    begInd = 0
    #while contents.find("GeoCoordinates", begInd) >= 0:
    while contents.find("latLong", begInd) >= 0:
        begInd = contents.find("latLong", begInd) + 1
        locs.append(begInd - 1)
        #print(begInd)
    #print(locs)

    lines = []
    for i in locs:
        lines.append(contents[i:i+100])
    #print(lines)

    lats = []
    longs = []
    for i in lines:
        latbeg = i.find("latitude") + 10
        latend = i.find(",", latbeg)
        lats.append(i[latbeg:latend])
    
        longbeg = i.find("longitude") + 11
        longend = i.find("}", longbeg)
        longs.append(i[longbeg:longend])
   
    lats = [float(i) for i in lats]
    longs = [float(i) for i in longs]

    return [lats,longs]

if __name__ == "__main__":
    [X,Y] = GetLatLong()
    print(X)
    print(Y)
    
