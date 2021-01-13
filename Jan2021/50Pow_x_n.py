# Author: Hailin Xiao(hlxiao@accuray.com)
# Date: 1/13/2021 
# Purpose:


def myPow(x: float, n: int) -> float:
    # Time Limit Exceeded Solution #
    '''
    result = 1
    is_negative = False
    if n < 0:
        is_negative = True
        n = 0 - n
    for i in range(n):
        result *= x
    result = round(result, 4)
    return 1 / result if is_negative else result
    '''
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n
    half = myPow(x, n // 3)
    if n % 2:
        return half * half * x
    else:
        return half * half
