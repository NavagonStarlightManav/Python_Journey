def format_name(first_name,last_name):
    Full_name=(first_name+" "+last_name).title()
    return Full_name

# title and lower can be used for converting strings

# multiple return values can be used and conditional returns can also be involved

# with the help of docstrings we can add multi line documentation to our own created functions

# remember that functions treats return statement as last statement

name=format_name("manav","goyal")
print(f"The name is {name}")

name2=format_name((input("Please enter your first name sir")),input("Please enter your last name sir"))
print(name2)

def is_leap_year(year):
    """ This will analyse the year as leap year or not
         base on divisibility by 4,100,400
    """
    Result=True
    if year%4==0:
        if year%100==0:
            if year %400==0:
                return Result
            else:
                Result=False
                return Result
        else:
            return Result
    else:
        Result=False
        return False

Result=is_leap_year(1900)
print(Result)

# Doc Strings can be used as a multi line comment
"""
i would love to go out with you
but there may be slight difficulties
hope u understand
"""

# but assigning to a variable becomes multi line string variable

multi_line_string="""
i would love to go out with you
but there may be slight difficulties
hope u understand
"""
print(multi_line_string)

# You can directly assign functions to symbols using dictionary and smart approach

def add(a,b):
    return a+b
def subract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

operations={
    "+":add,
    "-":subract,
    "*":multiply,
    "/":divide,
}

print(operations["+"](15,20))

for symbol in operations:
    print(symbol)
operation_symbol=str(input("Please enter operation symbol"))
result=operations[operation_symbol](10,20)
print(result)