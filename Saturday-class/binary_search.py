#you keep dividing your number by 2 until you find the target.
#list should be in ascending order (from smallest to largest)

def binary_search(num, target):
    left = 0
    right  =len(num) -1 

    while left <= right:
        mid_num = round((left + right)// 2)
        if num [mid_num] == target:
            return mid_num
        elif target < num[mid_num]:
            right = mid_num -1

        else:
            left = mid_num + 1

    return -1
print(binary_search([-1, 0, 3, 5, 9, 12], 9))
#This Python code implements a binary search algorithm to find the index of a target number in a sorted list. Here's an explanation of the code:

#1. **Function Definition:**
#   - `def binary_search(num, target):` defines a function named `binary_search` that takes two arguments: `num`, which is a sorted list of numbers, and `target`, which is the number to search for in the list.

# 2. **Initialization:**
   # - `left = 0` initializes the left pointer to the beginning of the list.
  #  - `right = len(num) - 1` initializes the right pointer to the end of the list.

# 3. **Binary Search Algorithm:**
#    - The `while` loop runs as long as the left pointer is less than or equal to the right pointer.
 #   - `mid_num = round((left + right) // 2)` calculates the middle index of the current search range.
 #   - If the number at the middle index is equal to the target, `return mid_num` returns the index where the target is found.
 #   - If the target is less than the number at the middle index, it updates the right pointer to `mid_num - 1` to search in the left half of the list.
 #   - If the target is greater than the number at the middle index, it updates the left pointer to `mid_num + 1` to search in the right half of the list.

# 4. **Return Value:**
#    - If the target is not found in the list, `return -1` is executed after the while loop.
   
# 5. **Function Call:**
 #   - `print(binary_search([-1, 0, 3, 5, 9, 12], 9))` calls the `binary_search` function with a sorted list `[-1, 0, 3, 5, 9, 12]` and a target number `9`. It prints the index where `9` is found using binary search.

# This code efficiently searches for a target number in a sorted list using the binary search algorithm.