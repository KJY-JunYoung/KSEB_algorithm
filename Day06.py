def is_even(n) -> bool:

    """
    짝수 판정 함수
    :param n: 판정할 정수
    :return: 짝수면 True, 홀수면 False
    """

    return not n & 1

def DectoOcto(n) -> int:

    if n == 0:
        return ""
    else:
        return DectoOcto(n // 8) + str(n % 8)



n= int (input())
print(DectoOcto(n))


