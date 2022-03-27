year=int(input("Which year do you wnat to check? "))
#first it should be devided by 4 and no  remaining 
if year %4==0:
    if year %100==0:
        if year %400==0:
            print("Its Leap Year")
        else:
            print("Its not Leap Year")
    else: 
        print("Its a Leap year")
else:
    print("Its not a leap year")     
