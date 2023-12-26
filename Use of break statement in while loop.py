num=int(input("enter any number"))#get userinput for any number , 7
i=1#initialization 
while(i<=num):#1<=7,2<=7,3<=7
    if(i==4):#1==4,2==4,3==4,4==4
        break;#stop
    else:
        print(i)#1,2,3
    i+=1#2,3,4
else:
    print("This is else part")