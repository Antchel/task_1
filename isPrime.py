def is_prime(value: int):
    if 1 == value:
        return False
    if value % 2 == 0:
        return value == 2
    tmp = 3
    while tmp * tmp <= value and value % tmp != 0:
        tmp += 2
    return tmp ** 2 > value


while True:
    try:
        number = int(input("Enter a number : "))
        if number < 0:
            raise Exception
        if is_prime(number):
            print("Entered number is a prime")
        else:
            print("Entered number is not a prime")
    except ValueError:
        print("Wrong number, try again please!")
    except Exception:
        print("Enter a positive value")
