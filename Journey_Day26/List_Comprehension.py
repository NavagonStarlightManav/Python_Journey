numbers=[1,2,3]

new_numbers=[n+1 for n in numbers]

name = "Angela"
letters_list = [letter for letter in name]

names=['Alex','Beth','Caroline','Eleanor','Freddie']
short_names=[name.upper() for name in names if len(name)>=5]
print(short_names)