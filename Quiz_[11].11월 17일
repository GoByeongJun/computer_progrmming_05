class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate(self, quantity):
        total_price = self.price * quantity
        return total_price

Coffee = Beverage("커피", 3000)
GreenTea = Beverage("녹차", 2500)
IceTea = Beverage("아이스티", 3000)

selected_beverage = input("주문할 음료를 선택하세요 (커피/녹차/아이스티): ")
selected_beverage = selected_beverage.strip()

if selected_beverage not in ["커피", "녹차", "아이스티"]:
    print("잘못된 음료를 선택하셨습니다.")
else:
    quantity = int(input("수량을 입력하세요: "))

    if selected_beverage == "커피":
        total = Coffee.calculate(quantity)
    elif selected_beverage == "녹차":
        total = GreenTea.calculate(quantity)
    else:
        total = IceTea.calculate(quantity)

    print(f"{selected_beverage} {quantity}잔의 가격은 {total}원 입니다.")
