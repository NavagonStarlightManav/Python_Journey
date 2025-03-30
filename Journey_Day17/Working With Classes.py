class User:
    pass

user1=User()

user1.id="001"
user1.username="jack"

print(user1.username)

user2=User()
user2.id="002"
user2.username="Nancy"

print(user2.id)

# Now adding the concept of Constructors in the classes

class Userclass:
    def __init__(self,user_id,username):
        self.id=user_id
        self.username=username
        self.followers=0
        self.following=0

    def follow(self,user):
        user.followers+=1
        self.following+=1


user_1=Userclass("001","angela")
user_2=Userclass("002","Jack")

print(f"User 1 is {user_1.id} and {user_1.username}")
print(f"User 2 is {user_2.id} and {user_2.username}")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.following)
print(user_2.followers)
