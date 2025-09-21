class Dust:
    def wow(self, the):
        sttr=the
        if sttr[0]==" " or sttr[0]=="+":
            x=1
            l=[]
            while True:
                if type(sttr[x])==int:
                    l.append(str(x))
                else:
                    break
                x=x+1
            y=str(l)
            z=int(y)
            print(z)
        elif sttr[0]=="-" or sttr[0]==("1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9"):
            x=1
            l=[sttr[0]]
            while True:
                if (sttr[x]=="1" or sttr[x]== "2" or sttr[x]== "3" or sttr[x]=="4" or sttr[x]=="5" or sttr[x]=="6" or sttr[x]=="7" or sttr[x]=="8" or sttr[x]=="9"):
                    l.append(sttr[x])
                else:
                    break
                x = x + 1
            print(l)
        else:
            print(0)
a=Dust()
a.wow("1234")





