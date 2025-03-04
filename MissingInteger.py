def task1(a):
    arr=len(a)
    myset=set()

    for num in a:
        if num > 0:
            myset.add(num)

    for i in range(1,arr+1):
        if i not in myset:
            return i
        
            return arr+1

print(task1([1, 3, 6, 4, 1, 2]))  # Output: 5
print(task1([1, 2, 3]))  # Output: 4
print(task1([-1, -3]))  # Output: 1
print(task1([2, 3, 7, 6, 8, -1, -10, 15]))  # Output: 1
print(task1([1, 2, 0]))  # Output: 3



#Optimized Approach (O(n) Time, O(1) Space)
def missing_integer(arr):
    n = len(arr)

    # Step 1: Swap numbers to correct positions
    for i in range(n):
        while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:  
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]  # Swap numbers

    # Step 2: Find the first missing number
    for i in range(n):
        if arr[i] != i + 1:
            return i + 1  # First missing positive number

    return n + 1  # If all are in place, return n+1


print(missing_integer([3, 4, -1, 1]))  # Output: 2
print(missing_integer([1, 2, 3]))      # Output: 4
print(missing_integer([-1, -3]))       # Output: 1
print(missing_integer([2, 3, 7, 6]))   # Output: 1
print(missing_integer([1, 2, 0]))      # Output: 3

