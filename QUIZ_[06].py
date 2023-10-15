class Bungoebbang:
    def __init__(self, contents):
        self.contents = contents

    def sell(self):
        print(f"{self.contents} 붕어빵이 판매되었습니다.")

    def eat(self):
        print(f"{self.contents} 붕어빵을 먹습니다.")

# "슈크림 붕어빵" 객체 생성
cream_bungoebbang = Bungoebbang("슈크림")

# "팥 붕어빵" 객체 생성
redbean_bungoebbang = Bungoebbang("팥")

# 판매와 먹기 테스트
cream_bungoebbang.sell()
cream_bungoebbang.eat()

redbean_bungoebbang.sell()
redbean_bungoebbang.eat()
