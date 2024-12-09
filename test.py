def recursion(num):
    if num == 1:
        return num
    else:
        return num * recursion(num - 1)
    
print(recursion(6))