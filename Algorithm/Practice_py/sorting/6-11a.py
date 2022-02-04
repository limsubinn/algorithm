# 정렬
# 실전 문제2. 성적이 낮은 순서로 학생 출력하기
# 교재 코드

n = int(input())
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda student:student[1])
for student in array:
    print(student[0], end=' ')