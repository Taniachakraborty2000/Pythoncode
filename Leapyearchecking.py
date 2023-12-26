year=int(input("enter any year"))#2012
if(year%400==0):
    print(year," is leap year")
elif(year%4==0 and year%100!=0):#leap year
    print(year," is leap year")
else:
    print(year,"is not leap year")