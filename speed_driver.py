def speed_123(speed):
    i=75
    point=0
    while i<=speed:
        if speed>70:
            point=point+1
            i=i+5
        if speed<70:
            print("ok")
        else:
            print("licence suspended")
user=int(input("enter the number"))
speed_123(user)
        







