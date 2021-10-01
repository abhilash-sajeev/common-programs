def isDudeney(num):
    cr = round(pow(num,1/3))
    while num:
        cr -= (num%10)
        num = num//10

    return True if cr==0 else False

if __name__ == '__main__':
    num = int(input())
    print(isDudeney(num))
