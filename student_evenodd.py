

def check_numbers_list(var1,var2):
    i=0
    while i<len(var1):
        j=0
        while j<len(var2): 
            if var1[i]%2==0 and var2[j]%2==0:
                print("dono even hai")
            else:
                print("dono even nahi hai")
            j=j+1
            i=i+1
check_numbers_list([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87]) 