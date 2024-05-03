class NextLevel:
    def __init__(self,Id="",level=0):
        self.Id = Id
        self.level = level

codetree = tuple(input().split())


user1 = NextLevel()

user1.Id = "codetree"
user1.level = 10

user2 = NextLevel()

user2.Id = codetree[0]
user2.level = codetree[1]

print(f"user {user1.Id} lv {user1.level}")
print(f"user {user2.Id} lv {user2.level}")