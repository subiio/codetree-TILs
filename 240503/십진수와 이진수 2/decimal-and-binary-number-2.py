def make_10(string):
    num = 0
    string = list(string)

    for i in range(len(string)):
        num = num*2 + int(string[i])
    
    return num

def make_digit(num):
    num = 17*num
    list1 = [ ]
    while True:
        if num < 2:
            list1.append(num)
            break

        list1.append(num%2)
        
        num //= 2
    
    print(*list1[::-1],sep = '')

string =  input()

make_digit(make_10(string))