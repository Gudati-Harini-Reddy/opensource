# Enter your code here. Read input from STDIN. Print output to STDOUT
bill_price=int(input())
dis_1=bill_price*0.1
dis_2=100
if dis_1>=dis_2:
    final_p=bill_price-dis_1
else:
    final_p=bill_price-dis_2
print(int(final_p))
