# Subscripting and can also apply negative numbers to start string backwards
print("Manav"[4])
print("Manav"[-2])

# Integer + whole number
print(123+456)

# Large Integers for interpreting  integers with commas
print(123_456_789)

# Float = Floating Point Number
print(3.14159)

#Boolean
print(True)
print(False)

len("Hello")

print(type("Hello"))
print(type(456))
print(type(3.14))
print(type(True))

print(int("456")+int("745"))

print("Number of letters in your name  " + str(len(input("Enter Your name"))))

print(type(6/2)) # Python is implicitly typecasting here returning result in float
print(type(6//3)) # Python is not returning result as integer

print(6-4)
print(2**3)

# Here Also Same rules of operation priority are followed and left to right  () , ** , * and / , + , -
print(3*(3+3)/3-3)

# Rounding of numbers
bmi = 84/1.65**2

print(bmi)
print(int(bmi))

print(round(bmi))
print(round(bmi,2))

# use of f strings
score = 0
score +=1
print(score)

print("Your score is " + str(score))

height = 1.8
is_winning = True

# Now with the help of f strings  all these variables can be put with any problems
print(f"Your score is {score},Your height is {height}. You are winning is {is_winning} \n")

print("Welcome to the tip Calculator!")
bill = float(input("What was the total bill ? $"))
tip = int(input("How much tip would you like to give ? 10 , 12 , or 15 ?"))
number_of_people = int(input("how many people to split the bill ? "))
Total_Bill=((tip/100)*bill)+bill
print(f" Each person should pay : ${round((Total_Bill/number_of_people),2)}")