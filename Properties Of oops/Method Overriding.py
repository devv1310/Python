# acccess with super() functions super().name of upur functions
class a:
    def add(self,x,y):
        return x+y,
class b(a):
    def add(self,x,y):
        run=super().add(x,y)
        print(run)
        return run
obj=b()
result=obj.add(5,6)

