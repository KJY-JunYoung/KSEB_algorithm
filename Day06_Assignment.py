# v1.4) https://github.com/inhadeepblue/2024_KEB_datastructure_algorithm 의
# v0.7 guess number 예제를 자동화하고 로그 파일(guess.txt)을 남기도록 코드를 수정하시오.
# 단, 해당 프로그램이 로그시간을 갖도록 한다.

import random

low = 1
high = 100

def auto_input_number(low, high) -> int:
    return (low + high) // 2

answer = random.randint(1, 100)
chance = 7

with open("guess.txt", 'w') as fp:
    fp.write(f'Chance : {chance}\n')
    while chance != 0:
        guess = auto_input_number(low, high)
        if guess == answer:
            print(f'You win. Answer is {answer}')
            fp.write(f'You win. Answer is {answer}\n')
            break
        elif guess > answer:
            chance = chance - 1
            print(f'{guess} is bigger. Chance left : {chance}')
            fp.write(f'{guess} is bigger. Chance left : {chance}\n')
            high = guess
        else:
            chance = chance - 1
            print(f'{guess} is lower. Chance left : {chance}')
            fp.write(f'{guess} is lower. Chance left : {chance}\n')
            low = guess
    else:
        print(f'You lost. Answer is {answer}')
        fp.write(f'You lost. Answer is {answer}\n')

