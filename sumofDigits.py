N= int(input("enter no:")) 
s=0
temp=N
while temp>0:
    digits=temp%10
    s+=digits
    temp//=10
    print(" numbers of digits =",s)
