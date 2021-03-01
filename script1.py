import math


def readData(dataPath):
    """Return the data at dataPath as an array of integers."""
    with open(dataPath, 'r') as f:
        data = [int(line) for line in f.readlines()]
    return data


def bmi(weight, height): return math.floor((weight / (height ** 2)) * 703)


def bmiChart(minHeight, maxHeight, minWeight, maxWeight):
    weightList = list(range(minWeight, maxWeight))
    print('W/L', *weightList, sep=' ')

    for height in range(minHeight, maxHeight):
        bmiList = [bmi(weight, height) for weight in range(minWeight,
                                                           maxWeight + 1)]
        print(height - 1, *bmiList, sep='  ')


def main():
    minHeight, maxHeight, minWeight, maxWeight = readData("data.txt")
    bmiChart(minHeight, maxHeight, minWeight, maxWeight)


if __name__ == "__main__": main()





