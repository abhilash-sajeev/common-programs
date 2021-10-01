def isNeon(num):
    sqr = num**2
    while sqr:
        num -= sqr%10
        sqr = sqr//10
    
    return True if num == 0 else False

if __name__ == '__main__':
    num = int(input())
    print(isNeon(num))
