
import re

def validate_resident_id(resident_id):
    # 주민등록번호 유효성 검사를 위한 정규표현식
    pattern = re.compile(r'^\d{6}[-]?[1-4]\d{6}$')

    # 정규표현식과 매치되는지 확인
    if not pattern.match(resident_id):
        return False

    # '-'를 제외한 숫자 부분을 추출
    resident_id_digits = re.sub(r'[-]', '', resident_id)

    # 유효한 날짜인지 확인
    birth_date = resident_id_digits[:6]
    if not is_valid_date(birth_date):
        return False

    # 유효한 체크 숫자 계산 및 확인
    check_digit = int(resident_id_digits[-1])
    if not is_valid_check_digit(resident_id_digits[:-1], check_digit):
        return False

    return True

def is_valid_date(birth_date):
    year = int(birth_date[:2])
    month = int(birth_date[2:4])
    day = int(birth_date[4:6])

    # 생년월이 유효한 범위인지 확인
    if year < 0 or (year > 20 and year < 99) or year > 99:
        return False

    if month < 1 or month > 12:
        return False

    # 2월일 경우 윤년 여부 확인
    if month == 2:
        if year % 4 == 0:
            if year % 100 != 0 or (year % 400 == 0 and year % 100 == 0):
                if day < 1 or day > 29:
                    return False
            else:
                if day < 1 or day > 28:
                    return False
        else:
            if day < 1 or day > 28:
                return False
    # 31일을 갖는 달인지 확인
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    # 30일을 갖는 달인지 확인
    else:
        if day < 1 or day > 30:
            return False

    return True

def is_valid_check_digit(resident_id_digits, check_digit):
    weights = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    sum = 0

    for i in range(12):
        sum += int(resident_id_digits[i]) * weights[i]

    remainder = sum % 11
    result = 11 - remainder

    if result >= 10:
        result -= 10

    return result == check_digit

# 주민등록번호 유효성 검사
resident_id = input("주민등록번호를 입력하세요 (예: YYMMDD-abcdefg 또는 YYYYMMDDabcdefg): ")
if validate_resident_id(resident_id):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")
