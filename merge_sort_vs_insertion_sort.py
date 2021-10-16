from typing import TypeVar, List, Callable
import random
import time
from matplotlib import pyplot as plt

T = TypeVar("T")  # represents generic type
data = [] # Data that will be sorted

# The mergeSort function was taken from https://www.geeksforgeeks.org/merge-sort/
# Written by Mayank Khanna
def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Insertion sort. Taken from https://www.geeksforgeeks.org/python-program-for-insertion-sort/
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Generate n random numbers
def generate_data(n):
    return [random.randint(1, 10000) for i in range(n)]

def test_insertion():
    insertionSort(data)

def test_merge():
    mergeSort(data)

def main():

    data_sizes = []
    insertion_times = []
    merge_times = []
    # Vary data size
    for i in range(1, 110):
        insertion_times_before_averaging = []
        merge_times_before_averaging = []
        # Repeat process 100 times to reduce outliers
        for j in range(100):
            data = generate_data(i)
            # Copy data to keep as much the same as possible between sorts
            data2 = data

            # Use insertion sort and time it
            start_time = time.perf_counter()
            insertionSort(data)
            end_time = time.perf_counter()
            insertion_time = end_time - start_time

            data = data2

            # Use merge sort and time it
            start_time = time.perf_counter()
            mergeSort(data)
            end_time = time.perf_counter()
            merge_time = end_time - start_time

            insertion_times_before_averaging.append(insertion_time)
            merge_times_before_averaging.append(merge_time)

        data_sizes.append(i)
        # Average out the sub-trial times into a single time
        insertion_times.append(sum(insertion_times_before_averaging) / len(insertion_times_before_averaging))
        merge_times.append(sum(merge_times_before_averaging) / len(merge_times_before_averaging))

    plt.scatter(data_sizes, insertion_times, c='r', label="Insertion Sort Times")
    plt.scatter(data_sizes, merge_times, c='b', label="Merge Sort Times")

    plt.legend(loc="upper left")
    plt.title("Insertion Sort vs. Merge Sort Runtimes")
    plt.xlabel("Input Data Size")
    plt.ylabel("time (s)")

    plt.show()


if __name__ == "__main__":
    main()
