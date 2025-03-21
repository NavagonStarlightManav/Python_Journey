programming_dictionary={
    "Bug":"An error in a program that prevents the program from running as expected",
    "Function":"A piece of code that you can easily call over and over again",
    "Loops":"The action of doing something over and over again",
    256:"Secret code for love"
}

print(programming_dictionary["Loops"])

#editing or adding a new key in dictionary
programming_dictionary[143]="Love ya buddy , gonna miss you a lot"
print(programming_dictionary)

# we can also create an empty dictionary
empty_dictionary={}

# # Wipe an existing dictionary
# programming_dictionary={}

print(programming_dictionary)

for key  in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades={}

for key in student_scores:
   if student_scores[key]>=91:
       student_grades[key]= "Outstanding"
   elif student_scores[key] >= 81 and student_scores[key]<=90:
       student_grades[key] = "Exceeds Expectation"
   elif student_scores[key] >= 71 and student_scores[key]<=80:
       student_grades[key] = "Acceptable"
   if student_scores[key]<=70:
       student_grades[key]= "Fail"

print(student_grades)

# we can also use list or dictionary as value for a key in our dictionary

capitals={
    "France":"Paris",
    "Germany":"Berlin",
}

# Nested list in Dictionary

Travel_log ={
    "France":["Paris","Lillie","Dijon"],
    "Germany":["Stuttgart","Berlin"],

}

print(Travel_log["France"][1])

nested_list=["A","B",["C","D"]]
print(nested_list[2][0])

# More nested list and dictionaries

Travel_log ={
    "France":{
        "Cities_Visited":["Paris","Lillie","Dijon"],
        "Total_visits":12,
    },
    "Germany":{
        "Cities_Visited":["Stuttgart","Berlin"],
        "total_visits":5,
    },
}

print(Travel_log["France"]["Total_visits"])
print(Travel_log["France"]["Cities_Visited"][2])