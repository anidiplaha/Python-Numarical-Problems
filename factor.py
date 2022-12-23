n=int(input("Enter A Number::"))

print("Factor of :",n,"is:",)

for i in range(1,n):
    if((n % i)==0):
        print(i,",",end='')
