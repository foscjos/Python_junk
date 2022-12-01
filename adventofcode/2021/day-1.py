def numberOfIncreases():
    previous = None
    total = 0
    with open('day1-input.txt', 'r') as file:
        measurementList = file.readlines()
        for measurement in measurementList:
            if (previous is not None and int(measurement.strip()) > previous):
                total +=1
            previous = int(measurement.strip())
        print('Result:', end=' ')
        print(total)
numberOfIncreases()