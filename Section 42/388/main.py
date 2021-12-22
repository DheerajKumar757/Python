def Fibonacci(N):
    if N < 0:
        return "N should be more than or equal to 0"
    elif N==0:
        return 0
    elif N==1:
        return 1
    else:
        return Fibonacci(N-1) + Fibonacci(N-2)

print(Fibonacci(7))
