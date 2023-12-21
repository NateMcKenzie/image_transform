def main():
    inputMatrix = []
    with open("input.txt") as inputFile:
        for line in inputFile:
            values = []
            splits = line.split(" ")
            #Remove newline character
            splits.pop(-1)
            for split in splits:
                values.append(int(split))
            inputMatrix.append(values)

    for line in inputMatrix:
        print(line)


main()
