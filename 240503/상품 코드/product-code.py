# 클래스 선언
class Product:
    def __init__(self, prod_id, code):
        self.prod_id = prod_id
        self.code = code

        
# 첫 번째 상품 생성
product1 = Product("codetree", 50)

# 변수 선언 및 입력
prod2_id, code2 = tuple(input().split())

# 두 번째 상품 생성
product2 = Product(prod2_id, int(code2))

# 출력
print(f"product {product1.code} is {product1.prod_id}")
print(f"product {product2.code} is {product2.prod_id}")