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

# for i in range(0, len(marks), 1):
#     if marks[i] >= 60:
#         print(f'{i + 1}번 학생은 합격입니다.')
#     else:
#         print(f'{i + 1}번 학생은 불합격입니다.')

# number = 1
# for mark in marks:
#     if mark >= 60:
#         print(f'{number}번 학생은 합격입니다.')
#     else:
#         print(f'{number}번 학생은 불합격입니다.')
#     number += 1

# for idx, mark in enumerate(marks):
#     if mark >= 60:
#         print(f'{idx + 1}번 학생은 합격입니다.')
#     else:
#         print(f'{idx + 1}번 학생은 불합격입니다.')

# score = 0
# print(score)
# score += 50
# print(score)

# print(range(10))
# print(range(0, 10, 2))

# for idx in range(len(marks)):
#     if marks[idx] < 60:
#         continue
#         # break
#     print(f'{idx + 1}번 학생 축하합니다. 합격입니다.')

# for i in range(2, 10):
#     for j in range(1, 10):
#         print(i * j, end=", ")
#     print("")

# b = [1, 2, 3, 4]
# result = []
# print(result)
# for idx in b:
#     if idx == 4:
#         break
#     result.append(idx * 3)
# print(result)

# N = int(input())
# for idx, i in enumerate(range(N - 1, -1, -1)):
#     print(" " * i + "*" * (idx + 1))
#
# for idx, i in enumerate(range(N - 1, -1, -1)):
#     print(" " * i, "*" * (idx + 1))