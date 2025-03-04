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
