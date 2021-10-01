def isPerfect(num):
    number = num
    for i in range(1, num//2+1):
        if num%i == 0:
            number -= i

    return True if number==0 else False

if __name__ == '__main__':
    num = int(input())
    print(isPerfect(num))
