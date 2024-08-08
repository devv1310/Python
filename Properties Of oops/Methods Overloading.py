class a:
    def add(*n):
        sum=0
        for i in n:
            sum=sum+i
        return sum
obj=a
print(obj.add(10,20,30))
print(obj.add(10,20,30,40,50))
