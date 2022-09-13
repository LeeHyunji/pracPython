# 계산기
#
# - 사용자의 입력을 받아 기능을 처리해주세요
# - 사용자가 입력한 숫자와 연산기호(+, -, *, /)에 따른 연산 결과를 출력해주세요
# - 더하기, 곱하기, 빼기, 나누기 기능을 하는 함수는 main.py가 아닌 다른 파일에서 작성해주세요

import re
from calc import calc

exp = input("계산이 필요한 간단한 식을 입력해주세요.")
num1, operator, num2 = re.split('([-|+|*|/])', exp)
result = calc.calc(int(num1), operator, int(num2))
print(f'결과 : {result}')
