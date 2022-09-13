# - 설정한 숫자를 계산해줄 클래스를 선언해주세요
# - 메소드를 호출해서 num1, num2를 설정할 수 있도록 해주세요
# - 입력된 숫자의 더하기, 빼기, 곱하기, 나누기 연산 결과를 구하는 메소드를 생성해주세요


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
        return self.num1 / self.num2


num1, num2 = input("계산할 숫자를 두개 입력해주세요.(띄어쓰기로 구분해주세요.)").split(" ")

calc = Calulator()
calc.set_number(int(num1), int(num2))
print(f'덧셈 {calc.num1}+{calc.num2} = {calc.add()}')
print(f'뺄셈 {calc.num1}-{calc.num2} = {calc.subtract()}')
print(f'곱셈 {calc.num1}*{calc.num2} = {calc.multiply()}')
print(f'나눗셈 {calc.num1}/{calc.num2} = {calc.divide()}')
