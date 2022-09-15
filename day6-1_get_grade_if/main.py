# 조건문
#
# 사용자의 시험 점수를 입력받아 등급을 출력하는 코드를 만들어주세요

def get_grade(score):
    if score > 100:
        return "잘못 입력된 점수입니다."
    elif score > 90:
        return "A"
    elif score > 80:
        return "B"
    elif score > 70:
        return "C"
    else:
        return "F"


score = int(input("이번 학기 시험 점수를 입력해주세요."))
grade = get_grade(score)
print(grade)  # A ~ F
