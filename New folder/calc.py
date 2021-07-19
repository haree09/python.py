from fun import add,sub,mul

n1=int(input("enter the n1="))
n2=int(input("enter the n2="))
ch=input('Enter the operetor')
if ch=='+':
     print(add(n1,n2))
elif  ch=='-':
    print(sub(n1,n2))
elif ch=='*':
    print(mul(n1,n2))

