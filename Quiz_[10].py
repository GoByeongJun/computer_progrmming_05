import random


def generate_lotto_numbers():
    lotto_numbers = []

    while len(lotto_numbers) < 6:
        number = random.randint(1, 45)

        if number not in lotto_numbers:
            lotto_numbers.append(number)

    lotto_numbers.sort()


    print(f"생성된 로또 번호는 {lotto_numbers} 입니다.")


generate_lotto_numbers()
