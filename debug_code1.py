# def greet(*names):
#     for name in names:
#         print("Welcome", name)


# greet("Rinki", "Vishal", "Kartik", "Bijender") 



# def info(name, age ): 
#    print(name + " is " +age + " years old")

# info("Sonu")
# info("Sana", "17")
# info("Umesh", "18") 



# def studentDetails(name,currentMilestone,mentorName):
#     print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)


# studentDetails("Nilam","loop") 
# # Edit on Github


# def function_print_lines():  
#     print("Mera naam Rishabh hai")
#     print("Main NavGurukul ka co-Founder hun.")
# function_print_lines()





# def add_numbers(add1,add2):
#     add3=add1+add2
#     print("add function=",add3)
# add_numbers(56,12)

# add1=[50,60,10]
# add2=[10,20,13]
def add_numbers(add1,add2):
    i=0
    # list=[]
    sum=0
    while i<len(add1):
        j=0
        while j<len(add2):
            sum=add1[i]+add2[i]
            # list.append(sum)
            j=j+1
        print(sum)
        i=i+1
add_numbers([50,60,10],[10,20,13])
    




