# def calculator(add1,add2,add3):
#     if add3=add1+add2:
#         print(add3)
#     if add3=add1-add2:
#         print(add3)
#     if add3=add1*add2:
#         print(add3)
#     if add3=add1%add2:
#         print(add3)
#     if add3=add1//add2:
#         print(add3)
# user1=int(input("enter the number"))
# user2=int(input("enter the number"))
# user3=input("enter the symbol")
# calculator(user1,user2,user3)



# def calculator(add1,add2):
#     add2=add1+add2
#     print(add2)
#     add2=add1-add2
#     print(add2)
#     add3=add1*add2
#     print(add3)
#     add3=add1%add2
#     print(add3)
# calculator(5,1)






def multiple_list(var1,var2):
    i=0
    list=[]
    while i<len(var1):
        j=0
        while j<len(var2):
            s=var1[i]*var2[i]
            list.append(s)
            #print(s)
            j=j+1
            i=i+1
        print(list)
multiple_list([5, 10, 50, 20],[2, 20, 3, 5]) 




