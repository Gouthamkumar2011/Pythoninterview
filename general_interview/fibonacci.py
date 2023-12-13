# #recursive Approach
# #Mathematical expression : F(n) = F(n-1) + F(n-2)

def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)


if __name__ == "__main__":
    n = 9
    print(n, "th Fibonacci Number: ")
    print(fibonacci(n))


#Dynamic Programming Approach
def fibonacci_dp(n):
    f = [0,1]
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]

print(fibonacci_dp(9))