def show_function(a_123):
    i=0
    while i<=user:
        if i%2==0:
            print(i,"even number")
        else:
            print(i,"odd number")
        i+=1
user=int(input("enter the number"))
show_function(user)


