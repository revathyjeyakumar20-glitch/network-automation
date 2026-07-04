age = int(input("Please enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote")



mark = int(input("Please enter your mark: "))
if mark >= 90:
    print("You have an A grade.")
elif mark >=75:
    print("You have a B grade.")
elif mark >=50:
    print("You have a C grade.")
else:
    print("You have failed the exam.")



x=int(input("Please enter first number: "))
y=int(input("Please enter second number: "))
if x>y:
    print(f"{x} is greater than {y}.")
elif x<y:
    print(f"{x} is less than {y}.")
else:
    print(f"{x} is equal to {y}.")


x = int(input("Please enter a number: "))
if x%2 == 0:
    print(f"{x} is an even number.")
else:
    print(f"{x} is an odd number.")