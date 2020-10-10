num=int(input("enter the number of terms: "))
n1=0
n2=1
count=0
if num<=0:
    print("enter a positive integer")
elif num==1:
    print('fibonacci seies: ',n1)
else:
    print("fibonacci series: ")
    while count<num:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count=count+1
