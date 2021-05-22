def perfect_num():
    num=int(input("enter the number"))
    sum=0
    i=1
    while i<num:
        if num%i==0:
            sum=sum+i
        i+=1
    if sum==num:
        print("perfect number")
    else:
        print("not perefct number")
# num=int(input("enter the number"))
perfect_num()







