# - 인스턴스를 선언할 때 가로, 세로 길이를 받을 수 있는 클래스를 선언해 주세요
# - 인스턴스에서 사각형, 삼각형, 원의 넓이를 구하는 메소드를 생성해주세요
# - 원의 넓이를 계산할 때는 세로 길이는 무시하고, 가로 길이를 원의 지름이라 가정하고 계산해 주세요

# 클래스 : 가로 b, 세로 h, 타입 type
# - 함수 : 넓이 구하기

from math import pi


class Figure():
    def __init__(self, type, b, h):
        print(f"도형의 타입: {type} / 가로={b} 세로={h}")
        self.type = type
        self.b = b
        self.h = h

    def area(self):
        if self.type == "square":
            return self.b*self.h
        elif self.type == "rectangle":
            return self.b*self.h % 2
        elif self.type == "circle":
            r = self.b % 2
            return pi*r**2
        else:
            return


type, b, h = input("도형의 타입, 가로, 세로를 입력해주세요.(띄어쓰기로 구분해주세요)\n").split(" ")
my_rectangle = Figure(type, int(b), int(h))
print(f'도형의 넓이는 {my_rectangle.area()}')
