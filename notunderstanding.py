# A, B = map(int, input().split())

# N = int(input())

# for i in range(1, 10):
    # print(f'{N} * {i} = {N * i}')
    # print("{} * {} = {}".format(N, i, N * i))

# for i in range(0, 9, 2):
#     print(f'{N} * {i + 1} = {N * (i + 1)}')

# count = 1
# while True:
#     if count == 10:
#         break
#     print(f'{N} * {count} = {N * count}')
#     count += 1

#while문 prompt, while

coffee = 10
print("돈을 넣어주세요: ")
money = 300

while True:
    if money == 300:
        print(f"{money}원을 받았습니다. 잠시만 기다리시면 커피가 나옵니다.")
        coffee = coffee-1
    elif money > 300:
        print(f"{money-300}원을 주고 커피를 줍니다.")
        coffee = coffee-1
    else:
        print(f"돈이 모자랍니다. {300 - money}원을 더 넣어주세요.")
        print(f"남은 커피의 양은 {coffee}개 입니다.")
        if coffee == 0:
            print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
            break