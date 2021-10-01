def sqrSum(num):
    res = 0
    while num:
        res += (num % 10)**2
        num = num // 10 
    return res

def isHappy(num):
    return True if num == 1 else isHappy(sqrSum(num))

if __name__ == '__main__':
    num = int(input())
    print(isHappy(num))
