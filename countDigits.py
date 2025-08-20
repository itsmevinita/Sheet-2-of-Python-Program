N= int(input("enter A:")) 
count=0
temp=N
while temp>0:
    count+=1
    temp//=10
    print(" numbers of digits =",count)
