"""a function that finds peaks in an arrays and returns them"""
array = [2, 8, 3, 7, 9, 2, 10, 11, 15, 1]
def find_peaks(array):
    length = len(array) - 2
    indices = [] # list of peaks

    for i in range(length):
#comparing 3 elements of the array to check for peak
        if array[i] < array[i + 1] > array[i + 2]:
            indices.append(array[i +1])
    return indices

print(find_peaks(array))
