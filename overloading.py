class clac:
    def add(self,a,b,c=0):
        if c>0:
            print("a+b+c={}".format(a+b+c))
        else:
            print("a+b={}".format(a + b ))
c1=clac()
c1.add(10,20)