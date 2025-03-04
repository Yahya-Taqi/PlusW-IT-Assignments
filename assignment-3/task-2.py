def FindMaxElement(list):
    maxValue = list[0]
    for num in list:
        if maxValue < num:
            maxValue = num
    
    return maxValue

def FindMinElement(list):
    minValue = list[0]
    for num in list:
        if minValue > num:
            minValue = num
    
    return minValue

numbers = [5, 6, 9, 7, 2, 1]

print(f"The maximum element in the list is: {FindMaxElement(numbers)}")
print(f"The minimum element in the list is: {FindMinElement(numbers)}")