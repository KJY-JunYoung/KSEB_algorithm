import random

try:
    with open("student.csv", 'r') as fp:
        students_list = fp.readlines()
        students_list.remove("***\n") # 특정 이름 제거
        students_list.remove("***\n")
        students_list.remove("***\n")
        students_list.remove("***\n")
        students_list.remove("***\n")

        for _ in range(3):
            random_pick = random.choice(students_list)
            print(random_pick, end='')
            students_list.remove(random_pick)

        # if "***\n" in students_list:
        #     print("!")
        # print(students_list[1], end='')

except FileNotFoundError as err:
    print(err)