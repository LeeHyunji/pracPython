# - 클래스를 활용해 작성했던 계산기 코드를 활용해주세요 (day4-2_calculator_class 참조)
# - 기존처럼 사용자의 입력을 받고 출력하되, try / except를 활용해 사용자의 입력을 검증하는 코드를 추가해주세요
#     - 두 번쨰 숫자에 0을 입력하고 나누기를 시도할 경우 “0으로 나눌 수 없습니다” 문구를 출력해주세요
#     - 숫자가 아닌 다른 값을 입력했을 경우 “숫자만 입력 가능합니다” 라는 문구를 출력해 주세요


class Calulator():
    def set_number(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1+self.num2

    def subtract(self):
        return self.num1-self.num2

    def multiply(self):
        return self.num1*self.num2

    def divide(self):
        # ZeroDivisionError 예외 처리 : 나누는 값이 0이 나오면 Error msg 출력 처리
        try:
            result = self.num1 / self.num2
            return result
        except ZeroDivisionError:  # 0으로 나누면서 에러가 발생했을 때
            print("0으로는 나눌수 없습니다.")
            return "Error"
        except Exception as e:  # 위에서 정의하지 않은 에러가 발생했을 때(권장하지 않음)
            print(f"예상하지 못한 에러가 발생했습니다. error : {e}")


# 입출력시 예외 처리 : 올바른 입력값이 나올때까지 루프
while True:
    try:
        num1, num2 = input("계산할 숫자를 두개 입력해주세요.(띄어쓰기로 구분해주세요.)").split(" ")
        num1 = int(num1)
        num2 = int(num2)
        break
    except ValueError:  # int로 변환하는 과정에서 에러가 발생했을 떄
        print(f"숫자만 입력 가능합니다. 다시 입력해주세요.")

    except Exception as e:  # 위에서 정의하지 않은 에러가 발생했을 때(권장하지 않음)
        print(f"예상하지 못한 에러가 발생했습니다. 다시 입력해주세요. error : {e}")


calc = Calulator()
calc.set_number(num1, num2)
print(f'덧셈 {calc.num1}+{calc.num2} = {calc.add()}')
print(f'뺄셈 {calc.num1}-{calc.num2} = {calc.subtract()}')
print(f'곱셈 {calc.num1}*{calc.num2} = {calc.multiply()}')
print(f'나눗셈 {calc.num1}/{calc.num2} = {calc.divide()}')
