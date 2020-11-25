def  main():
    num = int(input("Enter the number: "))
    if check_prime(num):
        print(num * 10
    else:
        print("Its not a prime number")


def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True


def next():


if __name__ == "__main__" :
    main()