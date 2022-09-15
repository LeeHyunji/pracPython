# 반복문(while)
#
# - 사용자의 입력을 받아 반복하는 프로그램을 만들어주세요
# - 사용자가 숫자를 입력했을 경우 입력값에 2배를 곱한 수를 출력해주세요
# - 사용자가 문자를 입력했을 경우 “입력한 문자는 {} 입니다.” 라는 문구를 출력해주세요
#     - {} 자리에는 사용자가 입력한 문자가 들어가야 합니다.
# - 사용자가 exit을 입력하거나 숫자가 5회 이상 입력됐을 경우 프로그램을 종료시켜주세요

i = 0

while i < 5:
    tmp = input("값을 입력해주세요. ")
    if tmp == "exit":
        break
    elif tmp.isnumeric():
        print(f'입력한 숫자의 2배는 {int(tmp)*2} 입니다.')
    else:
        print(f'입력한 문자는는 \'{tmp}\' 입니다.')
