import random

try:
    with open("student.csv", 'r') as fp: # csv 파일 불러오기 ('r' = read mode)
        students_list = fp.readlines() # csv 파일 읽기
        students_list.remove("***\n") # 특정 이름 제거
        students_list.remove("***\n")
        students_list.remove("***\n")
        students_list.remove("***\n")
        students_list.remove("***\n") # remove 함수로 list에서 특정 인원 이름 제거

        for _ in range(3): # 3회 반복
            random_pick = random.choice(students_list) # 특정 인원 추출
            print(random_pick, end='') #
            students_list.remove(random_pick)

        # if "***\n" in students_list:
        #     print("!")
        # print(students_list[1], end='')

except FileNotFoundError as err: # file not found error message
    print(err)