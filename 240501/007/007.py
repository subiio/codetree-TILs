sec,where,time= input().split()


class Secret:
    def __init__(self,sec,where,time):
        self.sec = sec
        self.where = where
        self.time = time

a =Secret(sec,where,time)

print("secret code :", a.sec)
print("meeting point :", a.where)
print("time :", a.time)