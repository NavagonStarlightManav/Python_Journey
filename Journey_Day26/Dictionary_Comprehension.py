names=['Alex','beth','caroline','dave','eleanor','freddie']
import random
student_scores={student:random.randint(1,100) for student in names}
print(student_scores)

passed_students={key:value for (key,value) in student_scores.items() if value>60}
print(passed_students)

student_dict={
    "students":["Angela","James","Lily"],
    "score":[56,76,98]
}

for (key,value) in student_dict.items():
    print(key)

import pandas
student_df=pandas.DataFrame(student_dict)

for (index , row ) in student_df.iterrows():
    print(row.score)

