nums=[1,2,3,4,5]
target=9
def wow(a,b):
    i=0
    j=1

    while 0<=i<=(len(a)-1):


        if (a[i]+a[j])==b:
            x=[i,j]
            print(x)
            return 
        i=i+1
        j=j+1

wow(nums,target)
