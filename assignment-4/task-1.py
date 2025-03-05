import numpy as np

arr_1d = np.array([6, 2, 4, 3, 5, 1])
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def NumpyPrintArray(array):
    print(f"{array}\n")

def SumOfArray(array):
    print(f"Sum of array: {np.sum(array)}\n")
    
def MeanOfArray(array):
    print(f"Mean of array: {np.mean(array)}\n")
    
    
def MedianOfArray(array):
    print(f"Median of array: {np.median(array)}\n")

def TranposeOfMatrix(matrix):
    print(f"Transpose of array:\n {np.transpose(matrix)}\n")
    
def MinMaxOfArray(array):
    print(f"Minimum value: {np.min(array)}")
    print(f"Maximum value: {np.max(array)}\n")

def SortArray(array):
    print(f"Sorted array:\n{np.sort(array)}\n")

def UniqueElements(array):
    print(f"Unique elements in array:\n{np.unique(array)}\n")

NumpyPrintArray(arr_1d)
NumpyPrintArray(arr_2d)

SumOfArray(arr_1d)
SumOfArray(arr_2d)

MeanOfArray(arr_1d)
MeanOfArray(arr_2d)

MedianOfArray(arr_1d)
MedianOfArray(arr_2d)

TranposeOfMatrix(arr_1d)
TranposeOfMatrix(arr_2d)

MinMaxOfArray(arr_1d)
MinMaxOfArray(arr_2d)

SortArray(arr_1d)

UniqueElements(arr_1d)
UniqueElements(arr_2d)