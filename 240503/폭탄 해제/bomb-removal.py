# 클래스 선언
class Bomb:
	def __init__(self, unlock_code, linear_color, time):
		self.unlock_code = unlock_code
		self.linear_color = linear_color
		self.time = time

# 변수 선언 및 입력
u_code, l_color, time = tuple(input().split())

# 객체 생성
b = Bomb(u_code, l_color, int(time))

# 출력
print(f"code : {b.unlock_code}")
print(f"color : {b.linear_color}")
print(f"second : {b.time}")