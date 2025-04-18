# try:
#    file=open("sample.txt")
#    a_dictionary={"key":"value"}
#    print(a_dictionary["key"])
# except FileNotFoundError:
#     file=open('sample.txt',"w")
#     file.write("something")
# except KeyError as error_message:
#     print("That key does not exist")
# else:
#     content=file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that i made up")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height>3:
    raise ValueError("Human Height should not be over 3 meters")
bmi = weight/height ** 2
print(bmi)





#keyError
# a_dictionary={"key":"value"}
# value = a_dictionary["non_existent_key"]

#IndexError
# fruit_list=["Apple","Banana","Pear"]
# fruit = fruit_list[3]

#TypeError
# text="abc"
# print(text+5)
