#uses what is called divide and concur strategy. It works by selcting a pivot and pationing them according to what is >< than the pivot.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

arr = [ 63, 35,21, 11, 29, 10, 89, 90]
sorted_array = quick_sort(arr)
print("Sorted array is:", sorted_array)
