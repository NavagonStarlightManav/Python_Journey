enemies=1

def increase_enemies():
    enemies=2
    print(f"enemies inside function: {enemies}")
increase_enemies()
print(f"enemies outside function :{enemies}")

# a new variable initialised under if condition
game_level=10
enemies=["Skeleton","Zombie","Alien"]

if game_level<12:
    newest_enemy=enemies[0]
print(newest_enemy)


# Creating an empty string ensuring that variable always has value even if 'if' doesnt execute
def create_enemy():
    new_enemy=""
    if game_level<5:
        new_enemy=enemies[0]
    print(new_enemy)

def prime_number(number):
    count=True
    for num in range(2,int(number/2)+1):
        if number%num!=0:
            continue
        else:
            count=False
            print("Number is not prime ")
            break
    return count
print(prime_number(17))

#Use of global variable
enemies_a=1

def increase_enemies():
    global enemies_a
    enemies_a+=1
    print(f"enemies inside function: {enemies_a}")
increase_enemies()
print(f"enemies outside function :{enemies_a}")

#Without use of global updating global scope variable within a function
enemies_a=1

def increase_enemies(enemy):
    print(f"enemies inside function: {enemies_a}")
    return enemies_a+1
enemies_a=increase_enemies(enemies_a)
print(f"enemies outside function :{enemies_a}")

#defining global variables and using them in whole worksheet, they are always used in capitals
PI=3.14159
GOOGLE_URL="MANAV GOYAL"

print(PI)
print(GOOGLE_URL)
