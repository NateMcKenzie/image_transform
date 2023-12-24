import drawing

def main():
    #It's not pretty, but I'm just going to the same thing for each channel 
    redMatrix = readMatrix("red.txt")
    greenMatrix = readMatrix("green.txt")
    blueMatrix = readMatrix("blue.txt")
    elementary = flipYMatrix(len(redMatrix))

    #Flip Y
    flippedR = multiplyMatrix(redMatrix,elementary)
    flippedG = multiplyMatrix(greenMatrix,elementary)
    flippedB = multiplyMatrix(blueMatrix,elementary)

    drawing.draw_side_by_side((redMatrix,greenMatrix,blueMatrix), (flippedR,flippedG,flippedB))
    #Flip X
    flippedR = multiplyMatrix(elementary,redMatrix)
    flippedG = multiplyMatrix(elementary,greenMatrix)
    flippedB = multiplyMatrix(elementary,blueMatrix)

    drawing.draw_side_by_side((redMatrix,greenMatrix,blueMatrix), (flippedR,flippedG,flippedB))

#Assume all matrices are square 
def flipYMatrix(size:int):
    #Build an identity matrix that has been flipped on Y
    matrix = []
    emptyRow = [0 for _ in range(size)]
    for i in range(size):
       newRow = emptyRow.copy()
       newRow[-i-1] = 1
       matrix.append(newRow)
    return matrix

#For this program, we are always multiplying two equal sized matrices
def multiplyMatrix(a,b):
    newMatrix = []
    for row in a:
        newRow = [] 
        for i in range(len(a)):
            col = [entries[i] for entries in b]
            newRow.append(dot(row,col))
        newMatrix.append(newRow)
    return newMatrix

def dot(row,col):
    result = 0
    for i in range(len(row)):
        result += row[i]*col[i]
    return result

def readMatrix(file):
    inputMatrix = []
    with open(file) as inputFile:
        for line in inputFile:
            values = []
            splits = line.split(" ")
            #Remove newline character
            splits.pop(-1)
            for split in splits:
                values.append(int(split))
            inputMatrix.append(values)
    return inputMatrix



main()
