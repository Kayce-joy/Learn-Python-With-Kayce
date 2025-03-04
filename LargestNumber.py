#easiest way
def largnum(n):
    return max(n)

print(largnum([10, 3, 5, 8, 2]))  # Output: 10
print(largnum([-1, -5, -3, -10]))  # Output: -1


#Loop approach
def largn(n):
    largest=n[0]

    for num in n:
        if num>largest:
            largest=num

    return largest
        
print(largn([10, 3, 5, 8, 2]))  # Output: 10
print(largn([-1, -5, -3, -10]))  # Output: -1


