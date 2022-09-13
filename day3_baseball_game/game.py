import random
import time
from datetime import timedelta


def play(numLen):
    print("\n\n ------------------------- Game Start -------------------------")

    # # 1. 랜덤 숫자 설정하기
    num = set_num(numLen)

    # # 2. 게임시작하기
    count = 0
    results = []
    start = time.time()

    while (play):
        # # 2-1. 답 올바르게 입력받기
        ans = input("정답은! ")
        if ans == "exit":
            print("종료합니다.")
            break
        elif not (ans).isdigit():
            print("숫자만 입력해주세요.")
            continue
        elif (len(ans) != numLen):
            print(f"{numLen}자리 숫자만 입력해주세요.")
            continue
        else:
            ans = list(map(int, ans))

        # # 2-2. 정답 확인 후 접수판에 기록하기
        score = check_score(ans, num, numLen)
        results.append(score)
        print(score)

        # # 2-4. 정답인지 체크하고 정답이면 종료하기
        if score['strike'] == numLen:
            print("정답!\n\n")
            end = time.time()
            break

    # # 3. 게임 기록 및 점수판 확인하기
    print(f'-------------------------- Game Score --------------------------')
    print(f'정답 {num} 까지 시도 횟수 {len(results)} 걸린 시간 {timedelta(seconds=end-start)}')
    for i, score in enumerate(results):
        print(f'{i}번째 점수 : {score}')


def set_num(numLen):
    num = []
    while (len(num) < numLen):
        rand = random.randrange(0, 10)
        if rand not in num:  # 새로운 수가 중복이 아니면,
            num.append(rand)  # 리스트에 추가
    return num


def check_score(ans, num, numLen):
    score = {
        "ans": ans,
        "strike": 0,
        "ball": 0,
        "out": 0,
    }
    for i in range(numLen):
        if ans[i] == num[i]:
            score["strike"] += 1
        elif ans[i] in num:
            score["ball"] += 1
        else:
            score["out"] += 1

    return score
