class Bin:
    
    def getNumPts(self):
        return len(self.xPts)
    
    def getMidpoint(self):
        return self.leftSide + self.spacing/2 
    
    @property
    def rightSide(self):
        return self.leftSide + self.spacing
    
    @property
    def value(self):
        "preserve volume during the binning"
        totalVol = 0
        for ind,xPt in enumerate(xPts):
            #get leftOfBox
            if ind == 0:
                if self.leftSide < xPt:
                    leftOfBox = self.leftSide
                else:
                    leftOfBox = xPt
            else:
                leftOfBox=xPt[ind-1]
            #get rightOfBox
            if ind == len(xPts):
                if self.rightSide > xPt:
                    rightOfBox = self.rightSide
                else:
                    rightOfBox = xPt
            else:
                rightOfBox=xPt[ind+1]
            boxLength = rightOfBox-leftOfBox
            boxVol = boxLength*yPt
            totalVol += boxVol
        totalHeight = totalVol/self.spacing
        return totalHeight
    
    def __init__(self, leftSide=None, spacing=None, numPreviousBins=None):
        self.numPreviousBins =  numPreviousBins
        self.value = 0.0
        self.xPts = []
        self.yPts = []
        self.leftSide = leftSide
        self.spacing = 0.0

#for each E, rebin the q's:
class SimpleRebin:
    """SimpleRebin() can 1) count the number of 
    data points that fall into a bin and post their total number as the data point value 
    for that bin and 2) take the values of the data points that fall within a given bin 
    and average them to give a composite data point value for that bin.  'binValue' controls
    which algorithm is used.
    
    newBins is either an integer or a numpy array of bins.
    """
#    #h,smallest,binWidth,junk = histogram(yS[:lim],numbins = 100)
#    if cutoffOfDosData:
#        xData = xS[:cutoffOfDosData]
#        yData = yS[:cutoffOfDosData]
#    else:
#        xData = xS
#        yData = yS
    #first sort the data (this should be moved to parnasis or otherwise)
    def __init__(self, xData, yData, newBins=None, binValue = 'countPoints', format = 'columns'):
        xData = np.sort(xData)
        sortedInds = np.argsort(xData)
        yData = yData[sortedInds]
        
        self.bins=[]
        if type(newBins) is type(1):
            # this algorithm is for data that has already been binned and we're going over the bins to rebin
            import math
            leftOverPts, numXdataInBin = math.modf(len(xData)/numBins)
            currentBin = Bin(numPreviousBins = int(numXdataInBin))
            for xPt,yPt in zip(xData,yData):
                if currentBin.getNumPts() >= numXdataInBin:
                    currentBin.spacing = xPt - currentBin.xPts[0]
                    self.bins.append(currentBin)
                    currentBin = Bin(numPreviousBins = int(numXdataInBin))
                currentBin.xPts.append(xPt)
                if binValue=='countPoints':
                    # then add together all the y axis values that fall within the new bin
                    currentBin.value += yPt
                elif binValue=='averagePoints':
                    #weight the average
                    numPointsInBin = currentBin.getNumPts()
                    currentBin.value = (numPointsInBin*currentBin.value + yPt)/(numPointsInBin+1)
        else:
            #assume newBins are equally spaced
            binCounter = 0
            binSize = newBins[1] - newBins[0]
            currentBin = Bin(spacing = binSize, leftSide = newBins[binCounter])
            for xPt,yPt in zip(xData,yData):
                if xPt >= currentBin.rightSide:
                    self.bins.append(currentBin)
                    binCounter += 1
                    currentBin = Bin(spacing = binSize, leftSide = newBins[binCounter])
                currentBin.xPts.append(xPt)
                currentBin.yPts.append(yPt) 
        # but when you plot, plot the y-axis value not at the x-axis pair, but at the midpoint between the x-axis pair
        # and the one up from it.  Assume there is an additional x-axis point at the end with the same spacing as all the others.

        
    def newYpts(self):
        return [bin.value for bin in self.bins]
    
    def newXCenters(self):
        return [bin.getMidpoint() for bin in self.bins]
    
    def getData(self):
        newXData = [bin.getMidpoint() for bin in bins]
        newYData = [bin.value for bin in bins]
        columnData = newXData,newYData
        if 'columns' in format:
            return columnData
        if 'rows' in format:
            data = n.array(columnData)
            data = data.transpose()
            rowData = data.tolist()
            return rowData