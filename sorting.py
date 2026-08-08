#selection sort
def selection_sort(arr, n):
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                arr[j], arr[min_index] = arr[min_index], arr[j]
    return arr
arr = [9, 5, 4, 3, 7, 1, 2]
n = len(arr)
print(selection_sort(arr, n))
#bubble sort
def bubble_sort(arr, n):
    for i in range(n):
        for j in range(i+1, n):
            if arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr
print(bubble_sort(arr, n))