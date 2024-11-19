# Enter your code here. Read input from STDIN. Print output to STDOUT
x,y,z=map(int,input().split())
if x+y<=z:
    print(2)
elif x<=z:
    print(1)
else:
    print(0)
