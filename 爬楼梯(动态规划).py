def climbStairs(n: int) -> int:
    A = [0]
    for i in range (1,n+1):
        if i == 1:
            A.append(1)
        elif i == 2:
            A.append(2)
        else:
            A.append(A[i-1]+A[i-2])
    return A[n]
print(climbStairs(5))
