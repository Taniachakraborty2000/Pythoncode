n=int(input("enter any  number"))#get user input for any number,4
def factorial(n):#function defining 
    if(n>1):#(4>1),(3>1),(2>1),(1>1)
        return n*factorial(n-1)#4*3,4*3*2,4*3*2*1=24
    else:
        return 1   
factorial(n)#function calling
print("The factorial of ",n ," is",factorial(n))#24