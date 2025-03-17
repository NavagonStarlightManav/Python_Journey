import random
import List_Module


random_integer=random.randint(1,15) #It is an inclusive function
print(random_integer)

print(List_Module.Export_Value)

random_number_0_to_1 = random.random() # Lower bound is included but upper bound is not included
print(random_number_0_to_1)

random_float=random.uniform(1,10) # Both Bounds are included
print(random_float)

if random_integer>=2.0:
    print("Heads")
else:
    print("Tails")

