n=int(input("enter your no"))
i=1
sum=1
while i<=n:
    sum=sum*i
    if i<=n-1:
        print(n,end="*")
    else:
        print(n,end="=")
    n=n-1
print(sum)
    