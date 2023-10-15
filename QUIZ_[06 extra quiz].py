class Bungoebbang:
    def __init__(self, contents, price):
        self.contents = contents
        self.price = price
        self.total_sales = 0

    def sell(self):
        print(f"{self.contents} 붕어빵이 {self.price}원에 판매되었습니다.")
        self.total_sales += self.price
        print(f"총 판매금: {self.total_sales}원")

    def eat(self):
        print(f"{self.contents} 붕어빵을 먹습니다.")

# "슈크림 붕어빵" 객체 생성, 가격 1500원
cream_bungoebbang = Bungoebbang("슈크림", 1500)

# "팥 붕어빵" 객체 생성, 가격 1000원
redbean_bungoebbang = Bungoebbang("팥", 1000)

# 판매와 먹기  테스트
cream_bungoebbang.sell()
cream_bungoebbang.eat()

redbean_bungoebbang.sell()
redbean_bungoebbang.eat()
