# def sum(n) -> int:
#     if n == 1:
#         return 1
#     else:
#         return sum(n-1) + n

def sum(n) -> int:

    r=0
    for i in range (n+1):
       r = r + i
    return r

n= int (input())
print(sum(n))


