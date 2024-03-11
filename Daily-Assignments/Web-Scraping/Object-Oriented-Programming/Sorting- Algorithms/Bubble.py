#swaps if they are in the wrong order. I keeps going through the elements

arr = [ 63, 35,21, 11, 29, 10, 89, 90]

def bubble_sort(arr):
    n= len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubble_sort(arr)
print("sorted array:", arr)

#How to get the time complexity
