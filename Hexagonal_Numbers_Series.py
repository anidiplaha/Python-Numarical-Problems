#1, 6, 15, 28, 45, 66, 91
#Formula Result=2*i*(2*i-1)/2
n=int(input("Enter Limit.. :"))
res=0
for i in range(0,n):
    res=2*i*(2*i-1)/2
    print(res)
