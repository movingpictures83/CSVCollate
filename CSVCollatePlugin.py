import PyPluMA
import math

def toFloat(arr):
    retval = []
    for value in arr:
        retval.append(float(value))
    return retval

def flatten(arr):
    retval = []
    for row in arr:
        for value in row:
            retval.append(value)
    return retval

def min(arr):
    minimum = math.inf
    for value in arr:
        if (value < minimum):
            minimum = value
    return minimum

def max(arr):
    maximum = -1
    for value in arr:
       if (value > maximum):
           maximum = value
    return maximum

def mean(arr):
    n = float(len(arr))
    sum = 0
    for value in arr:
        sum += value
    return sum/n

def err(arr):
    return (max([abs(mean(arr)-min(arr)), abs(max(arr)-mean(arr))]))

def crosssection(arr, startrow, endrow, startcol, endcol):
    retval = []
    for i in range(startrow, endrow):
        print(arr[i])
        retval.append(arr[i][startcol:endcol])
    return retval

class CSVCollatePlugin:
    def input(self, filename):
        infile = open(filename, 'r')
        self.parameters = dict()
        for line in infile:
            line = line.strip()
            contents = line.split('\t')
            self.parameters[contents[0]] = contents[1]

    def run(self):
        self.startrow = int(self.parameters["startrow"])-1
        self.endrow = int(self.parameters["endrow"])
        self.startcol = int(self.parameters["startcol"])-1
        self.endcol = int(self.parameters["endcol"])
        self.datafile = PyPluMA.prefix()+"/"+self.parameters["data"]

    def output(self, filename):
        mydata = open(self.datafile, 'r')
        outfile = open(filename, 'w')
        for line in mydata:
           datafromfile = []
           contents = line.strip().split('\t')
           print(contents[0])
           datafile = open(PyPluMA.prefix()+"/"+contents[0],'r')
           x = contents[1]
           y = contents[2]
           for line2 in datafile:
               contents2 = line2.strip().split(',')
               datafromfile.append(contents2)
           #print(datafromfile)
           #crosssection = datafromfile[self.startrow:self.endrow][self.startcol:self.endcol]
           linear = toFloat(flatten(crosssection(datafromfile, self.startrow, self.endrow, self.startcol, self.endcol)))
           print(linear)
           outfile.write(x+","+y+","+str(mean(linear))+","+str(err(linear))+"\n")
