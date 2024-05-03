class Secret:
    def __init__(self,code,where,time):
        self.code = code
        self.where = where
        self.time = time
a,b,c = map(str,input().split())
secret_code = Secret(a,b,c)

print("secret code :", secret_code.code)
print("meeting point :", secret_code.where)
print("time :", secret_code.time)