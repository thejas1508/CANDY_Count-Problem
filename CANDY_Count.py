Money_in_hand=int(input("Enter the Money that Ryan have:"))
total_candy=Money_in_hand/0.25
print("total candies Ryan can buy:",total_candy)
Wrapper_count=total_candy
Extra_candy=Wrapper_count/3
print("Extra candies:",Extra_candy)
Wrapper_count=Extra_candy+total_candy%3
print("Wrapper_count:",Wrapper_count)
total_candy=total_candy+Extra_candy
print("total_candies:",total_candy)
while (Wrapper_count>3):
        Wrapper_count/=3
        total_candy=total_candy+Wrapper_count
print("the total number of candies Ryan Have at last:",total_candy)



