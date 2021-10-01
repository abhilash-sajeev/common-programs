import math
def isKaprekar(num):
    sqr = num**2
    count = len(str(sqr))
    d = math.ceil(count/2)
    res = sqr//10**d + sqr%10**d
    
    return True if num - res == 0 else False

if __name__ == '__main__':
    num = int(input())
    print(isKaprekar(num))
