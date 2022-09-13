# 숫자 야구 게임
#
# - 프로그램이 시작되면 슷자야구 게임을 몇 자리 숫자로 할 건지 입력 받기 (최대 10자리)
# - 첫 번째 입력을 받은 자릿수 만큼 후 파이썬으로 중복 없는 랜덤한 수를 생성해 주세요
# - 사용자가 숫자를 입력 했을 때 숫자야구 게임의 규칙에 맞게 ball / out count를 출력해 주세요
# - 사용자가 정답을 맞춘 경우 아래 항목들을 출력해 주세요
#     - 사용자가 정답을 맞추기까지 입력 한 횟수
#     - 사용자가 게임을 시작해서 정답을 맞추기까지 소요된 시간
#     - 정답을 맞춘 시점의 날짜/시간
# - 게임을 진행하던 도중, “exit”을 입력할 경우 프로그램을 종료해 주세요


from game import play

MIN = 1  # numLen 최소값
MAX = 10  # numLen 최대값


def main():
    play_on = "y"
    # 0. 게임설정 : 숫자야구게임에 필요한 자리수 받아오기
    #       -> 입력값이 "exit"이면 종료
    #       -> 문자이면 재입력
    #       -> numLen는 MIN(1)이상 MAX(10)이하 여야한다.
    while (play_on == "y"):
        numLen = input("\n숫자 야구 게임을 몇자리 숫자로 할 것인지 입력해주세요.")
        if numLen == "exit":
            print("종료합니다.")
            play_on = "n"
            break
        elif not (numLen).isdigit():
            print("숫자만 입력해주세요.")
        elif (int(numLen) > MAX) | (int(numLen) < MIN):
            print(f"{MIN}이상 {MAX}이하의 숫자만 입력해주세요.")
        else:
            numLen = int(numLen)
            play(numLen)
            play_on = input("\n계속 게임을 하려면 y를 눌러주세요.")


main()
