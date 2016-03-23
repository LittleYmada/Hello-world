#a bubble sort by python

  

a=[1,2,3,4,5,6,7,8,11,2,34,14,45,32,3,1,0]




#bubble sort
def  sorts(a):
    judge=0
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                judge=1
            print(len(a)*i+j)
        if judge==0:
            break

sorts(a)
print(a)

#quick sort
def qsorts(a):
    a=3
