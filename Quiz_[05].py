def print_구구단(var):
    print("구구단을 출력합니다.\n")
    for x in range(1, var + 1):
        print("------- [" + str(x) + "단] -------")
        for y in range(1, var + 1):
            print(x, "X", y, "=", x * y)
    print("---------------------")

var = int(input("몇 단까지 출력할까요?"))
print(var, type(var))

print_구구단(var)