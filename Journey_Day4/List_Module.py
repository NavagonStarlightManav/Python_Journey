import random

Export_Value=10.56

states_of_America=["New York","Pennsylvania","New Jearsey","Georgia"]
print(states_of_America)

states_of_America[0]="Connecticut"

print(states_of_America[0])
print(states_of_America)

states_of_America.extend(["Angelaland","Jack Bauer Land"])
print(states_of_America)

friends=["Alice","Bob","Charlie","David","Emanuel"]
print(friends[random.randint(0,4)])

print(random.choice(friends))

num_of_states=len(states_of_America)
print(num_of_states)

dirty_foods=["Strawberries","Spinach","Kale","Apples","Onions","grapes"]

dirty_veg=["Spinach","Kale","Onions"]
dirty_fruits=["Strawberries","Apples","grapes"]

dirty_food=[dirty_veg,dirty_fruits]

print(dirty_food)
# 2 lists Immersed inside one list



