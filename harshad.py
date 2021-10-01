def isHarshad(num):
    number = num
    sod = 0
    while num:
        sod += num%10
        num = num//10

    return True if number%sod == 0 else False

if __name__ == '__main__':
    num = int(input())
    print(isHarshad(num))
