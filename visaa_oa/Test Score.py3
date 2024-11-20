# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X, Y = map(int, input().strip().split())
if Y % X == 0 and Y <= N * X:
    print("YES")
else:
    print("NO")
