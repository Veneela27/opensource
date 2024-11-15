x=int(input())
if x>=1 and x<=12:
    if x>2 and x<6:
        print("Spring")
    elif x>5 and x<9:
        print("Summer")
    elif x>8 and x<12:
        print("Autumn")
    elif x<3 or x==12:
        print("Winter")
    else:
        print("Invalid")
else:
    print("Invalid")
