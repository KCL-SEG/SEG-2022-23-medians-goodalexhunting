"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def getMedian(numList):
    numList.sort()
    if len(numList) == 1:
        return numList[0]
    if len(numList)%2 > 0:
        return numList[int(len(numList)/2)] 
    else:
        n1 = numList[int(len(numList)/2)] 
        n2 = numList[int(len(numList)/2)-1]
        return (n1+n2)/2
    

if __name__ == "__main__":
    while True:
        try:
            print("Enter a list of numbers separated by commas: ")
            numbers = [float(value) for value in input().split(",")]
            print(getMedian(numbers))
        except ValueError:
            print("Some input could not be converted to a number!")
        else:
            break



