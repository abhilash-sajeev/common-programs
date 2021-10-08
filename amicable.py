def SoF(num):
    sum = 1
    for i in range(2,num):
        if num%i == 0:
            sum+=i
    return sum

def isAmicable(num1, num2):
    return True if SoF(num1) == num2 and SoF(num2) == num1 else False

if __name__ == '__main__':
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(isAmicable(num1, num2))
