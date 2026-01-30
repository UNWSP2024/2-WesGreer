# Average Age program
# Written by Wesley Greer on 1/30/2026
def average_age():
    # Get User Input
print("Tell me the ages of five of your friends, and I'll tell you the average.")
age1 = float(input("What is your first friend's age? "))
age2 = float(input("What is your second friend's age? "))
age3 = float(input("What is your third friend's age? "))
age4 = float(input("What is your fourth friend's age? "))
age5 = float(input("What is your fifth friend's age? "))
    # Average the ages
avg = (age1 + age2 + age3 + age4 + age5) / 5
    # Print the results
print("The average of your friends' ages is...")
print(avg)
# Line which calls the above function.
average_age()
