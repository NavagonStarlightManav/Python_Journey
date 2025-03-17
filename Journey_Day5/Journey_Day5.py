fruits=["Apple","Peach","Strawberry"]
for fruit in fruits:
    print(fruit)
    print(fruit+"pie")
    print(fruits)
print(fruits)

student_scores=[120,142,185,120,24,59,68,199,78]

total_exam_score=sum(student_scores)
print(total_exam_score)

sum=0
for score in student_scores:
    sum+=score
print(sum)

max_number=max(student_scores)
print(max_number)

maximum=student_scores[0]
for max in student_scores:
    if max>maximum:
        maximum=max
    else:
        continue
print(f"The max number is {maximum}")

for number in range(1,12):
    print(number)

for number in range(1,12,3):
    print(number)

sum=0
for number in range(1,101):
    sum+=number
print(sum)

for num in range(1,101):
    if num % 3==0 and num % 5==0:
        print("FizzBuzz\n")
    elif num % 3 ==0:
        print("Fizz\n")
    elif num % 5 ==0:
        print("Buzz\n")
    else:
        print(num)
        print("\n")

