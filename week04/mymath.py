def factorial(n):
    """
    팩토리얼 함수 (재귀)
    :param n:
    :return: 결과값
    """
    if n == 0:
        return 1
    return n * factorial(n-1)

def factorial_iter(n):
    """
    팩토리얼 함수 (반복문)
    :param n:
    :return: 결과값
    """
    t = 1
    for i in range(2,n+1) :
        t = t*i
    return t
print(factorial_iter(5))