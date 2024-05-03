class Secret:
    def __init__(self,code,where,time):
        self.code = code
        self.where = where
        self.time = time

secret_code = Secret('codetree','L',13)

print("secret code :", secret_code.code)
print("meeting point :", secret_code.where)
print("time :", secret_code.time)