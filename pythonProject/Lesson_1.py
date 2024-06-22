age = int(input("How old are you? "))

if 30 <= age <= 35:
    print("You're old enough to be a senator but not president as you're " + str(age)), "years old"
elif age >=35:
    print ("you're old enough to be senator and president as you're" , age, "years old")

else:
    print("You're not old enough to be a senator or prez as you're only" , age, "years old")