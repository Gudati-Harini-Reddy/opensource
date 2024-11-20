# Enter your code here. Read input from STDIN. Print output to STDOUT
def maximum_mangoes(a,b,c):
    max_man_w=c-b
    max_man=max_man_w//a
    return max_man
a,b,c=map(int,input().split())
results=maximum_mangoes(a,b,c)
print(results)
