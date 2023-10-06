
pingpong_list = ["나영", "예진", "원빈", "현빈"]

def create_contents_of_mail(name):
    date = "2023-10-06"
    time = "10:30 AM"
    clothes = "트레이닝 복"

    content = f"한국교통대학교 천하제일 탁구대회, {name}님 탁구 대회에 참여해주셔서 감사합니다.\n"
    content += f"행사 일시: {date}, 시간: {time}, 복장: {clothes}\n"
    content += f"행사 당일에 뵙겠습니다. {name}님 감사합니다."

    return content


results = []

for participant in pingpong_list:
    email_content = create_contents_of_mail(participant)
    results.append(email_content)

for email in results:
    print(email)
